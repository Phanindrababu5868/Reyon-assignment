import multiprocessing
import time

def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())
            time.sleep(0.1)

def main():
    num_files = 2
    file_names = [f'sample{i}.txt' for i in range(1, num_files + 1)]

    processes = [multiprocessing.Process(target=read_file, args=(file_name,)) for file_name in file_names]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

