
import time
start = time.time()

#Code to be timed
time.sleep(2) #Simulating a time-consuming task

end = time.time()
print(f'Time taken: {round(end - start, 2)} seconds')