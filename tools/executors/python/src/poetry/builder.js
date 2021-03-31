// @ts-check
/**
 * @typedef {import("./builder").Options} Options
 */
const { createBuilder } = require("@angular-devkit/architect");
const childProcess = require("child_process");
const { Observable } = require("rxjs");

/** @param {Options} _options */
function builder(_options, context) {
  const cwd = `${context.currentDirectory}/apps/${context.target.project}`;
  context.logger.info(`Executing "poetry run"...`);
  context.logger.info(`Options: ${JSON.stringify(_options, null, 2)}`);
  const child = childProcess.spawn("poetry", [_options.command, ...(_options.args || [])], { cwd });
  return new Observable((observer) => {
    child.stdout.on('data', (data) => {
      context.logger.info(data.toString());
    });
    child.stderr.on('data', (data) => {
      context.logger.error(data.toString());
    });
    child.on('close', (code) => {
      context.logger.info(`Done.`);
      observer.next({ success: code === 0 });
      observer.complete();
    });
  });
}

module.exports.default = createBuilder(builder);
