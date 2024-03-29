import PySimpleGUI as sg
from sys import platform as PLATFORM

# import cv2
import lgpio
import time

gpio_pins = [2, 3, 4, 14, 15, 21]

# LGPIO initialisieren
gpio = lgpio.gpiochip_open(0)

for pin in gpio_pins:
    lgpio.gpio_claim_output(gpio, pin)

# Tasseschrank 57, Relais3
# 54, Relais 2
# 59, Relais 1
# 60, Relais 4
# Bunkertür 24, Relais 5
# Blaulicht, Relais 6

# Funktion für cv2
# def play_video(file_path):
#    cap = cv2.VideoCapture(file_path)
#
#    while cap.isOpened():
#        ret, frame = cap.read()
#
#        if not ret:
#            break
#
#        cv2.imshow("Video", frame)
#
#        if cv2.waitKey(1) & 0xFF == ord("q"):
#            break
#
#    cap.release()
#    cv2.destroyAllWindows()


sg.theme("DarkBlue1")

numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
# Layout within the column on the first screen (locked folder)
column_MasterFolder = [
    [sg.Text("", expand_y=True)],
    [
        sg.Button(
            key="MasterFolder",
            image_filename="LockedFolder.png",
            button_color="#252834",
        )
    ],
    [sg.Text("", expand_y=True)],
]

