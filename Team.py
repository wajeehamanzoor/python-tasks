class Team:

    fee = 1000
    # Initializer / Instance Attributes
    def __init__(self, name, city, is_paid, num_players):
        self.name = name
        self.city = city
        self.is_paid = is_paid
        self.num_players = num_players

    # @property
    # def name(self):
    #     print("getter method called")
    #     return self._name
    #
    #     # a setter function
    #
    # @name.setter
    # def name(self, a):
    #     self._name = a
    #
    # @property
    # def city(self):
    #     return self.city
    #
    #     # a setter function
    #
    # @city.setter
    # def city(self, a):
    #     self._city = a
    #
    # @property
    # def isPaid(self):
    #     return self._isPaid
    #
    #     # a setter function
    #
    # @isPaid.setter
    # def isPaid(self, a):
    #     self._isPaid = a
    #
    # @property
    # def noOfPlayers(self):
    #     return self._noOfPlayers
    #
    #     # a setter function
    #
    # @noOfPlayers.setter
    # def noOfPlayers(self, a):
    #     self._noOfPlayers = a
    #
    #
