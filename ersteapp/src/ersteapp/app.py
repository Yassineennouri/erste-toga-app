import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class NotizApp(toga.App):
    def startup(self):
        # Hauptcontainer
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # Titel der App
        title_label = toga.Label(
            'Meine Notizen',
            style=Pack(padding=(0, 0, 10, 0))
        )
        
        # Eingabefeld für Notizen
        self.note_input = toga.MultilineTextInput(
            placeholder='Schreibe deine Notiz hier...',
            style=Pack(flex=1, padding=5)
        )
        
        # Button zum Speichern
        save_button = toga.Button(
            'Notiz speichern',
            on_press=self.save_note,
            style=Pack(padding=5)
        )
        
        # Label für die Ausgabe
        self.output_label = toga.Label(
            'Gespeicherte Notizen:',
            style=Pack(padding=5)
        )
        
        # Liste für gespeicherte Notizen
        self.notes_view = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, padding=5)
        )
        
        # Komponenten zum Hauptcontainer hinzufügen
        self.main_box.add(title_label)
        self.main_box.add(self.note_input)
        self.main_box.add(save_button)
        self.main_box.add(self.output_label)
        self.main_box.add(self.notes_view)
        
        # Hauptfenster erstellen
        self.main_window = toga.MainWindow(title='Notiz App')
        self.main_window.content = self.main_box
        self.main_window.show()
        
        # Liste für Notizen
        self.notes = []

    def save_note(self, widget):
        note_text = self.note_input.value
        if note_text.strip():  # Prüfen ob die Notiz nicht leer ist
            # Notiz zur Liste hinzufügen
            self.notes.append(note_text)
            
            # Notizen im Ausgabefeld aktualisieren
            self.notes_view.value = '\n\n'.join(self.notes)
            
            # Eingabefeld leeren
            self.note_input.value = ''
            
            # Bestätigungsmeldung
            self.main_window.info_dialog(
                'Erfolg',
                'Notiz wurde gespeichert!'
            )
        else:
            # Fehlermeldung wenn keine Notiz eingegeben wurde
            self.main_window.error_dialog(
                'Fehler',
                'Bitte gib eine Notiz ein!'
            )

def main():
    return NotizApp('Notiz App', 'org.example.notizapp')

if __name__ == '__main__':
    app = main()
    app.main_loop()