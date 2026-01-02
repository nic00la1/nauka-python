import os 
import shutil

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane ńćśłó")
fh.close()

# Zmiana nazwy pliku
if not os.path.exists(scriptDir + "/newTest.txt"):
    os.rename(scriptDir + "/test.txt" , scriptDir + "/newTest.txt")

print(os.path.getsize(scriptDir + "/newTest.txt")) # ilość bajtów (wielkość pliku)

print(os.path.isfile(scriptDir + "/newTest.txt"))  
print(os.path.isdir(scriptDir + "/newTest.txt"))
print(os.path.isdir("./basics"))

# usunięcie katalogu
if os.path.exists(scriptDir + "/subDir"):
    os.rmdir(scriptDir + "/subDir")

# tworzenie nowego katalogu
if not os.path.exists(scriptDir + "/subDir"):
    os.mkdir(scriptDir + "/subDir")

# usunięcie pliku tekstowego newTest.txt
if os.path.exists(scriptDir + "/newTest.txt"):
    os.remove(scriptDir + "/newTest.txt")


# Zmiana current working directory (katalogu)
print("Current working dir: ", os.getcwd())
os.chdir(scriptDir)
print("Current working dir: ", os.getcwd())


# kopia pliku
if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat", "data-copy.dat") # plik źródłowy + plik docelowy