# -*- coding: utf-8 -*-
from utils.win_psutil import *
from utils.win_toaster import notaBaixaBateria
from datetime import datetime

import time
import sched
import threading


# Creating a global instance of the scheduler class
global SCHEDULES
SCHEDULES = sched.scheduler(time.time, time.sleep)

global EVENTS_LIST
EVENTS_LIST = []

def span_battery():
    """
    Funcao Main de check da Bateria.
    @param: mins= minutes (int)
    @return: new span instance
    """

    print('[log]<<START>>:', time.localtime(time.time()))

    tempo = restatempoBateria()
    taxacarga = restacargaBateria()
    situacao = situacaoBateria()

    # A partir de 40% Battery, e AC off: gera toast
    if taxacarga < 40 and not situacao:
        notaBaixaBateria(taxacarga=taxacarga, tempo=tempo, ac_on=situacao)

    print('[log]Restante:', tempo, '. Carga:', taxacarga, 'AC conn:', situacao)
    print('[log]<<END>>:', time.localtime(time.time()))

    pass


def time_check(mins=1, loops=1):
    """
    Funcao de sched dos checks da Bateria.
    @param: mins= minutes (int)
    @return: new span instance
    """

    events = []
    EVENTS_LIST = [events.append(None) for i in range(loops)]
    secs = mins * 60
    i = 0
    while i < loops:
        EVENTS_LIST[i] = SCHEDULES.enter(secs * i, 1, span_battery)
        i += 1
    # s.run()

    # Start a thread to run the events
    t = threading.Thread(target=SCHEDULES.run)
    t.start()

    return EVENTS_LIST
