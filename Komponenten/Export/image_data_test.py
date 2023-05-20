import unittest
from image_data import ImageData


class ImageDataTest(unittest.TestCase):
    def test_image_properties(self):
        # Test für die Eigenschaften der Bild-Daten
        image_data = ImageData(b"image data", 640, 480)
        self.assertEqual(image_data.height, 640)
        self.assertEqual(image_data.width, 480)


if __name__ == '__main__':
    unittest.main()
