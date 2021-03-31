from django.http import Http404
from graphql_relay.node.node import from_global_id


def get_object(model_cls, relay_id):
    try:
        model_cls.objects.get(pk=from_global_id(relay_id)[1])
    except model_cls.DoesNotExist:
        raise Http404("Model object does not exist")


def get_objects(object_name, relay_ids):
    return list(
        object_name.objects.filter(id__in=[from_global_id(id)[1] for id in relay_ids])
    )


def update_create_instance(instance, args, ignore=None):
    if ignore is None:
        ignore = ['id']

    if instance:
        [
            setattr(instance, key, value)
            for key, value in args.items()
            if key not in ignore
        ]

    instance.save()

    return instance
