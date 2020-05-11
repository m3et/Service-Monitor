import subprocess
from builtins import print

import psutil
from platform import system


# This function retrieve all running processes in sys in
def services_linux():
    output = subprocess.check_output(["service", "--status-all"])
    service_list = list()
    for line in output.split('\n'.encode(encoding='UTF-8')):
        string = str(line)
        service_name = string[10:- 1]
        service_list.append(service_name)

    service_dict = {p.pid: p.name() for p in psutil.process_iter(['name']) if p.info['name'] in service_list}
    return service_dict


def processes_dict():
    process_dict = {p.pid: p.info for p in psutil.process_iter(['name'])}
    process_dict = {key: process_dict.get(key).get('name') for key in process_dict}
    return process_dict


def services_win():
    service_dict = [s for s in psutil.win_service_iter()]
    service_dict = {s.pid(): s.name() for s in service_dict}
    return service_dict


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
