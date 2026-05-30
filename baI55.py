class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._c = 0.0
        self.celsius = celsius   # gọi setter để validate

    # getter celsius
    @property
    def celsius(self):
        return self._c

    # setter celsius (validate >= -273.15)
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._c = value

    # getter fahrenheit
    @property
    def fahrenheit(self):
        return self._c * 9 / 5 + 32

    # setter fahrenheit → convert rồi set celsius
    @fahrenheit.setter
    def fahrenheit(self, f):
        self.celsius = (f - 32) * 5 / 9