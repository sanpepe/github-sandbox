import unittest

class WebSandUniTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(WebSandUniTest, self).__init__(*args, **kwargs)

    def setUp(self):
        print("WebSandUniTest setUp")

    def test_assert_websand(self):
        print("WebSandUniTest test")