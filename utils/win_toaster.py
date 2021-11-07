from win10toast import ToastNotifier
import time


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
                       icon_path="thea-leaf-32.ico",
                       duration=duration,
                       threaded=normal)

    # toaster.show_toast("Example two",
    #                    "This notification is in it's own thread!",
    #                    icon_path=None,
    #                    duration=5,
    #                    threaded=True)

    # Wait for threaded notification to finish
    while toaster.notification_active():
        time.sleep(0.1)
