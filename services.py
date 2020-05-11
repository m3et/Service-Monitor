import subprocess

import psutil
from platform import system


# This function retrieve all running processes in sys in
def services_linux():
    output = subprocess.check_output(["service", "--status-all"])
    print(output)


def services_win():
    process_dict = [s for s in psutil.win_service_iter()]
    process_dict = {s.pid(): s.name() for s in process_dict}
    return process_dict


def get_dict_of_process():
    os = system()
    if os == 'Linux':
        return services_linux()
    elif os == 'Windows':
        return services_win()
    else:
        raise ValueError('OS id not supported')


# This function print all process in system
def print_dict_of_process():
    process_dict = get_dict_of_process()
    print(process_dict)


if __name__ == "__main__":
    services_linux()
