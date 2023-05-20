import unittest
from png_exporter import PNGExporter


class PNGExporterTest(unittest.TestCase):
    def test_png_exporter(self):
        # Test für den PNGExporter
        exporter = PNGExporter("image.png", b"image data", 90)
        self.assertEqual(exporter.name, "image.png")
        self.assertEqual(exporter.data, b"image data")
        self.assertEqual(exporter.quality, 90)


if __name__ == '__main__':
    unittest.main()
