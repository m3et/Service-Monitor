import logs
import services

serviceList = 'serviceList.txt'
statusLog = 'statusLog.txt'


def updates_log():
    proc = services.list_of_process()
    proc = logs.add_timestamp(proc)
    logs.print_to_file(serviceList, proc)
    # print('Updates Logs\n' + proc)


if __name__ == "__main__":
    for i in range(3):
        updates_log()


def ask_for_time():
    return float(input("Enter desire second between samples"))
