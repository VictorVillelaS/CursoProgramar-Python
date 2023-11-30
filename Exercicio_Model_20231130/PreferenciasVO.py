class PreferenciasVO:
    def __init__(self):
        pass

    def __init__(self, iD, descricao):
        self._id = iD
        self._descricao = descricao

    def getId(self):
        return self.iD

    def setId(self, iD):
        self._id = iD

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao

    _id = property(getId, setId)
    _descricao = property(getDescricao, setDescricao)

    idCollection = [PreferenciasVO()]