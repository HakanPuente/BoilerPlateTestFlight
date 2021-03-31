from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from ..models import ImageGroup, Image


class ImagesByImageGroupIdLoader(DataLoader):

    def batch_load_fn(self, image_group_ids):
        image_by_image_group_ids = defaultdict(list)
        queryset = Image.objects.filter(image_group_id__in=image_group_ids).order_by('image_group_id', 'width')
        for image in queryset.iterator():
            image_by_image_group_ids[image.image_group_id].append(image)
        return Promise.resolve(
            [
                image_by_image_group_ids.get(image_group_id, [])
                for image_group_id in image_group_ids
            ]
        )
