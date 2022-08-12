class Television:
    """

    """
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self):
        """"

        """
        self.__tv_channel = self.MIN_CHANNEL
        self.__tv_volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        """

        :return:
        """
        if self.__status:
            self.__status = False

        else:
            self.__status = True

    def channel_up(self):
        """

        :return:
        """
        if self.__status:
            self.__tv_channel = (self.__tv_channel + 1) % self.MAX_CHANNEL

    def channel_down(self):
        """

        :return:
        """
        if self.__status:
            self.__tv_channel = abs((self.__tv_channel - 1) % self.MAX_CHANNEL)

    def volume_up(self):
        """

        :return:
        """
        if self.__status:
            if self.__tv_volume < self.MAX_VOLUME:
                self.__tv_volume += 1

    def volume_down(self):
        """

        :return:
        """
        if self.__status:
            if self.__tv_volume > self.MIN_VOLUME:
                self.__tv_volume -= 1

    def __str__(self):
        """

        :return:
        """
        return f"TV status: Is on = {self.__status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}"