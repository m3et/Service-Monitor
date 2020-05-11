import json
from datetime import datetime, timedelta
from log_security import hashFile, checkSum
import logs


def ascii_atr():
    print("""\

     .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
    | | ____    ____ | || |      __      | || | ____  _____  | || | _____  _____ | || |  _________   | || |   _____      | | | | ____    ____ | || |     ____     | || |  ________    | || |  _________   | |
    | ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | || ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | | | ||_   \  /   _|| || |   .'    `.   | || | |_   ___ `.  | || | |_   ___  |  | |
    | |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | || |  | |    | |  | || |   | |_  \_|  | || |    | |       | | | |  |   \/   |  | || |  /  .--.  \  | || |   | |   `. \ | || |   | |_  \_|  | |
    | |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | || |  | '    ' |  | || |   |  _|  _   | || |    | |   _   | | | |  | |\  /| |  | || |  | |    | |  | || |   | |    | | | || |   |  _|  _   | |
    | | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | || |   \ `--' /   | || |  _| |___/ |  | || |   _| |__/ |  | | | | _| |_\/_| |_ | || |  \  `--'  /  | || |  _| |___.' / | || |  _| |___/ |  | |
    | ||_____||_____|| || ||____|  |____|| || ||_____|\____| | || |    `.__.'    | || | |_________|  | || |  |________|  | | | ||_____||_____|| || |   `.____.'   | || | |________.'  | || | |_________|  | |
    | |              | || |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' 
                            """)


def ask_for_time_samples():
    start = input("Enter first timestamp in '%Y-%m-%d %H:%M:%S' format\n")
    end = input("Enter first timestamp in '%Y-%m-%d %H:%M:%S' format\n")
    return start, end


def load(start, end):
    datetime_accuracy = timedelta(seconds=2)
    datetime_start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    datetime_end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

    log_dict1 = dict()
    log_dict2 = dict()
    # check integrity of log file
    file_path = 'Logs/serviceList.txt'
    if not checkSum(file_path, logs.service_checksum):
        raise ValueError('Log file' + file_path + 'was touched')

    with open('Logs/serviceList.txt', 'r') as f:
        for line in f:
            datetime_sample = datetime.strptime(line[2:21], '%Y-%m-%d %H:%M:%S')
            if abs(datetime_start - datetime_sample) < datetime_accuracy:
                log_dict1 = json.loads(line)
                log_dict1 = log_dict1.get(str(datetime_sample))

            if abs(datetime_end - datetime_sample) < datetime_accuracy:
                log_dict2 = json.loads(line)
                log_dict2 = log_dict2.get(str(datetime_sample))
        f.close()

    if not bool(log_dict1):
        raise ValueError('No corresponding sample in time range', str(datetime_start))
    if not bool(log_dict2):
        raise ValueError('No corresponding sample in time range', str(datetime_start))

    return log_dict1, log_dict2


def diff(log_dict1, log_dict2):
    new_process_dict = log_dict1
    old_process_dict = log_dict2

    process_dead_dict = {k: old_process_dict[k] for k in set(old_process_dict) - set(new_process_dict)}
    process_born_dict = {k: new_process_dict[k] for k in set(new_process_dict) - set(old_process_dict)}

    return process_born_dict, process_dead_dict


def print_diff(process_born_dict, process_dead_dict):
    output = 'New Process in system: '
    if len(process_born_dict) == 0:
        output += 'No new process\n'
    else:
        output += str(process_born_dict) + '\n'

    output += 'closed Process in system: '
    if len(process_dead_dict) == 0:
        output += 'No closed process\n'
    else:
        output += str(process_dead_dict) + '\n'
    return output


def manuel_mode_test():
    ascii_atr()
    log_dict1, log_dict2 = load(start='2020-05-09 23:00:56', end='2020-05-09 23:00:51')
    log_dict1, log_dict2 = diff(log_dict1, log_dict2)
    print(print_diff(log_dict1, log_dict2))


def manuel_mode():
    ascii_atr()
    start, end = ask_for_time_samples()
    log_dict1, log_dict2 = load(start, end)
    log_dict1, log_dict2 = diff(log_dict1, log_dict2)
    print(print_diff(log_dict1, log_dict2))


if __name__ == "__main__":
    manuel_mode()
