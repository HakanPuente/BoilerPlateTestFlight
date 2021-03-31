from PIL import Image, ImageFile
import io

SIZES = [
    (128, 128),
    (256, 256),
    (512, 512),
    (720, 720),
    (1080, 1080),
    (1280, 1280),
    (1920, 1920),
]


def scale_image(img_file):
    im = Image.open(img_file)
    ims = [(im, "original")]

    aspect_ratio = 16.0 / 9.0
    image_x, image_y = im.size
    width = min(image_x, image_y * aspect_ratio)
    height = min(image_x / aspect_ratio, image_y)
    left = (image_x - width) / 2
    top = (image_y - height) / 2
    box = (left, top, left + width, top + height)
    cropped = im.crop(box)

    for size in SIZES:
        new_img = cropped.copy()
        new_img.thumbnail(size)
        ims.append((new_img, str(size[0])))
    return ims


def image_to_file_obj(img):
    b = io.BytesIO()
    if img.mode in ("RGBA", "LA"):
        img.save(b, "PNG")
    else:
        try:
            img.save(b, "JPEG", quality=80, optimize=True, progressive=True)
        except IOError:
            ImageFile.MAXBLOCK = img.size[0] * img.size[1]
            img.save(b, "JPEG", quality=80, optimize=True, progressive=True)

    b.seek(0)
    return b
