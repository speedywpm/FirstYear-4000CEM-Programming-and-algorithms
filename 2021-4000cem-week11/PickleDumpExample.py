import pickle
f = open("DataStore.txt", "wb")
x = [1,2,3,4,5]
y = True
z = "Hello"
pickle.dump(x,f)
pickle.dump(y,f)
pickle.dump(z,f)
f.close()
