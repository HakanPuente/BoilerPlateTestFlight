import graphene
from graphene import relay
from graphql_relay import from_global_id
from .types import ImageGroupNode, ImageGroupEdge
from django.db import transaction
from ..models import ImageGroup
from django.shortcuts import get_object_or_404
from graphql_relay.connection.arrayconnection import offset_to_cursor
from app.utils.resize_images import create_and_upload_resized_images
from app.utils.check_and_set import check_and_set_field


class CreateImageGroupMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        tags = graphene.List(graphene.String)
        cover_photo = graphene.ID()

    image_group = graphene.Field(ImageGroupNode)
    image_group_edge = graphene.Field(ImageGroupEdge)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        image_group = ImageGroup()
        check_and_set_field(data, image_group, "name")
        check_and_set_field(data, image_group, "tags")
        image_group.save()

        image_edge = ImageGroupEdge(cursor=offset_to_cursor(0), node=image_group)
        uploaded_img = info.context.FILES.get("image", None)
        if uploaded_img:
            create_and_upload_resized_images(image_group, uploaded_img)

        return CreateImageGroupMutation(
            image_group=image_group, image_group_edge=image_edge
        )


class UpdateImageGroupMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        tags = graphene.List(graphene.String)

    image_group = graphene.Field(ImageGroupNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        with transaction.atomic():
            image_group = get_object_or_404(
                ImageGroup, pk=from_global_id(data["id"])[1]
            )
            check_and_set_field(data, image_group, "name")
            check_and_set_field(data, image_group, "tags")
            image_group.images.all().delete(save=False)
            image_group.save()
            # image_edge = ImageGroupEdge(cursor=offset_to_cursor(0), node=image_group)
            uploaded_img = info.context.FILES.get("image", None)
            if uploaded_img:
                create_and_upload_resized_images(image_group, uploaded_img)

            return UpdateImageGroupMutation(image_group=image_group)


class DeleteImageGroupMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    deletedId = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **data):
        with transaction.atomic():
            image_group = get_object_or_404(
                ImageGroup, pk=from_global_id(data["id"])[1]
            )
            image_group.delete()
            return DeleteImageGroupMutation(deletedId=data["id"])


class Mutation(graphene.ObjectType):
    create_image_group = CreateImageGroupMutation.Field()
    update_image_group = UpdateImageGroupMutation.Field()
    delete_image_group = DeleteImageGroupMutation.Field()
