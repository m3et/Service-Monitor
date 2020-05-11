import time
import log_thread
import manuel_mode


def monitor_mode():
    interval = ask_for_time()
    thread = log_thread.ThreadingLog(interval)
    print("Monitor mode is running in background,type '2' to go into Manuel mode ,type '0' to close at anytime\n")
    while True:
        res = input('\n')
        if res == '0':
            print("exit program")
            return
        elif res == '2':
            thread.stop_print()
            manuel_mode.manuel_mode()
            thread.resume_print()

        # time.sleep(secs=3)


def ask_for_time():
    return int(input("Enter desire second between samples\n"))


if __name__ == "__main__":
    monitor_mode()
