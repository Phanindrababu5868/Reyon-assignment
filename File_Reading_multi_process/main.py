import multiprocessing
import time

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())
            time.sleep(0.1)

def main():
    file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']  # Add more file names as needed

    processes = []
    for file_name in file_names:
        process = multiprocessing.Process(target=read_file, args=(file_name,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
