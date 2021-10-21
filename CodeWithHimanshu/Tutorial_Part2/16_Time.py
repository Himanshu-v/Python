import time

initialTime = time.time()
print("Started at", initialTime)
for i in range(1000):
    print("Executing")

print("Finished in", time.time()-initialTime)



