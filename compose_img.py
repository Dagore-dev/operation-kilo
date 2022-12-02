from PIL import Image

def compose_img (destination: str, template: str, number: int):
    new = Image.new("YCbCr", (3500,2200))

    img = Image.open(template)
    plot = Image.open(destination + str(number) + ".jpg")
    new.paste(img, (0,0))

    new.paste(plot, (675, 350))
    new.save(destination + str(number) + '.jpg')
