class Jar:
    """
    A class to represent a jar of cookies

    Attributes
    ----------
    capacity : int
        the jar capacity or the amount of cookies the jar can hold
    size : int
        the number of cookies currently in the jar
    """

    def __init__(self, capacity=12):
        """
        Init method to initialize a new jar of cookies

        :param capacity: The maximum jar capacity
        :type capacity: int
        :return: new Jar object
        :rtype: Jar object
        """
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        """
        String representation of the jar object

        :param self: The object itself
        :return: String representation of the number of cookies within the jar
        :rtype: str
        """
        return "🍪"*self.size

    @property
    def capacity(self):
        """
        Getter method to return the capacity of the jar
        :return: The maximum amount of cookies the jar can hold
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Setter method to set value for capacity
        :raise ValueError: If capacity not provided or its not an int or positive number
        """
        if not capacity or type(capacity) is not int or capacity < 1:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        """
        Getter method to return the size of the jar
        :return: The current amount of cookies in the jar
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Setter method to set value for size
        :raise ValueError: If the size is not integer and invalid
        """
        if type(size) is not int:
            raise ValueError("Invalid size")
        self._size = size

    def deposit(self, n):
        """
        Deposit new cookies into the jar

        :param n: number of new cookies to insert
        :type n: int
        :raise ValueError: If the inserting this amount of cookies will exceed the jar capacity
        """
        if self.size + n > self.capacity:
            raise ValueError(
                "You don't have enough room in the jar for those cookies")
        self.size += n

    def withdraw(self, n):
        """
        Withdraw cookies from the jar

        :param n: number of cookies to withdraw
        :type n: int
        :raise ValueError: If the withdrawing amount greater than the actual cookies in the jar
        """
        if n > self.size:
            raise ValueError("You don't have this amount of cookies")
        self.size -= n
