
class PyBooru:
    """
    Main entry class for the PyBooru libary
    """

    def __init__(self, siteUrl="https://derpibooru.org", apiKey=""):
        self._siteUrl = siteUrl
        self._apiKey = apiKey
