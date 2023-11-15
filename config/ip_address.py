# How to view a django project across other devices from your local computer - https://dev.to/codewitgabi/how-to-view-a-django-project-across-other-devices-from-your-local-computer-43eg

import socket

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return socket.gethostbyname(socket.gethostname())