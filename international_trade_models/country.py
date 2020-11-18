class Country():
    """A model for a country
    """
    def __init__(self, name, factor_endowments, technologies):
        """Initialize instance variables.

        :param name: country name
        :type name: str
        :param factor_endowments: country's factor endowments
        :type factor_endowments: dict
        :param technologies: country's unit labor requirements for trade goods
        :type technologies: dict
        :return None:
        """
        self.name = name
        self.factor_endowments = factor_endowments
        self.technologies = technologies
