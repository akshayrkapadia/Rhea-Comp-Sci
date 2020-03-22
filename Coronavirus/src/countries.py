class Earth(object):
    """
    Class that represents the Earth.

    Args:
        population (int),
        countries (Country[])
    """

    def __init__(self, population, countries):
        super(Earth, self).__init__()
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

    # TODO: Return the country with the most active cases
    def getMostInfectedCountry():
        pass


class Country(object):
    """
    Class that represents a coutry.

    Args:
        name (string),
        population (int)
    """

    # TODO: Initialize class variables
    def __init__(self, name, population):
        super(Country, self).__init__()
        pass


class InfectedCountry(Country):
    """
    Class that represents an infected country.

    Args:
        name (string),
        population (int),
        cases (int),
        recovered (int),
        deaths (int),
        activeCases (int)
    """

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
