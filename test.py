
def sayHello(fname, lname):
    return 'hello ' + fname + " " + lname;
print(sayHello('john', 'doe'))

def hidePassword(password):
    return len(password) * '*';
password = "hidemypasswordplease"
print(hidePassword(password))
