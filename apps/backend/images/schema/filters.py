from django_filters import FilterSet, OrderingFilter, Filter
from ..models import Image, ImageGroup
from django.db.models import Q


class ImageGroupFilter(FilterSet):
    class Meta:
        model = ImageGroup
        fields = {
            "super_search": ["super_search"],
            "has_file": ["has_file"],
            "sort_by": ["exact"],
        }

    super_search = Filter(method="filter_super_search")
    has_file = Filter(method="filter_has_file")
    sort_by = Filter(method="filter_sort_by")

    def filter_super_search(self, queryset, name, value):
        pass
        return None

    def filter_has_file(self, queryset, name, value):
        if value:
            return queryset.filter(Q(images__external_url=None)).distinct()
        return queryset.filter(~Q(images__file=None)).distinct()

    @property
    def qs(self):
        return super(ImageGroupFilter, self).qs

    def filter_sort_by(self, queryset, name, values):
        return None


class ImageFilter(FilterSet):
    class Meta:
        model = Image
        fields = {
            "name": ["icontains"],
            "height": ["gt", "lt", "exact"],
            "width": ["gt", "lt", "exact"],
        }

    order_by = OrderingFilter(fields=(("height", "width"),))
