import pyodbc
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Ustaw szerokość okna na 80% szerokości ekranu
        # Window.size = (Window.width * 0.8, Window.height)        

        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 210
    

        self.top_grid = GridLayout(
             row_force_default = True,
             row_default_height = 60,
             col_force_default = True,
             col_default_width = 200
             )
        
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Data dodania:",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))        
        self.data = TextInput(multiline=False,
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200)

        self.top_grid.add_widget(self.data)

        self.top_grid.add_widget(Label(text="Kategoria: ",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))
        # Utwórz Spinner z opcjami i ustaw szerokość na szerokość najszerszego tekstu
        self.kategoria = Spinner(
            text='Wybierz kategorię',
            values=('LOZ', 'TAP'),
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
        )
        self.top_grid.add_widget(self.kategoria)

        self.top_grid.add_widget(Label(text="Model:",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))        
        self.model = TextInput(multiline=False,
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200)

        self.top_grid.add_widget(self.model)

        self.top_grid.add_widget(Label(text="Tkanina:",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))        
        self.tkanina = TextInput(multiline=False,
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200)

        self.top_grid.add_widget(self.tkanina)

        self.top_grid.add_widget(Label(text="Kategoria błędu: ",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))

        # Utwórz Spinner z opcjami i ustaw szerokość na szerokość najszerszego tekstu
        self.kat_bledu = Spinner(
            text='Wybierz kategorię',
            values=('BRAK KATEGORII', 'KASTONY', 'MONTAŻ', 'MONTAŻ/STOLARNIA', 'PIANKOWANIE', 'STOLARNIA', 'SZWALNIA', 'TAPICERNIA', 'TECHNOLOGICZNY', 'TO NIE JEST BŁĄD'),
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
        )
        self.top_grid.add_widget(self.kat_bledu)

        self.top_grid.add_widget(Label(text="Opis:",
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200))
        self.opis = TextInput(multiline=True,
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 200)
        self.top_grid.add_widget(self.opis)

        self.add_widget(self.top_grid)

        self.dodaj_blad = Button(text = "Dodaj", font_size = 16,
                    size_hint_y = None,
                    height = 50,
                    size_hint_x = None,
                    width = 400)
        self.dodaj_blad.bind(on_press = self.press)
        self.add_widget(self.dodaj_blad)  

    def press(self, instance):
        kat = self.kategoria.text
        model = self.model.text
        tkanina = self.tkanina.text
        kat_bledu = self.kat_bledu.text
        opis = self.opis.text

        try:
            # Ustal połączenie z bazą danych
            conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\mjozefowski\Desktop\Bledy_prod\Probna_baza.accdb;'
            conn = pyodbc.connect(conn_str)

            # Utwórz kursor do bazy danych
            cursor = conn.cursor()

            # Definiuj zapytanie SQL do dodania rekordu z użyciem zmiennych
            insert_query = "INSERT INTO Baza_bledy_prod (Kategoria, Model, Tkanina, Kategoria_bledu, Opis) VALUES (?, ?, ?, ?, ?)"

            # Wykonaj zapytanie SQL z parametrami
            cursor.execute(insert_query, (kat, model, tkanina, kat_bledu, opis))

            # Zatwierdź zmiany i zamknij połączenie
            conn.commit()
            conn.close()

            print("Rekord został dodany do bazy danych.")
        except Exception as e:
            print(f"Błąd podczas dodawania rekordu do bazy danych: {str(e)}")

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    Window.size = (400, Window.height)
    MyApp().run()
