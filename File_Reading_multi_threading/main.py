import threading
import time

class FileReaderThread(threading.Thread):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                print(line.strip())
                time.sleep(0.1)

def main():
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']

    threads = []
    for file_name in file_names:
        thread = FileReaderThread(file_name)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
