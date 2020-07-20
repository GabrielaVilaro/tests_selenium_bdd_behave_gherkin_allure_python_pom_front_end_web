import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # BROWSER DE PRUEBAS
    BROWSER = u'CHROME'

    Environment = 'Test'

    if Environment == 'Test':
        URL = 'https://www.phptravels.net/home'