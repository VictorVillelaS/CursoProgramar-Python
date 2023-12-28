import pyodbc
from io import StringIO
from PreferenciasVO import PreferenciasVO
from FamiliaresVO import FamiliaresVO




class DataBank:
    _connection = None
    _pathBD = None

    def __init__(self, pathBD=None):
        if pathBD is not None:
            DataBank._pathBD = pathBD
        else:
            DBstring = StringIO()
            DBstring.write(r"DRIVER={Microsoft Access Driver ( *.mdb, *.accdb)};")
            DBstring.write(r"DBQ = C:.\ExercicioAccess_20231012.accdb;")

            DataBank._pathBD = DBstring.getvalue()

        DataBank.getConexao()

    @staticmethod
    def getConexao():
        if DataBank._connection is None:
            DataBank.setConexao()

        return DataBank._connection

    @staticmethod
    def setConexao():
        """connectionString = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:.\ExercicioAccess_20231012.accdb;'
        )"""
        with (open("config.ini", "r") as arquivo):
            connectionString = StringIO()
            connectionString.write(arquivo.readline())
            connectionString.write(arquivo.readline())

            connectionString = connectionString.getvalue()

        objConexao = pyodbc.connect(connectionString)
        DataBank._connection = objConexao

    @property
    def connection(self):
        return DataBank.getConexao()


class PreferenciasDAL(DataBank):
    def __init__(self):
        super().__init__()
    
    def ImportarBDConectado(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM ')
            strSQL.write('Preferencias3')

            objLeitorBD.execute(strSQL.getvalue())

            dados = []
            record = objLeitorBD.fetchone()

            while record is not None:
                dados.append(record)
                record = objLeitorBD.fetchone()

            objLeitorBD.close()
            return dados

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

    def ImportarBDDesconectado(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()
            strSQL = StringIO()
            strSQL.write('SELECT')
            strSQL.write(' ID')
            strSQL.write(',Descricao')
            strSQL.write(' FROM Preferencias3')
            objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()

            lstPreferenciasVOCollection = []
            for dado in record:
                objPreferenciasVO = PreferenciasVO(dado[0], dado[1])
                lstPreferenciasVOCollection.append(objPreferenciasVO)

            return lstPreferenciasVOCollection

        except Exception as e:
            raise Exception(f'Problemas na consulta da tabela Preferencias: {e.args}')

        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def AdicionarEntradaBD(self, parPreferenciasVO):
        try:
            objPreferenciasVO = parPreferenciasVO
            if objPreferenciasVO.descricao is not None or "":
                objConexao = self.connection
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write('INSERT INTO Preferencias3 (')
                strSQL.write(' Descricao')
                strSQL.write(') VALUES (')
                strSQL.write(' ?')
                strSQL.write(')')

                # strSQL = "INSERT INTO Preferencias3 ( Descricao ) VALUES (?)"
                objLeitorBD.execute(strSQL.getvalue(), objPreferenciasVO.descricao)
                objLeitorBD.commit()
            else:
                return
        except Exception as e:
            raise Exception(f"Problemas ao adicionar linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
    def EditarEntradaBD(self, parPreferenciasVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Preferencias3 SET")
            strSQL.write(" Descricao = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Preferencias3 SET Descricao = (?) WHERE ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (parPreferenciasVO.descricao, parPreferenciasVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Problemas ao editar entrada em propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def RemoverEntradaBD(self, parPreferenciasVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Preferencias3")
            strSQL.write(" WHERE ID = ?")
            # strSQL = "DELETE FROM Preferencias3 Where ID = (?)"

            objLeitorBD.execute(strSQL.getvalue(), parPreferenciasVO.id)
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Problemas ao remover linha em Propriedades: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass


class FamiliaresDAL(DataBank):
    def __init__(self):
        super().__init__()

    def importarBDFamiliaresDesconectado(self):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Favorito")
            strSQL.write(" FROM Familiares")

            # strSQL = "SELECT * FROM Familiares"
            objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()

            dados = []
            for dado in record:
                objFamiliaresVO = FamiliaresVO(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5])
                dados.append(objFamiliaresVO)
            return dados

        except Exception as e:
            raise Exception(f"Erro ao consultar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def consultarBDFamiliares(self, ID=None):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID")
            strSQL.write(",Nome")
            strSQL.write(",Sexo")
            strSQL.write(",Idade")
            strSQL.write(",Salario")
            strSQL.write(",Favorito")
            strSQL.write(" FROM Familiares")

            if ID is not None:
                strSQL.write(" WHERE ID = ?")
                objLeitorBD.execute(strSQL.getvalue(), (ID,))
            else:
                objLeitorBD.execute(strSQL.getvalue())

            record = objLeitorBD.fetchall()
        except Exception as e:
            raise Exception(f"Erro aou consultar Familiares: {e}")
        else:
            if record:
                record = record[0]
                objFamiliaresVO = FamiliaresVO(record[0], record[1], record[2], record[3], record[4], record[5])
                return objFamiliaresVO
            else:
                return None
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def adicionarEntrada(self, parFamiliaresVO):
        try:
            if parFamiliaresVO is not None or "":
                objConexao = self.connection
                objLeitorBD = objConexao.cursor()

                strSQL = StringIO()
                strSQL.write("INSERT INTO Familiares (")
                strSQL.write(" Nome")
                strSQL.write(",Sexo")
                strSQL.write(",Idade")
                strSQL.write(",Salario")
                strSQL.write(",Favorito")
                strSQL.write(") VALUES (")
                strSQL.write(" ?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(",?")
                strSQL.write(")")
                # strSQL = "INSERT INTO Familiares (Nome, Sexo, Idade, Salario, Favorito) VALUES (?, ?, ?, ?, ?)"

                objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.nome,
                                                        parFamiliaresVO.sexo,
                                                        parFamiliaresVO.idade,
                                                        parFamiliaresVO.salario,
                                                        parFamiliaresVO.favorito)
                                    )
                objLeitorBD.commit()
            else:
                return
        except Exception as e:
            raise Exception(f"Erro ao adicionar parente: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def editarEntrada(self, parFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE Familiares SET")
            strSQL.write(" Nome = ?")
            strSQL.write(",Sexo = ?")
            strSQL.write(",Idade = ?")
            strSQL.write(",Salario = ?")
            strSQL.write(",Favorito = ?")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "UPDATE Familiares SET Nome = ?, Sexo = ?,Idade = ?,Salario = ?,Favorito = ? WHERE ID = ? "

            objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.nome,
                                                            parFamiliaresVO.sexo,
                                                            parFamiliaresVO.idade,
                                                            parFamiliaresVO.salario,
                                                            parFamiliaresVO.favorito,
                                                            parFamiliaresVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao editar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass

    def removerEntrada(self, parFamiliaresVO):
        try:
            objConexao = self.connection
            objLeitorBD = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE FROM Familiares")
            strSQL.write(" WHERE ID = ?")

            # strSQL = "DELETE FROM Familiares Where ID = (?)"
            objLeitorBD.execute(strSQL.getvalue(), (parFamiliaresVO.id))
            objLeitorBD.commit()
        except Exception as e:
            raise Exception(f"Erro ao deletar Familiares: {e}")
        finally:
            try:
                objLeitorBD.close()
            except:
                pass
