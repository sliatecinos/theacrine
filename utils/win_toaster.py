from win10toast import ToastNotifier
import time
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def notaBaixaBateria(taxacarga=5, tempo='0:05:00'):
    msg = f"Bateria esgotando em: {tempo}.\nRestam apenas {taxacarga}%."
    normal = True
    duration = 15

    if taxacarga < 10:
        normal = False
        duration = 20

    toaster = ToastNotifier()
    toaster.show_toast("Theacrine aviso",
                       msg=msg,
                       icon_path=resource_path("default_32.ico"),
                       duration=duration,
                       threaded=normal)

    # Wait for threaded notification to finish
    while toaster.notification_active():
        time.sleep(0.1)
