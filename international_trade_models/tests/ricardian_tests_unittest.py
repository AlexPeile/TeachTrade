import unittest
from international_trade_models import country, ricardian


class test_ricardian(unittest.TestCase):
    def setUp(self):
        USA_factors = {"labor": 500,
                       "capital": 1000}
        UK_factors = {"labor": 700,
                      "capital": 200}
        USA_tech = {"wine": 3,
                    "cloth": 2,
                    "microprocessors": 2}
        UK_tech = {"wine": 1,
                   "cloth": 1,
                   "microprocessors": 4}
        country_a = country.Country("USA", USA_factors, USA_tech)
        country_b = country.Country("UK", UK_factors, UK_tech)
        self.model = ricardian.Ricardian2C2G("wine", "cloth", "labor", country_a, country_b)

    def test_set_factor(self):
        self.model.set_factor("capital")
        self.assertEqual(self.model.input, "capital")
        self.model.set_factor("labor")
        self.assertEqual(self.model.input, "labor")

    def test_set_goods(self):
        self.model.set_good_a("microprocessors")
        self.model.set_good_b("wine")
        self.assertEqual(self.model.a, "microprocessors")
        self.assertEqual(self.model.b, "wine")
        self.model.set_good_a("wine")
        self.model.set_good_b("cloth")
        self.assertEqual(self.model.a, "wine")
        self.assertEqual(self.model.b, "cloth")

    def test_ufr_grid(self):
        self.assertEqual(self.model.ufr_grid(), [[3,2],[1,1]])
        self.model.set_good_a("microprocessors")
        self.assertEqual(self.model.ufr_grid(), [[2, 2], [4, 1]])
        self.model.set_good_a("wine")


    def test_equal_autarky(self):
        self.assertEqual(self.model.equal_autarky(), {"USA": 100, "UK": 350})
        self.model.set_good_a("microprocessors")
        self.assertEqual(self.model.equal_autarky(), {"USA": 125, "UK": 140})
        self.model.set_good_a("wine")

    def test_full_specialization(self):
        self.assertEqual(self.model.full_specialization(), {"USA": ("cloth", 250), "UK": ("wine", 700)})
        self.model.set_good_a("microprocessors")
        self.assertEqual(self.model.full_specialization(), {"USA": ("microprocessors", 250), "UK": ("cloth", 700)})
        self.model.set_good_a("wine")



if __name__ == '__main__':
    unittest.main()
