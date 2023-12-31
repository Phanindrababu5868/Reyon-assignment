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
                time.sleep(0.2)

def main():
    num_files = 2  # You can adjust the number of files here
    file_names = [f'sample{i}.txt' for i in range(1, num_files + 1)]

    threads = [FileReaderThread(file_name) for file_name in file_names]

    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
