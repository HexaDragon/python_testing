"""car module to produce car objects"""


class Car(object):
    """class Car containing methods"""

    discount = float(50/100)       # declaring the discount as global member

    def __init__(self, model_name, make, color, final_price):
        self.model_name = model_name
        self.make = make
        self.color = color
        self.final_price = final_price

    @property
    def make_model_statement(self):
        return '{} of {} is the best car ever made'.format(self.model_name, self.make)

    @property
    def model_color_available(self):
        return '{} is available in {} color'.format(self.model_name, self.color)

    def apply_discount(self):
        self.final_price = int(self.final_price * self.discount)

