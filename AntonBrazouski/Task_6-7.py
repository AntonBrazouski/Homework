class Money:



    def __init__(self, value, currency):
        self.exchange_rate = {
            "EUR": 0.93,
            "BYN": 2.1,
        }
        self.value = value
        self.currency = currency

    def __repr__(self):
        return f"{self.value}, {self.currency}"

    def __eq__(self, other):
        # simplified
        return (self.value == other.value
            and self.currency == other.currency)

    def __add__(self, other):
        # simplified
        if self.currency == other.currency:
            return Money(self.value + other.value, self.currency)



x = Money(10, "BYN")
y = Money(10, "BYN")
v = Money(11, "USD")
w = Money(11, "BYN")

print(x == y)
print(x == v)
print(x == w)

print(x+y)