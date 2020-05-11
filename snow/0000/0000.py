from PIL import Image, ImageDraw, ImageFont


with Image.open("picture.jpg") as im:
    font = ImageFont.truetype("Arial.ttf", 20)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    draw.text((4*width/5, 4), "+5", fill=(255, 0, 0), font=font)
    # im.show()
    im.save("newpic.jpg")
