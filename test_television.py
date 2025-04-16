import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def test__init__(self):
        TV = Television()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")

    def test_power(self):
        TV = Television()
        TV.power()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[0]")
        TV.power()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")

    def test_mute(self):
        TV = Television(True)
        TV.volume_up()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[1]")
        TV.mute()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[0]")
        TV.mute()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[0]")
        TV.power()
        TV.mute()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")

    def test_channel_up(self):
        TV = Television()
        TV.channel_up()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")
        TV.power()
        TV.channel_up()
        self.assertEqual(str(TV), "Power=[True], Channel=[1], Volume=[0]")
        TV.channel = Television.MAX_CHANNEL
        TV.channel_up()
        self.assertEqual(str(TV), f"Power=[True], Channel=[0], Volume=[0]")

    def test_channel_down(self):
        TV = Television()
        TV.channel_down()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")
        TV.power()
        TV.channel = Television.MIN_CHANNEL
        TV.channel_down()
        self.assertEqual(str(TV), f"Power=[True], Channel=[3], Volume=[0]")

    def test_volume_up(self):
        TV = Television()
        TV.volume_up()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")

        TV.power()
        TV.volume_up()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[1]")

        TV.volume = Television.MAX_VOLUME
        TV.volume_up()
        self.assertEqual(str(TV), f"Power=[True], Channel=[0], Volume=[2]")
        TV.volume = 1
        TV.mute()
        TV.volume_up()
        TV.mute()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[0]")

    def test_volume_down(self):
        TV = Television()
        TV.volume_down()
        self.assertEqual(str(TV), "Power=[False], Channel=[0], Volume=[0]")
        TV.power()
        TV.volume = Television.MAX_VOLUME
        TV.volume_down()
        self.assertEqual(str(TV), f"Power=[True], Channel=[0], Volume=[1]")
        TV.volume = 1
        TV.mute()
        TV.volume_down()
        TV.mute()
        self.assertEqual(str(TV), "Power=[True], Channel=[0], Volume=[0]")

if __name__ == '__main__':
    unittest.main()
