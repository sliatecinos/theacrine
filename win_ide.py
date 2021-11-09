from win_sched import time_check
import PySimpleGUI as sg
import time
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def modalTheacrine():
    """
    Constructor do form de escolha da Aplicacao
    :return: object
    """
    sg.theme('Teal Mono')

    title = 'Escolha o periodo de funcionamento do Theacrine:'
    layout = [[sg.Text(title)],  # Textbox caption
            [sg.Combo(['4 hrs', '6 hrs', '8 hrs'], key='-COMBO-')],  # Periodos
            [sg.Text('', key='-TEXT1-')],  # Textbox de erro
            [sg.OK(), sg.Button('Sair')]  # Menu de opcoes
    ]

    window = sg.Window('Theacrine main panel', layout, icon=resource_path('default_16.ico'))

    while True:
        event, values = window.read()
        # print(event, values)

        if event in ('Sair', None):
            break
            exit(0)

        dict_options = {'4 hrs': 4, '6 hrs': 6, '8 hrs': 8}
        if event == 'OK':
            if values['-COMBO-'] not in dict_options:
                window['-TEXT1-'].update('Escolha um valor disponível !')

            else:
                selected = dict_options[values['-COMBO-']]
                ix = list(dict_options.keys())[list(dict_options.values()).index(selected)]
                msg = 'Você selecionou: (%s)\nCorreto ?' % ix

                # Cria Popup de confirmacao da option escolhida
                button = sg.popup_yes_no(msg)

                if button == 'Yes':
                    window['-TEXT1-'].update('Selecionado... ' + str(selected))
                    time.sleep(3)
                    loops = divmod(selected * 60, 5)  # Nr of loops x 1HR

                    window.minimize()

                    # Start loops of checks
                    time_check(mins=5, loops=loops[0])  # Notifier a cada 5min
                    window.Normal()
