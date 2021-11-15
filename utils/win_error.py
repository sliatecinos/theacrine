import traceback
import PySimpleGUI as sg


"""
https://stackoverflow.com/questions/59907714/how-can-pysimplegui-give-a-popup-message-if-the-script-has-crashed
"""


class TheacrineError:
    """
    Theacrine Error cslass
    """

    # Interfaces declarations
    def modal_theacrine_error():
        """
        @return:
        """
        layout = [[sg.Text('My Window')],
                  [sg.Input(key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
                  [sg.Button('Go'), sg.Button('Exit')]
                  ]

        window = sg.Window('Window Title', layout)

        try:
            while True:  # Event Loop
                event, values = window.read()
                window.bad()
                print(event, values)
                if event in (None, 'Exit'):
                    break
                if event == 'Go':
                    window['-OUT-'].update(values['-IN-'])

        except Exception as e:
            tb = traceback.format_exc()
            sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
            sg.Print(f'An error happened.  Here is the info:', e, tb, keep_on_top=True)
            while True:
                values = sg.Button()

                if values == True:
                    break
            window.close()
