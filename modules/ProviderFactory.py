class ProviderFactory:
    def ProviderModule(self, ProviderName):
        try:
            return __import__("libcloud.%s.providers" % ProviderName, fromlist=["libcloud"])
        except ImportError as ex:
            print("Error")

    def ProviderDriver(self, ProviderName):
        return self.ProviderModule(ProviderName).get_driver