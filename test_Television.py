import unittest


class MyTestCase(unittest.TestCase):
    import classes as tv
    def test_volume_down(self):
        self.test_volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'


if __name__ == '__main__':
    unittest.main()
