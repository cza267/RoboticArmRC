#import serial
import matplotlib.pyplot as plt
import numpy as np

i=0 
x=list()
y=list()

serialData = np.random.rand(10,10)

#serial info from sensor
#serialData =serial.Serial()

#Open and close serial for safety
#ser.close()
#ser.open()
print(serialData)



plt.matshow(serialData)
plt.colorbar()
plt.show()
'''
while True:
    #data=serialData.readline()
    #print(data.decode())
    pl
    print(data)
    x.append(i)
    #y.append(data.decode())
    y.append(data)

    plt.scatter(i, float(data))

    i+=1
    plt.show()
    plt.pause(0.0001)

'''

