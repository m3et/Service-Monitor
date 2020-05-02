import datetime


serviceList = 'serviceList.txt'
statusLog = 'statusLog.txt'


def print_to_file(file_name, input):
    with open(file_name, 'a+') as write_obj:
        write_obj.write(input + '\n')
    write_obj.close()


def add_timestamp(input):
    timestamp = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    input = timestamp + '\n' + input
    return input


if __name__ == "__main__":
    import services

    for i in range(3):
        proc = services.list_of_process()
        proc = add_timestamp(proc)
        print_to_file(serviceList, proc)
