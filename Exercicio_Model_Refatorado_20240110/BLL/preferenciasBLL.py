from DAL.preferenciasDAL import PreferenciasDAL


class Preferencias:
    def __init__(self):
        pass

    def ImportarBDDesconectado():
        try:
            return PreferenciasDAL().consultarBD()
        except Exception as e:
            raise e

    def AdicionarEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().incluirBD(parPreferenciasVO)
        except Exception as e:
            raise (e)

    def EditarEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().editarBD(parPreferenciasVO)
        except Exception as e:
            raise (e)

    def RemoverEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().excluirBD(parPreferenciasVO)
        except Exception as e:
            raise e