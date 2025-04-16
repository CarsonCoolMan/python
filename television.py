class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status: bool = False, muted: bool = False, volume: float = MIN_VOLUME, channel: float = MIN_CHANNEL):
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel

    def power(self, status: bool):
        """
        :param status: this turns the TV on or off
        """
        self.status = status

    def mute(self, muted: bool):
        self.muted = muted

    def channel_up(self):
        if self.status:
            if self.channel + 1 > Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel = self.channel + 1

    def channel_down(self):
        if self.status:
            if self.channel - 1 < Television.MIN_CHANNEL:
                self.channel = self.channel - 1
            else:
                self.channel = self.channel - 1

    def volume_up(self):
        self.muted = False
        if self.status:
            if self.volume + 1 > Television.MAX_VOLUME:
                pass
            else:
                self.volume = self.volume + 1

    def volume_down(self):
        self.muted = False
        if self.status:
            if self.volume - 1 < Television.MIN_VOLUME:
                pass
            else:
                self.volume = self.volume - 1

    def __str__(self):
        return f"Power=[{self.status}], Channel=[{self.channel}], Volume=[{self.volume}]"

