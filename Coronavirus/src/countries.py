class Country(object):
    """Class that represents a coutry."""

    # TODO: Initialize class variables
    def __init__(self, name, population):
        super(Country, self).__init__()
        pass


class InfectedCountry(Country):
    """Class that represents an infected country."""

    # TODO: Initialize class variables
    def __init__(self, name, population, cases, recovered, deaths, activeCases):
        super(InfectedCountry, self).__init__(name, population)
        pass

    # TODO: Return the percentage of cases resulting in deaths
    def getPercentDead():
        pass

    # TODO: Return the percentage of cases resulting in full recoveries
    def getPercentRecovered():
        pass

    # TODO: Return the percentage of people infected
    def getPercentInfected():
        pass

    # TODO: Return number of cases per 1 million people
    def getCasesPerMillion():
        pass
