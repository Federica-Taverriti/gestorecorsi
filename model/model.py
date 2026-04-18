from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwIscritti(self, pd):
        result = DAO.getCorsiPDwIscritti(pd)
        result.sort(key= lambda s: s[1], reverse=True) #lambda function per riordinare in ordine decrescente di iscritti, s[0] sarà il corso il secondo elemento sarà il numero di iscritti
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s:s.cognome) #ordinati per cognome
        return studenti

    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key = lambda c: c[1], reverse=True) #in ordine decrescente per numero di iscritti
        return cds
