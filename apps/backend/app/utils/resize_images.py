import threading
import stringcase
import os
import io
from django.db import transaction
from images.models import Image
from .image import scale_image, image_to_file_obj
from django import db
"""
To make the user experience better, 
we use threading module to make upload functionality in background
"""


def resize_img(image_group, img, filename, ext):
    scaled_imgs = scale_image(img)
    for (img, size) in scaled_imgs:
        with transaction.atomic():
            print("saving", img, size)
            thumbnail = Image.objects.create(
                name=f"{image_group.name} ({size})",
                height=img.height,
                width=img.width,
                image_group=image_group,
            )
            file_obj = image_to_file_obj(img)
            thumbnail.file.save(
                f"{stringcase.spinalcase(image_group.name)}-{size}-{image_group.id}{ext}",
                file_obj,
            )
            thumbnail.save()
    image_group.processed = True
    image_group.save()


def resize_worker(*args, **kwargs):
    resize_img(*args, **kwargs)
    db.connections.close_all()


def create_and_upload_resized_images(image_group, img):
    # resize_worker(image_group, img)
    image_file = io.BytesIO(img.read())
    filename, ext = os.path.splitext(img.name)
    if not filename or not ext:
        raise Exception(
            "Cover photo must be a valid image with a proper extension (.jpg, .png, etc.)"
        )
    t = threading.Thread(
        target=resize_worker, args=(image_group, image_file, filename, ext)
    )
    t.setDaemon(True)
    t.start()
