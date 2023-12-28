from DAL import PreferenciasDAL, FamiliaresDAL
# BLL = Business Logical Layer

class Preferencias:
    def __init__(self):
        pass
    
    def ListboxWhile():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            lista = []
            id = 0
            preferencia = arquivo.readline()
            while preferencia != '':
                id += 1
                lista.append([id, preferencia])
                preferencia = arquivo.readline()
            arquivo.close()
        return lista
    
    def ListboxForComIndice():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            preferencias = arquivo.readlines()
        arquivo.close()
        preferencias = [[i+1, preferencias[i]] for i in range(len(preferencias))]
        return preferencias
        
    def ListboxForSemIndice():
        with open('C:\Curso Programar\python\preferencias.txt') as arquivo:
            preferencias = arquivo.readlines()
        arquivo.close()
        preferencias = [[i+1, preferencias[i]] for i in range(len(preferencias))]
        return preferencias

    def ImportarBDConectado():
        try:
            return PreferenciasDAL().ImportarBDConectado()
        except Exception as e:
            raise e

    def ImportarBDDesconectado():
        try:
            return PreferenciasDAL().ImportarBDDesconectado()
        except Exception as e:
            raise e

    def AdicionarEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().AdicionarEntradaBD(parPreferenciasVO)
        except Exception as e:
            raise(e)

    def EditarEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().EditarEntradaBD(parPreferenciasVO)
        except Exception as e:
            raise(e)

    def RemoverEntradaBD(parPreferenciasVO):
        try:
            return PreferenciasDAL().RemoverEntradaBD(parPreferenciasVO)
        except Exception as e:
            raise e


class Familiares:
    def __init__(self):
        pass

    def importarBDFamiliares(self):
        try:
            return FamiliaresDAL().importarBDFamiliaresDesconectado()
        except Exception as e:
            raise e

    def consultarBDFamiliares(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().consultarBDFamiliares(parFamiliaresVO)
        except Exception as e:
            raise e

    def adicionarFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().adicionarEntrada(parFamiliaresVO)
        except Exception as e:
            raise e

    def editarFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().editarEntrada(parFamiliaresVO)
        except Exception as e:
            raise e

    def removerFamiliar(self, parFamiliaresVO):
        try:
            return FamiliaresDAL().removerEntrada(parFamiliaresVO)
        except Exception as e:
            raise e


