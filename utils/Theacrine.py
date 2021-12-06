# -*- coding: utf-8 -*-
from utils.win_sched import SCHEDULES, EVENTS_LIST, time_check
from utils.win_nolock import keep_system_awake

import PySimpleGUI as sg
import time
import os
import sys
import sched


# === Auxiliaries methods ===
def resource_path(path):
    relative_path = path
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# === Interfaces methods ===
class Theacrine:
    """
    Theacrine IDE class
    """
    # Initializing
    def __init__(self):
        """Constructor"""
        print('Constructor called')
        self.SCHEDULES = SCHEDULES
        self.EVENTS_LIST = EVENTS_LIST
        pass

    # Calling destructor
    def __del__(self):
        """Destructor"""
        print('Destructor called')
        pass

    # === Another methods ===
    def modal_theacrine(self):
        """
        Constructor do form de escolha da Aplicacao
        @return: object
        """
        # theacrine = self

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

        window = sg.Window('Theacrine settings', icon=resource_path(path='icons/default_16.ico')).Layout(layout)
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
                exit(0)
                break

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
                        self.EVENTS_LIST = time_check(mins=5, loops=loops[0])  # Notifier a cada 5min

                        # Return all to default state:
                        keep_system_awake(mode=0)
                        window.Normal()
        pass

    # noinspection PyMethodMayBeStatic
    def modal_theacrine_error(self, msg_error='Unidentified error'):
        """
        @return:
        """
        epoch_time = float(time.time())
        events = self.EVENTS_LIST
        # Cancel all prior schedules
        # scheduler = sched.scheduler(time.time, time.sleep)
        if len(events) > 0:
            for event in events:
                if event.time < epoch_time:
                    events.pop(0)

            for queue in events:
                self.SCHEDULES.cancel(queue)

        self.error = msg_error

        layout = [  [sg.Text('Detalhes do erro:', background_color='red')],
                    [sg.Output(size=(50,10), key='-OUTPUT-')],
                    [sg.Text(key='-OUT-')],
                    [sg.Button('Exit')]  ]


        sg.theme('DarkRed1')
        window = sg.Window('Logs de erro', layout, finalize = True)
        
        window['-OUTPUT-'].update(self.error)

        try:
            print('\nScheds ativos: ', str(self.SCHEDULES))
            while True:  # Event Loop
                # window.bad()
                event, values = window.read()
                print('\n\nSaindo...')

                if event in (sg.WIN_CLOSED, 'Exit'):
                    break

        except Exception:
            sg.popup_error(f'AN EXCEPTION OCCURRED!', 'Detalhes do Erro', title=True)
            sg.Print(f'An error happened.  Here is the info:', self.error, end='\n', keep_on_top=True)
            while True:
                values = sg.Button()

                if values == True:
                    break
            window.close()
    pass
