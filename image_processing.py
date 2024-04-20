from PIL import Image


def shrink_image(file):
  img = Image.open(file)
  img = img.resize((100, 100))
  img.save(file)
  img.show()


if __name__ == "__main__":
  shrink_image("images/sample2.png")
