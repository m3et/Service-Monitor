import services
import logs
import json
import threading
import time
from datetime import datetime


def time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class ThreadingLog(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=5):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.process_dict = services.get_dict_of_process()
        self.process_born_dict = {}
        self.process_dead_dict = {}
        self.counter = 0
        self.print = True

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Demonize thread
        thread.start()  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Log list of process running in sys
            service_list = {time_now(): self.process_dict}
            service_list_log = json.dumps(service_list)
            logs.print_to_serviceList(service_list_log)

            # Lod difference between lat log
            if self.counter != 0:
                self.diff()
                statusLog_log = self.statusLog_str()
                if self.print:
                    print(statusLog_log)
                logs.print_to_statusLog(statusLog_log)

            self.counter += 1
            time.sleep(self.interval)

    def update_process_dict(self):
        self.process_dict = services.get_dict_of_process()
        return self.process_dict

    def diff(self):
        old_process_dict = self.process_dict
        new_process_dict = self.update_process_dict()

        self.process_dead_dict = {k: old_process_dict[k] for k in set(old_process_dict) - set(new_process_dict)}
        self.process_born_dict = {k: new_process_dict[k] for k in set(new_process_dict) - set(old_process_dict)}

    def statusLog_str(self):
        output = time_now() + '\n'
        output += 'New Process in system: '
        if len(self.process_born_dict) == 0:
            output += 'No new process\n'
        else:
            output += str(self.process_born_dict) + '\n'

        output += 'closed Process in system: '
        if len(self.process_dead_dict) == 0:
            output += 'No closed process\n'
        else:
            output += str(self.process_dead_dict) + '\n'
        return output

    def stop_print(self):
        self.print = False

    def resume_print(self):
        self.print = True


if __name__ == "__main__":
    example = ThreadingLog()
    while True:
        # print('main')
        time.sleep(5)
