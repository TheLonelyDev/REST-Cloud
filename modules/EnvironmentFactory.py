class EnvironmentFactory:
    def Environment(self, ProviderDriver, EnvironmentName):
        return ProviderDriver(EnvironmentName)
