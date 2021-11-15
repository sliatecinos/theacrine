from win_sched import time_check
from utils.win_nolock import keep_system_awake
import traceback
import PySimpleGUI as sg
import time
import os
import sys


class Theacrine:
    """
    Theacrine IDE class
    """

    def __init__(self):
        '''Constructor'''
        pass

    # Auxiliaries Functions
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    # Interfaces declarations
    def modal_theacrine():
        """
        Constructor do form de escolha da Aplicacao
        @return: object
        """
        sg.theme('DarkGrey')

        # Captions section
        title = 'Escolha o periodo de funcionamento do Theacrine:'
        radiotext = 'Ficar acordado?'

        layout = [[sg.Text(title)],  # Textbox caption
                [sg.Combo(['2 hrs', '4 hrs', '6 hrs', '8 hrs'], key='-COMBO-')],  # Periodos
                [sg.Text('', key='-TEXT1-', text_color='yellow')],  # Textbox de erro
                [sg.OK('Comece!'), sg.Button('Sair')],  # Menu de opcoes
                [sg.Text(radiotext)],  # Textbox radio
                [sg.Radio('N', 1, enable_events=True, key="R1"),
                sg.Radio('S', 2, enable_events=True, key="R2")]  # Menu de Acordado

        ]

        window = sg.Window('Theacrine settings', icon=Theacrine.resource_path('icons/default_16.ico')).Layout(layout)
        acordado = None

        while True:
            event, values = window.read()

            # Acoes de RadioButton
            if values['R2']:
                window['R1'].Update(False)
                acordado = True

            if values['R1']:
                window['R2'].Update(False)
                acordado = False

            if event in ('Sair', None):
                break
                exit(0)

            dict_options = {'2 hrs': 2, '4 hrs': 4, '6 hrs': 6, '8 hrs': 8}
            if event == 'Comece!':
                if values['-COMBO-'] not in dict_options:
                    window['-TEXT1-'].update('Escolha um valor disponível !')

                elif acordado is None:
                    window['-TEXT1-'].update('Precisa escolher se fica acordado !')

                else:
                    selected = dict_options[values['-COMBO-']]
                    acordado_dict = {True: 'Ficar', False: 'Nao Ficar'}  # Acordado dict

                    ix = list(dict_options.keys())[list(dict_options.values()).index(selected)]  # Opcao escolhida
                    msg = 'Você selecionou: (%s)\nE %s acordado. Ta Certo ?' % (ix, acordado_dict[acordado])

                    # Cria Popup de confirmacao da option escolhida:
                    button = sg.popup_yes_no(msg)

                    if button == 'Yes':
                        window['-TEXT1-'].update('Selecionado... ' + str(selected))
                        loops = divmod(selected * 60, 5)  # Nr of loops x 1HR

                        time.sleep(3)
                        window.minimize()

                        # Start set of no-screen-lock:
                        keep_system_awake(mode=acordado)

                        # Start loops of checks:
                        time_check(mins=5, loops=loops[0])  # Notifier a cada 5min

                        # Return all to default state:
                        keep_system_awake(mode=0)
                        window.Normal()

