import psutil


def secs2hours(secs):
    """
    Funcao que converte os segs restantes em formato tempo.
    """
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


battery = psutil.sensors_battery()
# print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))

def restatempo_Bateria():
    return secs2hours(battery.secsleft)

def restacarga_Bateria():
    return battery.percent

def situacao_Bateria():
    return battery.power_plugged
