import psutil
import time


def secs2hours(secs):
    """
    Funcao que converte os segs restantes em formato tempo.
    # print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
    @param: secs= time in seconds
    @return: saidaBateria, sendo: restatempo, restacarga, situacao.
    """
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def saidaBateria(a='default', b='Default'):
    time.sleep(2)
    print('Saida', a, 'da package.:', b)


def restatempoBateria(a='tempo'):
    battery = psutil.sensors_battery()
    b = secs2hours(battery.secsleft)
    saidaBateria(a, b)
    return b


def restacargaBateria(a='carga'):
    battery = psutil.sensors_battery()
    b = battery.percent
    saidaBateria(a, b)
    return b


def situacaoBateria(a='situacao'):
    battery = psutil.sensors_battery()
    b = battery.power_plugged
    saidaBateria(a, b)
    return b
