class Contact:
    name='Jane'

def hello(name:str) -> str:
    return 'Hello: ' + name

def hello_contact(contact:Contact)-> str:
    return 'Hello: ' + contact.name

M=Contact

val=hello(Contact.name)
print(val)

print(  hello_contact(M) )
