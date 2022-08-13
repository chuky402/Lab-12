class Television:
    """
    sets the max and min for channel and volume
    """
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self):
        """
        starting the remote
        """
        self.__tv_channel = self.MIN_CHANNEL
        self.__tv_volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        function to have the power button on the tv turn on or off.
        :return: Null
        """
        if self.__status:
            self.__status = False

        else:
            self.__status = True

    def channel_up(self):
        """
        funtion to change the channel by +1
        :return:
        """
        if self.__status:
            self.__tv_channel = (self.__tv_channel + 1) % self.MAX_CHANNEL

    def channel_down(self):
        """
        function to chnage the channel by -1
        :return:
        """
        if self.__status:
            self.__tv_channel = abs((self.__tv_channel - 1) % self.MAX_CHANNEL)

    def volume_up(self):
        """
        function to change the volume by +1
        :return:
        """
        if self.__status:
            if self.__tv_volume < self.MAX_VOLUME:
                self.__tv_volume += 1

    def volume_down(self):
        """
        function to change the volume by -1

        :return:
        """
        if self.__status:
            if self.__tv_volume > self.MIN_VOLUME:
                self.__tv_volume -= 1

    def _str__(self):
        """

        :return: return the status of the power channel and volume
        """
        return f"TV status: Is on = {self.__status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}"
