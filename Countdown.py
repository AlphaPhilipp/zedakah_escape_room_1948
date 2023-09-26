import PySimpleGUI as sg
from playsound import playsound


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
    window = sg.Window(
        "Countdown", layout, fullscreen=True, element_justification="center"
    )

    # Variablen initialisieren
    minutes = 60
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
                playsound("Abgelaufen.mp3")
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
