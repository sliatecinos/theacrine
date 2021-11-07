from win_sched import time_check
import PySimpleGUI as sg
import time


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

    window = sg.Window('Theacrine main panel', layout, icon='thea-leaf-32.ico')

    while True:
        event, values = window.read()
        # print(event, values)

        if event in ('Sair', None):
            break
            exit(0)

        if event == 'OK':
            if values['-COMBO-'] == '':
                window['-TEXT1-'].update('Precisa escolher um valor !')

            else:
                dict_options = {'4 hrs': 4, '6 hrs': 6, '8 hrs': 8}
                selected = dict_options[values['-COMBO-']]
                # print(selected)
                window['-TEXT1-'].update('Selecionado... ' + str(selected))
                time.sleep(3)
                loops = divmod(selected * 60, 5)  # Nr of loops x 1HR

                window.minimize()

                # Start loops of checks
                time_check(mins=5, loops=loops[0])  # Notifier a cada 5min
                window.Normal()
