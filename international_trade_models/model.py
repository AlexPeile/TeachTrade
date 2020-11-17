import country
import ricardian
from matplotlib import pyplot as plt

class Model():
    """
        A 2 country, 2 good model, from which a number of neoclassical and new international
        trade models can be derived
    """
    def __init__(self, country_a, country_b):
        """
            Initialize instance variables.
            :param country_a (Country): the 'home' country in the model
            :param country_b (Country): the 'foreign' country in the model
            :return None:
        """
        self.home = country_a
        self.foreign = country_b

    def ricardo(self, good_a, good_b, input):
        """
            Sets the model to a 2 good Ricardian trade model
            :param good_a (str): the first trade good of the model
            :param good_b (str): the second trade good of the model
            :return None:
        """
        self.model = ricardian.Ricardian2C2G(good_a, good_b, input, self.home, self.foreign)


