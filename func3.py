from PIL import Image
from PIL import ImageEnhance
def enhance(img):
    userimg = Image.open(img)
    enh = ImageEnhance.Contrast(userimg)
    enh.enhance(1.8).show("More Contrast")
