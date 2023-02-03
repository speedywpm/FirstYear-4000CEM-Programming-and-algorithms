import pickle
f = open("DataStore.txt", "rb")
x = pickle.load(f)
y = pickle.load(f)
z = pickle.load(f)
f.close()
print(x,y,z)
