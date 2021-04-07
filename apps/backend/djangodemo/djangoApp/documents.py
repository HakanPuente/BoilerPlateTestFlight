from django.conf import settings

from django_elasticsearch_dsl import Document, Index, fields

from django_elasticsearch_dsl.registries import registry
from .models import MyModel

@registry.register_document
class MyModelDocument(Document):
    
    # year = fields.CompletionField()
    # name = fields.CompletionField()
    # country = fields.CompletionField()
    # productID = fields.CompletionField()
    # id = fields.CompletionField()

    class Index:
        name = 'mymodels'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    
    id = fields.IntegerField(attr='id')
    name = fields.TextField(
        # analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    country = fields.TextField(
        # analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    year = fields.TextField(
        # analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    productID = fields.FloatField(
        # analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    class Django:
        model = MyModel

        fields = [
                    
        ]

