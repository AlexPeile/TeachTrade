from international_trade_models import ricardian
from international_trade_models import country
# from matplotlib import pyplot as plt


class Model():
    """
    A 2 country, 2 good model, from which a number of neoclassical and
    new international trade models can be derived
    """
    def __init__(self, country_a, country_b):
        """Initialize instance variables.

        :param country_a: the 'home' country in the model
        :type country_a: country.Country
        :param country_b: the 'foreign' country in the model
        :type country_b: country.Country
        :return None:
        """
        self.home = country_a
        self.foreign = country_b

    def ricardo(self, good_a, good_b, input):
        """Sets the model to a 2 good Ricardian trade model

            :param good_a: the first trade good of the model
            :type good_a: str
            :param good_b: the second trade good of the model
            :type good_b: str
            :param input: the single factor of production
            :type input: str
            :return None:
        """
        self.model = ricardian.Ricardian2C2G(good_a, good_b, input, self.home, self.foreign)
