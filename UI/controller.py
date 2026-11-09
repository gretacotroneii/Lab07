import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None


    # POPOLA DROPDOWN
    def popola_dropdown(self):
        #popola il dropdown delle biblioteche e aggiunge prima l'opzione 'Nessun filtro'
        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option(key='Nessun filtro',text='Nessun filtro')
        )
        biblioteche=self._model.get_biblioteche()
        for b in biblioteche:
            #per assicurarsi che l'oggetto b abbia id e nome
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(key=str(b.id),text=b.nome)
            )

        # popola il dropdown dei generi e aggiunge prima l'opzione 'Nessun filtro'
        self._view.dd_genere.options.append(
            ft.dropdown.Option(key='Nessun filtro',text='Nessun filtro')
        )
        generi=self._model.get_generi()
        for genere in generi:
            self._view.dd_genere.options.append(
                ft.dropdown.Option(key=genere,text=genere)
            )
        self._view.update()

    # CALLBACKS DROPDOWN
    def read_biblioteca(self, e):
        #Callback eseguita quando l'utente cambia la biblioteca nel menu a tendina.
        if e.control.value == "Nessun filtro" or not e.control.value:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = e.control.value

    def read_genere(self, e):
        """Callback eseguita quando l'utente cambia il genere nel menu a tendina."""
        if e.control.value == "Nessun filtro" or not e.control.value:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        #Gestisce il click sul pulsante 'Mostra Libri' per filtrare e stampare i risultati.

        # Chiamiamo il Model passando i parametri salvati dai dropdown
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # Puliamo la ListView dei risultati precedenti
        self._view.lst_risultati.controls.clear()

        # Controlliamo se la ricerca ha prodotto risultati
        if not libri:
            self._view.lst_risultati.controls.append(
                ft.Text("Nessun libro trovato con i filtri selezionati.", color="red")
            )
        else:
            # Mostriamo il conteggio dei libri trovati
            self._view.lst_risultati.controls.append(
                ft.Text(f"Trovati {len(libri)} libri:")
            )
            # Aggiungiamo ogni libro alla ListView
            for libro in libri:
                self._view.lst_risultati.controls.append(
                    ft.Text(f"- {libro.titolo} ({libro.autore}) | Genere: {libro.genere}")
                )

        # Aggiorniamo la pagina per rendere visibili i cambiamenti
        self._view.update()
