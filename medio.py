class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos

    def reflejar(self, una_senal):
        """
        Los blancos en el medio reflejan la senal
        """        
        self.blancos.reflejar(una_senal)

        return una_senal
