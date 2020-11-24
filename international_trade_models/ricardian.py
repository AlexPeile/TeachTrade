from international_trade_models import country
import matplotlib
matplotlib.rcParams['text.usetex'] = True
from matplotlib import pyplot as plt



class Ricardian2C2G():
    """
    A 2 country, 2 good, single input Ricardian trade model
    Assumptions:
    - consumers have identical, homothetic preferences
    - labor perfectly mobile across sectors
    """
    def __init__(self, good_a, good_b, input, home, foreign):
        """Initialize instance variables

        :param good_a: the first trade good of the model
        :type good_a: str
        :param good_b: the second trade good of the model
        :type good_b: str
        :param input: the single factor of production
        :type input: str
        :param home: the home country for the model
        :type home: country.Country
        :param foreign: the foreign country for the model
        :type foreign: country.Country
        :return None:
        """
        self.a = good_a
        self.b = good_b
        self.input = input
        self.home = home
        self.foreign = foreign

    def set_factor(self, factor):
        """Set the model's single factor of production

        :param factor: the new factor to use
        :type factor: str
        """
        self.input = factor

    def set_good_a(self, good_a):
        """Set the model's first good

        :param good_a: the new good to use
        :type good_a: str
        """
        self.a = good_a

    def set_good_b(self, good_b):
        """Set the model's second good

        :param good_b: the new good to use
        :type good_b: str
        """
        self.b = good_b

    def ufr_grid(self):
        """Generate a 2D list of unit factor requirements

        :return grid: a pyplot table of unit factor requirements
        :type grid: 2D list
        """
        ufr_home_a = self.home.technologies[self.a]
        ufr_home_b = self.home.technologies[self.b]
        ufr_foreign_a = self.foreign.technologies[self.a]
        ufr_foreign_b = self.foreign.technologies[self.b]

        grid = [[ufr_home_a, ufr_home_b], [ufr_foreign_a, ufr_foreign_b]]

        return grid

    def equal_autarky(self):
        """Generate a possible state of autarky for each country, assuming equal production of both goods

        :return autarky: dict of autarky amounts for each country, keyed on country names
        :type autarky: dict
        """
        grid = self.ufr_grid()
        autarky = {}

        ufr_home = grid[0]
        ufr_foreign = grid[1]
        factor_home = self.home.factor_endowments[self.input]
        factor_foreign = self.foreign.factor_endowments[self.input]

        autarky[self.home.name] = factor_home / sum(ufr_home)
        autarky[self.foreign.name] = factor_foreign / sum(ufr_foreign)

        return autarky

    def full_specialization(self):
        """Finds the good each country has comparitive advantage in, and the amount they produce at full specialization

        :return specialization: dict of (good, amount) duples, keyed on country names
        :type specialization: dict
        """
        grid = self.ufr_grid()
        specialization = {}

        opcost_a_home = grid[0][0] / grid[0][1]
        opcost_a_foreign = grid[1][0] / grid[1][1]

        if opcost_a_home <= opcost_a_foreign:
            specialization[self.home.name] = (self.a, self.home.factor_endowments[self.input] / grid[0][0])
            specialization[self.foreign.name] = (self.b, self.foreign.factor_endowments[self.input] / grid[1][1])
        else:
            specialization[self.home.name] = (self.b, self.home.factor_endowments[self.input] / grid[0][1])
            specialization[self.foreign.name] = (self.a, self.foreign.factor_endowments[self.input] / grid[1][0])

        return specialization

    def ppf(self, filename = 'ppfs'):
        """Visualizes the Ricardian, 1 input-2 good production possibilities frontier

        :param filename: (optional) name of image to create
        :type filename: str"""

        factor_home = self.home.factor_endowments[self.input]
        factor_foreign = self.foreign.factor_endowments[self.input]
        grid = self.ufr_grid()

        x_home = [0, factor_home/grid[0][0]]
        y_home = [factor_home/grid[0][1], 0]
        x_for = [0, factor_foreign/grid[1][0]]
        y_for = [factor_foreign/grid[1][1], 0]

        fig, (hax, fax) = plt.subplots(2, 1)
        fig.tight_layout(h_pad=4)
        fig.suptitle(r"PRODUCTION POSSIBILITIES FRONTIERS \newline $Y_{%s} = \frac{%s}{a_{%s}} - \frac{a_{%s}}{a_{%s}} Y_{%s}$"
                  % (self.b, self.input, self.a, self.a, self.b, self.a))
        plt.subplots_adjust(left=0.125, top=0.85, bottom=0.1)

        hax.plot(x_home, y_home)
        hax.set(xlabel=self.a, ylabel=self.b,
               title=self.home.name)
        hax.grid()

        fax.plot(x_for, y_for)
        fax.set(xlabel=self.a, ylabel=self.b,
                title=self.foreign.name)
        fax.grid()

        fig.savefig(filename + ".png")
        plt.show()

    def rs_curve(self, filename='rs_curve'):
        """Visualizes the Ricardian world relative supply curve

        :param filename: (optional) name of image to create
        :type filename: str"""

        grid = self.ufr_grid()
        spec = self.full_specialization()
        x_fullspec = spec[self.home.name][1] / spec[self.foreign.name][1]

        x = [0, 0, x_fullspec, x_fullspec, 2*x_fullspec]
        if spec[self.home.name][0] == 'a':
            y = [0, grid[0][0]/grid[0][1], grid[0][0]/grid[0][1], grid[1][0]/grid[1][1], grid[1][0]/grid[1][1]]
        else:
            y = [0, grid[1][0] / grid[1][1], grid[1][0] / grid[1][1], grid[0][0] / grid[0][1], grid[0][0] / grid[0][1],]

        fig, ax = plt.subplots()
        fig.suptitle("WORLD RELATIVE SUPPLY CURVE")

        ax.plot(x, y)
        ax.set_xlabel(r"$\frac{Global\ %s\ Production}{Global\ %s\ Production}$" % (self.a, self.b), labelpad=5)
        ax.xaxis.set_label_coords(1, -0.055)
        ax.set_ylabel(r"$\frac{P_{%s}}{P_{%s}}$" % (self.a, self.b), rotation=0)
        ax.yaxis.set_label_coords(-0.025, 1.05)
        ax.grid()

        fig.savefig(filename + ".png")
        plt.show()