# Layout within the column on the second screen (subfolders)
column_Subfolders1 = [
    [sg.Text("", expand_y=True)],
    [
        sg.Button(
            key="Subfolder-Ordnung-1",
            image_filename="UnlockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Teepause-1",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Universum-1",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Code837-1",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
    ],
    [
        sg.Text("Ordnung", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Teepause", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Universum", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Code 837", expand_y=True, expand_x=True, justification="c"),
    ],
]
column_Subfolders2 = [
    [sg.Text("", expand_y=True)],
    [
        sg.Button(
            key="Subfolder-Ordnung-2",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Teepause-2",
            image_filename="UnlockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Universum-2",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Code837-2",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
    ],
    [
        sg.Text("Ordnung", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Teepause", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Universum", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Code 837", expand_y=True, expand_x=True, justification="c"),
    ],
]
column_Subfolders3 = [
    [sg.Text("", expand_y=True)],
    [
        sg.Button(
            key="Subfolder-Ordnung-3",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Teepause-3",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Universum-3",
            image_filename="UnlockedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Code837-3",
            image_filename="LockedFolder.png",
            button_color="#252834",
        ),
    ],
    [
        sg.Text("Ordnung", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Teepause", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Universum", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Code 837", expand_y=True, expand_x=True, justification="c"),
    ],
]
column_Subfolders4 = [
    [sg.Text("", expand_y=True)],
    [
        sg.Button(
            key="Subfolder-Ordnung-4",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Teepause-4",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Universum-4",
            image_filename="SolvedFolder.png",
            button_color="#252834",
        ),
        sg.Button(
            key="Subfolder-Code837-4",
            image_filename="UnlockedFolder.png",
            button_color="#252834",
        ),
    ],
    [
        sg.Text("Ordnung", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Teepause", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Universum", expand_y=True, expand_x=True, justification="c"),
        sg.Text("Code 837", expand_y=True, expand_x=True, justification="c"),
    ],
]

# Layout within the column on the Ordnung Screen
column_Ordnung_List = [
    [
        sg.Combo(
            ["", "1", "2", "3", "4", "5"],
            expand_y=True,
            pad=(10, 10),
            font=(any, 23),
            k="-Ordnung-C4",
        ),
        sg.Button(
            "Ist ein Volk auf einmal zur Welt gekommen?",
            font=(any, 23),
            pad=(10, 10),
        ),
    ],
    [
        sg.Combo(
            ["", "1", "2", "3", "4", "5"],
            expand_y=True,
            pad=(10, 10),
            font=(any, 23),
            k="-Ordnung-C5",
        ),
        sg.Button(
            "Kaum in Wehen, hat Zion schon ihre Kinder geboren.",
            font=(any, 23),
            pad=(10, 10),
        ),
    ],
    [
        sg.Combo(
            ["", "1", "2", "3", "4", "5"],
            expand_y=True,
            pad=(10, 10),
            font=(any, 23),
            k="-Ordnung-C2",
        ),
        sg.Button(
            "Wer hat solches je gesehen?",
            font=(any, 23),
            pad=(10, 10),
        ),
    ],
    [
        sg.Combo(
            ["", "1", "2", "3", "4", "5"],
            expand_y=True,
            pad=(10, 10),
            font=(any, 23),
            k="-Ordnung-C3",
        ),
        sg.Button(
            "Ward ein Land an einem Tage geboren?",
            font=(any, 23),
            pad=(10, 10),
        ),
    ],
    [
        sg.Combo(
            ["", "1", "2", "3", "4", "5"],
            expand_y=True,
            pad=(10, 10),
            font=(any, 23),
            k="-Ordnung-C1",
        ),
        sg.Button(
            "Wer hat solches je gehört?",
            font=(any, 23),
            pad=(10, 10),
        ),
    ],
]

# Layout within the bottom column on the Ordnung Screen
column_Ordnung_Bottom = [
    [
        sg.Text(
            ".- - - /. /. . ./.-/. - - - /. - / - . . . . / - . . . ./, - - - ..",
            text_color="#000011",
            justification="c",
            font=(any, 23),
        )
    ],
    [
        sg.Button("Lösung prüfen", k="-CHECK-Ordnung-", size=(20, 2), font=(any, 23)),
    ],
]

# Layout within the column on the Universum Screen
column_Universum = [
    [
        sg.Image(filename="Sonne.png", subsample=(2), pad=(15, 15)),
        sg.Image(filename="Mond.png", subsample=(2), pad=(15, 15)),
        sg.Image(filename="Sterne.png", subsample=(2), pad=(15, 15)),
        sg.Image(filename="Meer.png", subsample=(2), pad=(15, 15)),
    ],
    [
        sg.Combo(
            numbers,
            pad=(10, 10),
            font=(any, 23),
            k="-Universum-C1",
        ),
        sg.Combo(
            numbers,
            pad=(10, 10),
            font=(any, 23),
            k="-Universum-C2",
        ),
        sg.Combo(
            numbers,
            pad=(10, 10),
            font=(any, 23),
            k="-Universum-C3",
        ),
        sg.Combo(
            numbers,
            pad=(10, 10),
            font=(any, 23),
            k="-Universum-C4",
        ),
    ],
    [
        sg.Button(
            "Lösung prüfen",
            k="-CHECK-Universum-",
            auto_size_button=True,
            font=(any, 23),
        )
    ],
]

# Layout within the column on the Code 837 Screen
column_code837_1 = [
    [
        sg.Text(
            "Was ist der gesuchte Code Name?",
            expand_y=True,
            expand_x=True,
            justification="c",
        )
    ],
    [
        sg.Button(
            key="Gott der Allmaechtige",
            image_filename="Code 837_Gott der Allmaechtige.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Fels Israels",
            image_filename="Code 837_Fels Israels.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="der lebendige Gott",
            image_filename="Code 837_Der lebendige Gott.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Hoffnung Israels",
            image_filename="Code 837_Hoffnung Israels.png",
            button_color="#252834",
            size=(310, 233),
        ),
    ],
    [
        sg.Button(
            key="Herr der Heerscharen",
            image_filename="Code 837_Herr der Heerscharen.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Jakobs Anteil",
            image_filename="Code 837_Jakobs Anteil.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="der Heilige Israels",
            image_filename="Code 837_der Heilige Israels.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Koenig der Ewigkeit",
            image_filename="Code 837_Koenig der Ewigkeit.png",
            button_color="#252834",
            size=(310, 233),
        ),
    ],
    [
        sg.Button(
            key="der Gott eurer Vaeter",
            image_filename="Code 837_der Gott eurer Vaeter.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Schrecken Isaaks",
            image_filename="Code 837_Schrecken Isaaks.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="Hueter Israels",
            image_filename="Code 837_Hueter Israels.png",
            button_color="#252834",
            size=(310, 233),
        ),
        sg.Button(
            key="hoechster Gott",
            image_filename="Code 837_hoechster Gott.png",
            button_color="#252834",
            size=(310, 233),
        ),
    ],
    [sg.Text("", expand_y=True)],
]
column_code837_2 = [
    [
        sg.Text(
            "",
            k="-EXPAND-",
            expand_y=True,
        )
    ],
    [
        sg.Input(
            k="-INPUT-Code837-",
            font=(any, 23),
            size=(9, 1),
            expand_x=True,
            justification="c",
        )
    ],
    [sg.Button("Lösung prüfen")],
    [
        sg.Text("", k="-EXPAND2-", expand_y=True),
    ],
]

column_exit = [
    [sg.Image(filename="Exit.png", expand_y=True)],
    [sg.Text("Geschafft! Nichts wie raus")],
    [sg.Button(k="-EXIT-", button_text="Beenden", button_color="red")],
]
# Layout within the Master Folder Window
layout_MasterFolder = [
    [
        sg.Button(
            "Tippen zum aktivieren",
            k="-ACTIVATE-",
            button_color="black",
            size=(1920, 1080),
            pad=(0, 0),
            font=(any, 23),
        ),
        sg.Column(
            column_MasterFolder,
            k="-MasterFolderColumn-",
            vertical_alignment="c",
            expand_y=True,
            visible=False,
        ),
    ],
]

# Create the Master Window
master_window = sg.Window(
    "Escape Room",
    layout_MasterFolder,
    # no_titlebar=True,
    location=(0, 0),
    size=(1920, 1080),
    # keep_on_top=True,
    element_justification="center",
    element_padding=None,
).Finalize()
# master_window.Maximize()


# Second (Subfolders) Window
def subfolder_window():
    # Second Window Layout
    layout_subfolders = [
        [
            sg.Column(
                column_Subfolders1,
                vertical_alignment="center",
                justification="center",
                k="-SubfoldersColumn1-",
                expand_y=True,
            ),
            sg.Column(
                column_Subfolders2,
                vertical_alignment="center",
                justification="center",
                k="-SubfoldersColumn2-",
                expand_y=True,
                visible=False,
            ),
            sg.Column(
                column_Subfolders3,
                vertical_alignment="center",
                justification="center",
                k="-SubfoldersColumn3-",
                expand_y=True,
                visible=False,
            ),
            sg.Column(
                column_Subfolders4,
                vertical_alignment="center",
                justification="center",
                k="-SubfoldersColumn4-",
                expand_y=True,
                visible=False,
            ),
        ]
    ]

    # Second Window initialization
    subfolders_window = sg.Window(
        "Escape Room",
        layout_subfolders,
        no_titlebar=True,
        location=(0, 0),
        keep_on_top=True,
    ).Finalize()
    subfolders_window.Maximize()

    # Defining variables
    unlock_Teepause = False
    unlock_Universum = False
    unlock_Code837 = False

    solved_Ordnung = False
    solved_Teepause = False
    solved_Universum = False

    # Second Window (Subfolders Window) Event Loop
    while True:
        event, values = subfolders_window.read()
        # Open Ordnung
        if (
            event == "Subfolder-Ordnung-1"
            or event == "Subfolder-Ordnung-2"
            or event == "Subfolder-Ordnung-3"
            or event == "Subfolder-Ordnung-4"
        ) and solved_Ordnung == False:
            unlock_Teepause = True
            solved_Ordnung = True
            subfolders_window["-SubfoldersColumn1-"].update(visible=False)
            subfolders_window["-SubfoldersColumn2-"].update(visible=True)
            ordnung_window()

        # Error if solved
        elif (
            event == "Subfolder-Ordnung-1"
            or event == "Subfolder-Ordnung-2"
            or event == "Subfolder-Ordnung-3"
            or event == "Subfolder-Ordnung-4"
        ) and solved_Ordnung == True:
            sg.popup_ok(
                "Dieses Rätsel wurde bereits gelöst!",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        # Open Teepause if unlocked
        if (
            (
                event == "Subfolder-Teepause-1"
                or event == "Subfolder-Teepause-2"
                or event == "Subfolder-Teepause-3"
                or event == "Subfolder-Teepause-4"
            )
            and unlock_Teepause == True
            and solved_Teepause == False
        ):
            solved_Teepause = True
            unlock_Universum = True

            # Teepause Event Loop
            while True:
                sg.popup_timed(
                    "Verbindung abgebrochen. Ein Netzwerkfehler liegt vor.",
                    auto_close_duration=5,
                    keep_on_top=True,
                )
                password = sg.popup_get_text(
                    "Möge die Hitze die Schwärze aus unserem Inneren wegspülen, auf dass das Licht der Wahrheit erscheine",
                    "Netzwerkschlüssel eingeben",
                    keep_on_top=True,
                )
                if password == "Euer Land":
                    sg.popup_timed(
                        "Korrekt! Der nächste Ordner wird entsperrt.",
                        title="Korrekt!2",
                        auto_close_duration=3,
                        keep_on_top=True,
                    )
                    # Relais2
                    state = lgpio.gpio_read(gpio, gpio_pins[1])
                    lgpio.gpio_write(gpio, gpio_pins[1], not state)
                    time.sleep(2)
                    state = lgpio.gpio_read(gpio, gpio_pins[1])
                    lgpio.gpio_write(gpio, gpio_pins[1], not state)
                    break
                else:
                    sg.popup_ok(
                        "Passwort falsch!",
                        title="Fehler",
                        keep_on_top=True,
                    )
            subfolders_window["-SubfoldersColumn2-"].update(visible=False)
            subfolders_window["-SubfoldersColumn3-"].update(visible=True)

        # Error if locked
        elif (
            event == "Subfolder-Teepause-1"
            or event == "Subfolder-Teepause-2"
            or event == "Subfolder-Teepause-3"
            or event == "Subfolder-Teepause-4"
        ) and unlock_Teepause == False:
            sg.popup_ok(
                "Ordner gesperrt",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        # Error if solved
        elif (
            (
                event == "Subfolder-Teepause-1"
                or event == "Subfolder-Teepause-2"
                or event == "Subfolder-Teepause-3"
                or event == "Subfolder-Teepause-4"
            )
            and unlock_Teepause == True
            and solved_Teepause == True
        ):
            sg.popup_ok(
                "Dieses Rätsel wurde bereits gelöst!",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        # Open Universum if unlocked
        if (
            (
                event == "Subfolder-Universum-1"
                or event == "Subfolder-Universum-2"
                or event == "Subfolder-Universum-3"
                or event == "Subfolder-Universum-4"
            )
            and unlock_Universum == True
            and solved_Universum == False
        ):
            unlock_Code837 = True
            solved_Universum = True
            subfolders_window["-SubfoldersColumn3-"].update(visible=False)
            subfolders_window["-SubfoldersColumn4-"].update(visible=True)
            universum_window()

        # Error if locked
        elif (
            event == "Subfolder-Universum-1"
            or event == "Subfolder-Universum-2"
            or event == "Subfolder-Universum-3"
            or event == "Subfolder-Universum-4"
        ) and unlock_Universum == False:
            sg.popup_ok(
                "Ordner gesperrt",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        # Error if solved
        elif (
            (
                event == "Subfolder-Universum-1"
                or event == "Subfolder-Universum-2"
                or event == "Subfolder-Universum-3"
                or event == "Subfolder-Universum-4"
            )
            and unlock_Universum == True
            and solved_Universum == True
        ):
            sg.popup_ok(
                "Dieses Rätsel wurde bereits gelöst!",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        # Open Code837 if unlocked
        if (
            event == "Subfolder-Code837-1"
            or event == "Subfolder-Code837-2"
            or event == "Subfolder-Code837-3"
            or event == "Subfolder-Code837-4"
        ) and unlock_Code837 == True:
            code837_window()
            break

        # Error if locked
        elif (
            event == "Subfolder-Code837-1"
            or event == "Subfolder-Code837-2"
            or event == "Subfolder-Code837-3"
            or event == "Subfolder-Code837-4"
        ) and unlock_Code837 == False:
            sg.popup_ok(
                "Ordner gesperrt",
                title="Kein Zugriff",
                keep_on_top=True,
            )

        if event == sg.WIN_CLOSED:
            break
    subfolders_window.close()


# Ordnung Window
def ordnung_window():
    # Ordnung Window Layout
    layout_ordnung = [
        [
            sg.Column(
                column_Ordnung_List,
                vertical_alignment="center",
                justification="c",
                element_justification="l",
                expand_y=False,
                k="-OrdnungColumnList-",
            ),
        ],
        [sg.Text("", expand_y=True)],
        [
            sg.Column(
                column_Ordnung_Bottom,
                vertical_alignment="c",
                justification="c",
                element_justification="c",
                expand_y=True,
            )
        ],
    ]
    # Ordnung Window initialization
    ordnung_window = sg.Window(
        "Escape Room",
        layout_ordnung,
        no_titlebar=True,
        location=(0, 0),
        keep_on_top=True,
    ).Finalize()
    ordnung_window.Maximize()

    # Ordnung Window Event Loop
    while True:
        event, values = ordnung_window.read()

        # Close the Window if Solution is correct
        if (
            event == "-CHECK-Ordnung-"
            and values["-Ordnung-C1"] == "1"
            and values["-Ordnung-C2"] == "2"
            and values["-Ordnung-C3"] == "3"
            and values["-Ordnung-C4"] == "4"
            and values["-Ordnung-C5"] == "5"
        ):
            sg.popup_timed(
                "Korrekt! Der nächste Ordner wird entsperrt.",
                title="Korrekt!3",
                auto_close_duration=3,
                keep_on_top=True,
            )
            # Relais3
            state = lgpio.gpio_read(gpio, gpio_pins[2])
            lgpio.gpio_write(gpio, gpio_pins[2], not state)
            time.sleep(2)
            state = lgpio.gpio_read(gpio, gpio_pins[2])
            lgpio.gpio_write(gpio, gpio_pins[2], not state)

            break

        # Error if Solution is incorrect
        elif event == "-CHECK-Ordnung-":
            sg.popup_ok(
                "Passwort falsch!",
                title="Fehler",
                keep_on_top=True,
            )

        # End Ordnung Window if user closes window
        if event == sg.WIN_CLOSED:
            break
    ordnung_window.close()


# Universum Window
def universum_window():
    # Universum Window Layout
    layout_universum = [
        [
            sg.Column(
                column_Universum,
                vertical_alignment="center",
                justification="c",
                element_justification="c",
                k="-UniversumColumn-",
            ),
        ],
    ]
    # Universum Window initialization
    universum_window = sg.Window(
        "Escape Room",
        layout_universum,
        no_titlebar=True,
        location=(0, 0),
        keep_on_top=True,
        element_justification="c",
    ).Finalize()
    universum_window.Maximize()

    # Universum Window Event Loop
    while True:
        event, values = universum_window.read()

        # Close the Window if Solution is correct
        if (
            event == "-CHECK-Universum-"
            and values["-Universum-C1"] == "0"
            and values["-Universum-C2"] == "5"
            and values["-Universum-C3"] == "7"
            and values["-Universum-C4"] == "3"
        ):
            sg.popup_timed(
                "Korrekt! Der nächste Ordner wird entsperrt.",
                title="Korrekt!1",
                auto_close_duration=3,
                keep_on_top=True,
            )
            # Relais1
            state = lgpio.gpio_read(gpio, gpio_pins[0])
            lgpio.gpio_write(gpio, gpio_pins[0], not state)
            time.sleep(2)
            state = lgpio.gpio_read(gpio, gpio_pins[0])
            lgpio.gpio_write(gpio, gpio_pins[0], not state)
            break
        elif event == "-CHECK-Universum-":
            sg.popup_ok(
                "Passwort falsch!",
                title="Fehler",
                keep_on_top=True,
            )

        # End Universum Window if user closes window
        if event == sg.WIN_CLOSED:
            break
    universum_window.close()


# Code 837 Window
def code837_window():
    # Code 837 Window Layout
    layout_code837 = [
        [
            sg.Column(
                column_code837_1,
                expand_y=True,
                vertical_alignment="center",
                justification="c",
                element_justification="l",
                k="-Code837Column1-",
            ),
        ],
        [
            sg.Column(
                column_code837_2,
                expand_y=False,
                vertical_alignment="center",
                justification="c",
                element_justification="c",
                k="-Code837Column2-",
                visible=False,
            ),
        ],
    ]
    # Code 837 Window initialization
    code837_window = sg.Window(
        "Escape Room",
        layout_code837,
        no_titlebar=True,
        location=(0, 0),
        keep_on_top=True,
    ).Finalize()
    code837_window.Maximize()

    # Code 837 Window Event Loop
    while True:
        event, values = code837_window.read()

        # Open Input if Solution is correct
        if event == "Fels Israels":
            code837_window["-Code837Column1-"].update(visible=False)
            code837_window["-Code837Column2-"].update(visible=True)

        # Open End Message if Solution is Correct
        if event == "Lösung prüfen" and values["-INPUT-Code837-"] == "Fels Israels":
            exit_window()

            # Relais 5 Kurz ,6 und Nach Count. plus relais 4
            """state = lgpio.gpio_read(gpio, gpio_pins[4])
            lgpio.gpio_write(gpio, gpio_pins[4], not state)
            state = lgpio.gpio_read(gpio, gpio_pins[5])
            lgpio.gpio_write(gpio, gpio_pins[5], not state)
            time.sleep(2)
            state = lgpio.gpio_read(gpio, gpio_pins[4])
            lgpio.gpio_write(gpio, gpio_pins[4], not state)"""

            break

        if event == "Lösung prüfen" and values["-INPUT-Code837-"] != "Fels Israels":
            sg.popup_ok(
                "Codename falsch!",
                title="Fehler",
                keep_on_top=True,
            )

        if event != "Fels Israels" and event != "Lösung prüfen":
            sg.popup_ok(
                "Eingabe falsch!",
                title="Fehler",
                keep_on_top=True,
            )

        # End Code 837 Window if user closes window
        if event == sg.WIN_CLOSED:
            break
    code837_window.close()


def exit_window():
    # Exit Window Layout
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

        if event == "-EXIT-":
            exit = sg.popup_ok_cancel(
                "Möchtest du das Master Control Programm wirklich schließen? Du könntest Hinweise übersehen haben!  Ab hier hilft der Computer nicht mehr weiter...",
                title="Programm beenden?",
                keep_on_top=True,
            )
            if exit == "OK":
                break

        # End Exit Window if user closes window
        if event == sg.WIN_CLOSED:
            break
    exit_window.close()


# Master event loop
while True:
    event, values = master_window.read(timeout=1000)

    # Turn on Screen with tap
    if event == "-ACTIVATE-":
        master_window["-ACTIVATE-"].update(visible=False)
        # master_media_window()
        master_window["-MasterFolderColumn-"].update(visible=True)

    # Click on Master Folder opens Password Popup
    if event == "MasterFolder":
        password = sg.popup_get_text(
            "Passwort eingeben",
            "Passworteingabe",
            icon="LockedFolder.png",
            keep_on_top=True,
        )
        # If the Password is correct close master Window open the next window
        if password == "Israel1948":
            subfolder_window()
            break
        # If the password is incorrect display an error
        else:
            sg.popup_ok(
                "Passwort falsch!",
                title="Fehler",
                keep_on_top=True,
            )

    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break
master_window.close()
