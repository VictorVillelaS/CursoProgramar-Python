from DAL import Dados
#BLL = Business Logical Layer

class Preferencias():
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
            return Dados.ImportarBDConectado()
        except Exception as e:
            raise e

    def ImportarBDDesconectado():
        try:
            return Dados.ImportarBDDesconectado()
        except Exception as e:
            raise(e)

    def AdicionarEntradaBD(dados):
        try:
            return Dados.AdicionarEntradaBD(dados)
        except Exception as e:
            raise(e)

    def EditarEntradaBD(dadoEditar, dadoValorNovo):
        try:
            return Dados.EditarEntradaBD(dadoEditar, dadoValorNovo)
        except Exception as e:
            raise(e)

    def RemoverEntradaBD(dadoRemover):
        try:
            return Dados.RemoverEntradaBD(dadoRemover)
        except Exception as e:
            raise e


class Familiares():
    def __init__(self):
        pass

    def importarBDFamiliares(self):
        try:
            return Dados.ImportarBDFamiliaresDesconectado()
        except Exception as e:
            raise e

    def consultarBDFamiliares(self, _id):
        try:
            return Dados.ConsultarBDFamiliares(_id)
        except Exception as e:
            raise e

    def adicionarFamiliar(self, nome, sexo, idade, salario, favorito):
        try:
            return Dados.AdicionarEntradaBDFamiliares([nome, sexo, idade, salario, favorito])
        except Exception as e:
            raise e

    def editarFamiliar(self, id, nome, sexo, idade, salario, favorito):
        try:
            return Dados.EditarEntradaBDFamiliares([nome, sexo, idade, salario, favorito, id])
        except Exception as e:
            raise e

    def removerFamiliar(self, id):
        try:
            return Dados.RemoverEntradaBDFamiliares(id)
        except Exception as e:
            raise e


