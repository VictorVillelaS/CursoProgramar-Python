from DAL.familiaresDAL import FamiliaresDAL


class FamiliaresBLL:
    def __init__(self):
        pass

    def importarBDFamiliares(self):
        try:
            return FamiliaresDAL().importarBD()
        except Exception as e:
            raise e

    def consultarBDFamiliares(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().consultarBD(parFamiliaresVO)
        except Exception as e:
            raise e

    def adicionarFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().incluirBD(parFamiliaresVO)
        except Exception as e:
            raise e

    def editarFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().editarBD(parFamiliaresVO)
        except Exception as e:
            raise e

    def removerFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().excluirBD(parFamiliaresVO)
        except Exception as e:
            raise e