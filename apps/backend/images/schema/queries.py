from graphene import relay, ObjectType
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import ImageGroupNode
from .filters import ImageGroupFilter


class Query(ObjectType):
    image_group = relay.Node.Field(ImageGroupNode,)
    all_image_groups = DjangoFilterConnectionField(
        ImageGroupNode,
        super_search=graphene.String(),
        lang=graphene.String(),
        has_file=graphene.Boolean(),
        sort_by=graphene.List(graphene.String),
    )

    def resolve_all_image_groups(self, info, **kwargs):
        return ImageGroupFilter(kwargs, request=info.context).qs
