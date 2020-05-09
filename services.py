import psutil


# This function retrieve all running processes in sys in
def get_dict_of_process():
    process_dict = {p.pid: p.info for p in psutil.process_iter(['name'])}
    process_dict = {key: process_dict.get(key).get('name') for key in process_dict}
    return process_dict


# This function print all process in system
def print_dict_of_process():
    process_dict = get_dict_of_process()
    print(process_dict)


if __name__ == "__main__":
    print_dict_of_process()
