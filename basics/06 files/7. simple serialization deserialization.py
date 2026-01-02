import os 
import pickle

scriptDir = os.path.dirname(__file__)

number = 1234567
listData = ["Ania", "Ola", "Kasia", 12345]
strData = "Test ąśćłó"

fh = open(scriptDir + "/data.dat", "wb") # wb = write binary
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()


fh = open(scriptDir + "/data.dat", "rb") # rb = read binary
numerInfo = pickle.load(fh)
listInfo = pickle.load(fh)
strInfo = pickle.load(fh)
fh.close()

print(numerInfo)
print(listInfo)
print(strInfo)