#!/usr/bin/env python3.8
import datetime
import psutil


# This function retrieve all running processes in sys
def get_list_of_process():
    return psutil.process_iter(attrs=None, ad_value=None)


# This function print all process in system
def list_of_process():
    iterator = get_list_of_process()
    output = ''
    for process in iterator:
        try:
            # Get process name & pid from process object.
            processName = process.name()
            processID = process.pid
            processCreationTime = datetime.datetime.fromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            processCpuPercentage = process.cpu_percent()
            processMemoryPercentage = process.cpu_percent()
            output += processName + ' ::: ' + str(processID) + ' ::: ' + str(processCreationTime) + ' ::: ' + str(processCpuPercentage) + ' ::: ' + str(processMemoryPercentage) + '\n'
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    output = 'processName | processID | processCreationTime | processCpuPercentage | processMemoryPercentage\n' + output
    # print(output)
    return output


if __name__ == "__main__":
    list_of_process()
