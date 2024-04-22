"""
Program: image_upload.py
Author: Khilfi
Handles image upload, image pre-processing, and image saving in the program file
"""

from PIL import Image
from breezypythongui import EasyFrame
import tkinter.filedialog
import os


class ImageUpload(EasyFrame):
  
  def __init__(self):
    """Sets up the window and widgets."""
    EasyFrame.__init__(self, "File Dialog Demo")
    self.outputArea = self.addTextArea("", row = 0, column = 0, width = 80, height = 15)
    self.addButton(text = "Open", row = 1, column = 0, command = self.openFile)

  # Event handling method.
  def openFile(self):
    """Pops up an open file dialog, and if a file is selected, displays its text in the text area and its pathname in the title bar."""
    fList = [("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
    fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
    imageId = 100
    os.makedirs(f"images/{imageId}")

    with Image.open(fileName) as img:
      img.save(f"images/{imageId}/original.png")
      img_1 = img.resize((200, 200))
      img_1.save(f"images/{imageId}/200x200.png")
      img_2 = img.resize((100, 100))
      img_2.save(f"images/{imageId}/100x100.png")
      img_3 = img.resize((50, 50))
      img_3.save(f"images/{imageId}/50x50.png")


if __name__ == "__main__":
  ImageUpload().mainloop()
