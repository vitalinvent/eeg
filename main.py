import serial
import time
import matplotlib.pyplot as plt

start = time.time()
bufferSize = 50
x = [0]*bufferSize
y = [0]*bufferSize
xi = 0
# x = []
# y = []

ser = serial.Serial('COM3')
time.sleep(2)
fig = plt.figure()
plt.ion()  # turn on interactive mode
fig.canvas.draw()
plt.show(block=False)

log_file = open("log.txt","a")

while True:
    num = int.from_bytes(ser.read(), "big")
    log_line=str(num)+"\n"
    log_file.write(log_line)
    end = time.time()
    # y.append(num)
    y[xi] = num
    time_elapsed= end - start
    # x.append(time_elapsed)
    x[xi] = xi
    # x[xi] = xi
    plt.cla()
    plt.plot(x, y, 'red')
    plt.pause(0.05)
    plt.draw()
    xi += 1
    if xi > bufferSize-1:
        xi = 0