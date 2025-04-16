import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def test__init__(self):
        TV = Television()
        self.assertFalse(TV.status)
        self.assertFalse(TV.muted)
        self.assertAlmostEqual(0, TV.volume)
        self.assertAlmostEqual(0, TV.channel)
        self.assertAlmostEqual(0, Tv.Channel)

    def test_power(self):
        TV = Television()
        TV.power()
        self.assertTrue(TV.status)
        TV.power()
        self.assertFalse(TV.status)

    def test_mute(self):
        TV = Television(True)
        TV.volume = 1
        TV.mute()
        self.assertTrue(TV.muted)
        self.assertEqual(TV.volume, 0)
        TV.mute()
        self.assertFalse(TV.muted)
        self.assertEqual(TV.volume, 2)

    def test_channel_up(self):
        TV = Television(True)
        TV.channel = Television.MAX_CHANNEL
        TV.channel_up()
        self.assertEqual(TV.channel, Television.MIN_CHANNEL)
        TV.channel_up()
        self.assertEqual(TV.channel, Television.MIN_CHANNEL + 1)

    def test_channel_down(self):
        TV = Television(True)
        TV.channel = Television.MIN_CHANNEL
        TV.channel_down()
        self.assertEqual(TV.channel, Television.MAX_CHANNEL)
        TV.channel_down()
        self.assertEqual(TV.channel, Television.MAX_CHANNEL - 1)

    def test_volume_up(self):
        TV = Television(True)
        TV.volume = Television.MAX_VOLUME - 1
        TV.volume_up()
        self.assertEqual(TV.volume, Television.MAX_VOLUME)
        TV.volume_up()
        self.assertEqual(TV.volume, Television.MAX_VOLUME)

    def test_volume_down(self):
        TV = Television(True)
        TV.volume = Television.MIN_VOLUME + 1
        TV.volume_down()
        self.assertEqual(TV.volume, Television.MIN_VOLUME)
        TV.volume_down()
        self.assertEqual(TV.volume, Television.MIN_VOLUME)

    def test_volume_change_while_muted(self):
        TV = Television(True)
        TV.volume = 1
        TV.mute()
        TV.volume_up()
        TV.volume_down()
        TV.mute()
        self.assertEqual(TV.volume, 2)


if __name__ == '__main__':
    unittest.main()
