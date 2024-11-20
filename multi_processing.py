import concurrent.futures
import time
from datetime import datetime
import multiprocessing

c=concurrent.futures

def func1():
    time.sleep(3)
    print("\nFunction 1 Complete " + datetime.now().strftime("%d/%m/%y %H:%M:%S"))

def func2():
    time.sleep(3)
    print("\nFunction 2 Complete " + datetime.now().strftime("%d/%m/%y %H:%M:%S"))

def func3():
    time.sleep(3)
    print("\nFunction 3 Complete " + datetime.now().strftime("%d/%m/%y %H:%M:%S"))

def main():
    # List of functions to execute
    functions = [func1, func2, func3]
    
    cores = multiprocessing.cpu_count()
    # Number of threads in the pool
    num_threads = cores

    # Using ThreadPoolExecutor to execute functions concurrently
    with c.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit each function to the thread pool
        futures = [executor.submit(func) for func in functions]

        # Wait for all threads to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
