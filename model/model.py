from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        #gestione del filtro biblioteca
        if biblioteca=='Nessun filtro' or not biblioteca:
            biblioteca_param=None
        else:
            biblioteca_param=biblioteca

        #gestione del filtro genere
        if genere=='Nessun filtro' or not genere:
            genere_param=None
        else:
            genere_param=genere

        return self._libro_dao.get_libri(biblioteca_param, genere_param)


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        tutti_i_libri=self._libro_dao.get_libri(None,None)
        generi=[]
        for libro in tutti_i_libri:
            #controllo che il genere esista e non sia stato inserito nella lista
            if libro.genere and libro.genere not in generi:
                generi.append(libro.genere)
        return generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_all_biblioteche()

