from utils.win_psutil import *
from utils.win_toaster import notaBaixaBateria
import sched
import time
from datetime import datetime


# Creating an instance of the scheduler class
s = sched.scheduler(time.time, time.sleep)

def convert_date(t=1636254512):
    """
    Funcao de retorno para carimbo de data-hora
    :param t: float/int
    :return: carimbo time (str)
    """
    return datetime.fromtimestamp(t).strftime('%c')

def span_battery():
    """
    Funcao Main de check da Bateria.
    :param mins: minutes (int)
    :return: new span instance
    """

    print('<<START>>:', convert_date(time.time()))

    tempo = restatempoBateria()
    taxacarga = restacargaBateria()
    situacao = situacaoBateria()

    # A partir de 25% Battery, e AC off: gera toast
    if taxacarga < 25 and not situacao:
        notaBaixaBateria(taxacarga=taxacarga, tempo=tempo)

    print('Restante:', tempo, '. Carga:', taxacarga, 'AC conn:', situacao)
    print('<<END>>:', convert_date(time.time()))

    pass
    # return tempo, carga, situacao


def time_check(mins=1, loops=1):
    """
    Funcao de sched dos checks da Bateria.
    :param mins: minutes (int)
    :return: new span instance
    """
    events = []
    events_list = [events.append(None) for i in range(loops)]
    secs = mins * 60
    i = 0
    while i < loops:
        events_list[i] = s.enter(secs * i, 1, span_battery)
        i += 1

    s.run()
