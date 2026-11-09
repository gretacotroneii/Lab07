from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    #funzione che recupera tutte le biblioteche presenti nel database
    def get_all_biblioteche(self):
        cnx=DBConnect.get_connection()
        result=[]

        if cnx is not None:
            print('Connection to database established (bibliotecaDAO)')

            query='SELECT id,nome,indirizzo FROM biblioteca'

            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query)

            for row in cursor:
                biblioteca = Biblioteca(
                    id=row['id'],
                    nome=row['nome'],
                    indirizzo=row['indirizzo']
                )
                result.append(biblioteca)

            cursor.close()
            cnx.close()

        return result

