import platform
from modules.errorsHandler import errorsHandler

def detect_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "win"
    elif os_name == "Linux":
        return "lin"
    elif os_name == "Darwin":
        return "mac"
    else:
        return "nieznany"

print(detect_os())
