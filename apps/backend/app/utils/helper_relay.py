from django.shortcuts import get_object_or_404
from graphql_relay.node.node import from_global_id


def get_object(model_cls, relay_id, otherwise="undefined", **kwargs):
    try:
        return get_object_or_404(model_cls, pk=from_global_id(relay_id)[1], **kwargs)
    except Exception as e:
        if otherwise != "undefined":
            return otherwise
        else:
            raise e


def get_objects(object_name, relay_ids):
    return list(
        object_name.objects.filter(id__in=[from_global_id(id)[1] for id in relay_ids])
    )


def update_create_instance(instance, args, exception=["id"]):
    if instance:
        [
            setattr(instance, key, value)
            for key, value in args.items()
            if key not in exception
        ]

    instance.save()

    return instance
