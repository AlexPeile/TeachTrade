class Country():
    """
           A model for a country
    """
    def __init__(self, name, factor_endowments, technologies) :
        """
            Initialize instance variables.
            :param factor_endowments (dict): country's factor endowments
            :param technologies (dict): country's unit labor requirements for trade goods
            :return None:
        """
        self.name = name
        self.factor_endowments = factor_endowments
        self.technologies = technologies