import pytest
from international_trade_models import country, ricardian


@pytest.fixture
def ricardian_model():
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
    model = ricardian.Ricardian2C2G("wine", "cloth", "labor", country_a, country_b)
    return model


def test_set_factor(ricardian_model):
    ricardian_model.set_factor("capital")
    assert ricardian_model.input == "capital"
    ricardian_model.set_factor("labor")
    assert ricardian_model.input == "labor"


def test_set_goods(ricardian_model):
    ricardian_model.set_good_a("microprocessors")
    ricardian_model.set_good_b("wine")
    assert ricardian_model.a == "microprocessors"
    assert ricardian_model.b == "wine"
    ricardian_model.set_good_a("wine")
    ricardian_model.set_good_b("cloth")
    assert ricardian_model.a == "wine"
    assert ricardian_model.b == "cloth"


def test_ufr_grid(ricardian_model):
    assert ricardian_model.ufr_grid() == [[3, 2], [1, 1]]
    ricardian_model.set_good_a("microprocessors")
    assert ricardian_model.ufr_grid() == [[2, 2], [4, 1]]
    ricardian_model.set_good_a("wine")


def test_equal_autarky(ricardian_model):
    assert ricardian_model.equal_autarky() == {"USA": 100, "UK": 350}
    ricardian_model.set_good_a("microprocessors")
    assert ricardian_model.equal_autarky() == {"USA": 125, "UK": 140}
    ricardian_model.set_good_a("wine")


def test_full_specialization(ricardian_model):
    assert ricardian_model.full_specialization() == {"USA": ("cloth", 250), "UK": ("wine", 700)}
    ricardian_model.set_good_a("microprocessors")
    assert ricardian_model.full_specialization() == {"USA": ("microprocessors", 250), "UK": ("cloth", 700)}
    ricardian_model.set_good_a("wine")
