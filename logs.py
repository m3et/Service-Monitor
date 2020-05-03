import os
from os import path
import datetime

serviceList = 'serviceList.txt'
statusLog = 'statusLog.txt'


def print_to_log(file_name, line):
    if not path.exists(file_name):
        append_print_to_log(file_name, line)

    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

    read_obj.close()
    write_obj.close()


def append_print_to_log(file_name, line):
    with open(file_name, 'a') as write_obj:
        write_obj.write(line + '\n')
    write_obj.close()


def add_timestamp(line):
    timestamp = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    line = timestamp + '\n' + line
    return line


if __name__ == "__main__":
    import services

    for i in range(3):
        proc = services.list_of_process()
        proc = add_timestamp(proc)
        print_to_log(serviceList, proc)
