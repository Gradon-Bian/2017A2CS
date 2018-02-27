# Gradon Bian S3C5 Opt1
# 2018-02-26 Homework: Cars Project
# Save 5 car records to a file and load them out

import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID="BMW"
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00

##ThisCar=CarRecord()

Car=[CarRecord() for i in range (5)]

Car[0].EngineSize=1000
Car[1].EngineSize=2500
Car[2].EngineSize=2000
Car[3].EngineSize=2600
Car[4].EngineSize=3000
#print(Car[3].EngineSize)


CarFile=open('Cars.DAT','wb')


for i in range (5):
    pickle.dump(Car[i],CarFile)

CarFile.close()

CarFile=open('Cars.DAT','rb')
CarList=[]

#EOF=False

#while not EOF:
    #try:
        #CarList.append(pickle.load(CarFile))
    #except:
        #EOF=True

for i in range(5):
    CarList.append(pickle.load(CarFile))
       
CarFile.close()

print(CarList[1].EngineSize)

