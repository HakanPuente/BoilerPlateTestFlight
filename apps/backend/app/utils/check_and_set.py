from django.shortcuts import get_object_or_404
from graphql_relay import from_global_id


def check_and_set_field(input_data, instance, field_name):
    value = input_data.get(field_name, "undefined")
    if value != "undefined":
        setattr(instance, field_name, value)


def check_and_set_foreign_id(
        input_data, input_field_name, instance, instance_field_name=None
):
    foreign_global_id = input_data.get(input_field_name, "undefined")
    if foreign_global_id is None:
        setattr(instance, instance_field_name or input_field_name, None)
    elif foreign_global_id != "undefined":
        foreign_id = from_global_id(foreign_global_id)[1]
        setattr(instance, instance_field_name or input_field_name, foreign_id)

