import ctypes
import time


def keep_system_awake(mode=0):
    """
    Prevent from going to sleeping state.
    @param: mode= int flag of OS power mode
    @return:
    """

    mode_dict = {
        "ES_AWAYMODE_REQUIRED": "0x00000040",
        "ES_CONTINUOUS": "0x80000000",
        "ES_DISPLAY_REQUIRED": "0x00000002",
        "ES_SYSTEM_REQUIRED": "0x00000001",
        "ES_USER_PRESENT": "0x00000004"
    }

    def mode_selection(mode_options: dict) -> str:
        return ' | '.join(mode_options)

    # Mode selection by params:
    if mode is True:
        mode_options = dict({k: mode_dict[k] for k in ['ES_CONTINUOUS', 'ES_SYSTEM_REQUIRED', 'ES_AWAYMODE_REQUIRED', 'ES_DISPLAY_REQUIRED']})
    else:
        mode_options = dict({k: mode_dict[k] for k in ['ES_CONTINUOUS']})

    print(time.time_ns())
    # @ Television recording is beginning.Enable away mode and prevent
    # @ the sleep idle time - out.
    # @ Clear EXECUTION_STATE flags to disable away mode and allow the system to idle to sleep normally.
    # @ Wait  until  recording is complete...
    ctypes.windll.kernel32.SetThreadExecutionState(mode_selection(mode_options))
    time.sleep(5)
    print(time.time_ns())
