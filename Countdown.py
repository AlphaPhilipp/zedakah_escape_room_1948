import PySimpleGUI as sg

from playsound import playsound

sg.theme("DarkBlue1")


# Fenster, wenn der Countdown abgelaufen ist
def exit_window():
    # Exit Window Layout
    column_exit = [
        [sg.Image(filename="Exit.png", expand_y=True)],
        [sg.Text("Die Zeit ist um! Nichts wie raus. Findet den Ausgang!")],
        [sg.Button(k="-EXIT-", button_text="Beenden", button_color="red")],
    ]

    layout_exit = [
        [
            sg.Column(
                column_exit,
                expand_y=True,
                vertical_alignment="center",
                justification="c",
                element_justification="c",
                k="-EXIT-",
                visible=True,
            ),
        ],
    ]
    # Exit Window initialization
    exit_window = sg.Window(
        "Escape Room",
        layout_exit,
        no_titlebar=True,
        location=(0, 0),
        keep_on_top=True,
    ).Finalize()
    exit_window.Maximize()

    # Exit Window Event Loop
    while True:
        event, values = exit_window.read()

        # User klickt auf "Beenden"
        if event == "-EXIT-":
            exit = sg.popup_ok_cancel(
                "Möchtest du das Master Control Programm wirklich schließen? Du könntest Hinweise übersehen haben!  Ab hier hilft der Computer nicht mehr weiter...",
                title="Programm beenden?",
                keep_on_top=True,
            )
            # Beenden bei OK
            if exit == "OK":
                break

        # End Exit Window if user closes window
        if event == sg.WIN_CLOSED:
            break
    exit_window.close()


def main():
    # GUI-Layout definieren
    layout = [
        [
            sg.Text(
                "Countdown:",
                font=("Helvetica", 100),
                text_color="red",
                key="-TIMER-",
                justification="center",
            )
        ]
    ]

    # Fenster erstellen
    window = sg.Window("Countdown", layout, element_justification="center")

    # Variablen initialisieren
    minutes = 59
    seconds = 0

    # Event Loop
    while True:
        event, _ = window.read(timeout=1000)  # Alle 1 Sekunde aktualisieren

        if event in (sg.WINDOW_CLOSED, "Escape:27"):
            break

        # Countdown aktualisieren
        if seconds == 0:
            if minutes == 30:
                playsound("Audio30min.mp3")  # Audio-Datei abspielen
            if minutes == 15:
                playsound("Audio30min.mp3")  # Audio-Datei abspielen
            if minutes == 5:
                playsound("Audio30min.mp3")  # Audio-Datei abspielen
            if minutes == 0:
                playsound("Abgelaufen.mp3")  # Audio-Datei abspielen
                exit_window()  # Fenster oeffnen
                break  # Countdown abgelaufen
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1

        # Countdown-Anzeige aktualisieren
        window["-TIMER-"].update(f"{minutes:02d}:{seconds:02d}")

    window.close()


if __name__ == "__main__":
    main()
