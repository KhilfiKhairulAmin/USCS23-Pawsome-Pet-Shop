from PIL import Image


def shrink_image(file):
  img = Image.open(file)
  img = img.resize((50, 50))
  img.save(file)
  img.show()


if __name__ == "__main__":
  shrink_image("images/1/50x50.png")
  shrink_image("images/2/50x50.png")
