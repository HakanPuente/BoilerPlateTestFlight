import graphene
import images.schema


class Mutation(images.schema.Mutation, graphene.ObjectType):
    pass


class Query(images.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
