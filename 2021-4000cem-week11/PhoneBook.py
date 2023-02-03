myContacts = {
    "Ned Stark"         : 442477733900,
    "Jaime Lannister"   : 4424777131809,
    "Cersei Lannister"  : 442477850129,
    "Daenerys Targaryen": 440121533541,
    "Jon Snow"          : 442477697420,
}
myContacts["Bran Stark"]=myContacts["Jon Snow"]
myContacts["Jaime Lannister"]=myContacts["Cersei Lannister"]
del myContacts["Ned Stark"]



print(myContacts)