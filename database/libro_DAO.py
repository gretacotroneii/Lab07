from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self, id_biblioteca=None,genere=None):
        #recupero i libri dal database e applico in modo opzionale i filtri di biblioteca e genere tramite COALESCE

        cnx=DBConnect.get_connection()
        result=[]

        if cnx is not None:
            print('Connection to database established (LibroDAO')

            query='''
                SELECT id,titolo,autore,genere,anno_pubblicazione,id_biblioteca
                FROM libro
                WHERE (id_biblioteca=COALESCE(%s,id_biblioteca))
                AND (genere=COALESCE(%s,genere))
                '''

            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query,(id_biblioteca,genere))

            for row in cursor:
                libro=Libro(
                    id=row['id'],
                    titolo=row['titolo'],
                    autore=row['autore'],
                    genere=row['genere'],
                    anno_pubblicazione=row['anno_pubblicazione'],
                    id_biblioteca=row['id_biblioteca']
                )
                result.append(libro)

            cursor.close()
            cnx.close()

        return result

