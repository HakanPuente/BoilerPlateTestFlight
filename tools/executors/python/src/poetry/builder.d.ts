import type { BuilderOutput, createBuilder } from "@angular-devkit/architect";
import type { json } from "@angular-devkit/core";
import type { Observable } from "rxjs";

export interface Options extends json.JsonObject {
  command: string;
  args?: string[];
}

declare function builder(options: Options, context: BuilderOutput): Observable<BuilderOutput>;

interface Callable<ReturnType> {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (...args: any[]): ReturnType;
}

type GenericReturnType<ReturnType, F> = F extends Callable<ReturnType>
  ? ReturnType
  : never;

declare const _default: ReturnType<GenericReturnType<typeof builder, typeof createBuilder>>;
export default _default;
