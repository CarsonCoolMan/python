class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status: bool = False, muted: bool = False, volume: float = MIN_VOLUME, channel: float = MIN_CHANNEL):
        """
        :param status: on or off
        :param muted: muted or unmuted
        :param volume: max of 3 min of 0
        :param channel: max of 3 min of 0
        :param prev_volume: used to save previous volume when muted
        """
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel
        self.prev_volume = volume

    def power(self):
        """
        :param status: this turns the TV on or off
        the code will not run unless status is true
        """
        if self.status == True:
            self.status = False
        else:
            self.status = True
    def mute(self):
        """
        the code will not run unless status is true
        :param prev_volume: saves the previous volume so
        that when you unmute it has the original volume
        """
        if self.status == True:
            if self.muted == True:
                self.muted = False
            else:
                self.prev_volume = self.volume
                self.volume = Television.MIN_VOLUME
                self.muted = True


    def channel_up(self):
        """
        the code will not run unless status is true
        if the channel is at the MAX channel it goes to min Channel
        """
        if self.status:
            if self.channel + 1 > Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel = self.channel + 1

    def channel_down(self):
        """
        the code will not run unless status is true
        if the channel is at the MIN channel it goes to max Channel
        """
        if self.status:
            if self.channel - 1 < Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel = self.channel - 1

    def volume_up(self):
        """
        the code will not run unless status is true
        if the volume is the max volume it just passes
        if not than it increases the volume by 1
        """

        if self.status:
            if self.muted == True:
                self.muted = False
                self.volume = self.prev_volume
                print(self.volume)
            if self.volume + 1 > Television.MAX_VOLUME:
                pass
            else:
                self.volume = self.volume + 1

    def volume_down(self):
        """
        the code will not run unless status is true
        if the volume is the min volume it just passes
        if not than it decreases the volume by 1
        """
        if self.status:
            if self.muted == True:
                self.muted = False
                self.volume = self.prev_volume
                print(self.volume)
            if self.volume - 1 < Television.MIN_VOLUME:
                pass
            else:
                self.volume = self.volume - 1

    def __str__(self):
        """
        :return: the status channel and volume currently
        """
        return f"Power=[{self.status}], Channel=[{self.channel}], Volume=[{self.volume}]"

