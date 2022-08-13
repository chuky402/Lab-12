import unittest


class MyTestCase(unittest.TestCase):
    import classes as tv

    def test_volume_down(self):
        self.tv.Television.volume_down(self)
        assert self.tv.Television._str__(self) == 'TV status: Is on = False, Channel = 0, Volume = 0'


if __name__ == '__main__':
    unittest.main()
