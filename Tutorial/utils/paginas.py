from utils.singleton import Singleton


class Paginas(Singleton):
    """utilidades para distribuir registros por página"""
    def __init__(self):
        Singleton.__init__(self)

    def total_de_paginas(self, total_de_registros:int, registros_por_pagina:int) -> int:
        """total das páginas. 10 siginifica que a primeira página é 0 e a última 9."""
        if total_de_registros <= 0:
            return 0

        if total_de_registros % registros_por_pagina == 0:
            return (total_de_registros // registros_por_pagina)

        return (total_de_registros // registros_por_pagina) + 1

    def primeiro_registro_da_pagina(self, pagina:int, registros_por_pagina:int) -> int:
        """a primeira página é 0 (zero)"""
        if pagina < 0 or registros_por_pagina <= 0:
            return 0

        return pagina * registros_por_pagina

    def ultimo_registro_da_pagina(self, pagina:int, registros_por_pagina:int) -> int:
        """se a página é 2 e o registros_por_pagina é 10, então retorna 19"""
        if pagina < 0 or registros_por_pagina <= 0:
            return 0

        return self.primeiro_registro_da_pagina(pagina,registros_por_pagina) + registros_por_pagina - 1

