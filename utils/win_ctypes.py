from ctypes import wintypes
import ctypes
"""
Get power status of the system using ctypes to call GetSystemPowerStatus
Documentation:
· https://stackoverflow.com/questions/6153860/in-python-how-can-i-detect-whether-the-computer-is-on-battery-power
"""


class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
GetSystemPowerStatus.restype = wintypes.BOOL

status = SYSTEM_POWER_STATUS()
if not GetSystemPowerStatus(ctypes.pointer(status)):
    raise ctypes.WinError()

print('ACLineStatus', status.ACLineStatus)
print('BatteryFlag', status.BatteryFlag)
print('BatteryLifePercent', status.BatteryLifePercent)
print('BatteryLifeTime', status.BatteryLifeTime)
print('BatteryFullLifeTime', status.BatteryFullLifeTime)