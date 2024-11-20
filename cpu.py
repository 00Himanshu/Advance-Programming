#program to check number of cpu cores in a system 
import os
import multiprocessing
print("Number of CPU cores in system are: ",multiprocessing.cpu_count())