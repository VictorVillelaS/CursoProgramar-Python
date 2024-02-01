from DAL.preferenciasDeFamiliaresDAL import PreferenciasDeFamiliaresDAL


class PreferenciasDeFamiliares:
    def __init__(self):
        pass

    def importPreferenciasFamiliares(self):
        try:
            return PreferenciasDeFamiliaresDAL().consultarBD()
        except Exception as e:
            raise e

    def adicionarPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            PreferenciasDeFamiliaresDAL().incluirBD(objPreferenciaFamiliar)
        except Exception as e:
            raise e

    def editarPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            PreferenciasDeFamiliaresDAL().editarBD(objPreferenciaFamiliar)
        except Exception as e:
            raise e

    def removerPreferenciaFamiliar(self, objPreferenciaFamiliar):
        try:
            PreferenciasDeFamiliaresDAL().excluirBD(objPreferenciaFamiliar)
        except Exception as e:
            raise e