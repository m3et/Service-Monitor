import os
from os import path

from log_security import hashFile, checkSum

service_checksum = hashFile('Logs/serviceList.txt')
log_checksum = hashFile('Logs/statusLog.txt')


def update_hashfile():
    global service_checksum
    global log_checksum
    service_checksum = hashFile('Logs/serviceList.txt')
    log_checksum = hashFile('Logs/statusLog.txt')


def print_to_serviceList(line):
    file_path = 'Logs/serviceList.txt'
    if checkSum(file_path,service_checksum):
        __print_to_log(file_path, line)
        update_hashfile()
    else:
        raise ValueError('Log file' + file_path + 'was touched')


def print_to_statusLog(line):
    file_path = 'Logs/statusLog.txt'
    if checkSum(file_path, log_checksum):
        __print_to_log(file_path, line)
        update_hashfile()
    else:
        raise ValueError('Log file' + file_path + 'was touched')


# This function write to the top of a given log file a given input
def __print_to_log(file_name, line):
    if not path.exists(file_name):
        __append_print_to_log(file_name, line)

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
    # close the files
    read_obj.close()
    write_obj.close()


# This function append to a given log file a given input
def __append_print_to_log(file_name, line):
    with open(file_name, 'a') as write_obj:
        write_obj.write(line + '\n')
    write_obj.close()
