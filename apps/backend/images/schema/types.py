from graphene import relay, ObjectType
import graphene
from graphene_django import DjangoObjectType
from ..models import Image, ImageGroup


class ImageFileType(ObjectType):
    name = graphene.String()
    url = graphene.String()

    def resolve_url(self, info, **kwargs):
        return self.url


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        filter_fields = ["name", "width", "height"]
        interfaces = (relay.Node,)

    file = graphene.Field(ImageFileType)

    def resolve_file(self, info, **kwargs):
        return self.file if self.file else None


ImageEdge = ImageNode._meta.connection.Edge


class ImageConnection(relay.Connection):
    class Meta:
        node = ImageNode


class ImageGroupNode(DjangoObjectType):
    images = relay.ConnectionField(ImageConnection, order_by=graphene.String())

    class Meta:
        model = ImageGroup
        interfaces = (relay.Node,)
        filter_fields = []

    def resolve_images(self, info, **kwargs):
        return info.context.images_image_group_id_loader.load(self.id)


ImageGroupEdge = ImageGroupNode._meta.connection.Edge
