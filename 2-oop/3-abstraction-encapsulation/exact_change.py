class Denomination:
    def __init(self, value, singular, plural):
        self.value = value
        self.singular = singular
        self.plural = plural

QUARTER = Denomination(.25, 'Quarter', 'Quarters')
PENNY = Denomination(.01, 'Penny', 'Pennies')

class Amount:
    def __init(self, amount, demonination):
        self._amount = amount
        self.denomination = demonination

    @property
    def get_amount(self):
        if self._amount == 1:
            return f"{self._amount} {self.denomination.singular}"
        else:
            return f"{self._amount} {self.denomination.plural}"

five_bucks = Amount(5, QUARTER)
five_bucks.get_amount
