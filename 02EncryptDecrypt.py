def encrypt(str,key):
	return key.join(str)
def decypt(str,key):
	return str.split(key)

msg=input('Enter a Message :')
key1=input('Enter Encryption Key :')
coded_msg=encrypt(msg,key1)
dec=decypt(coded_msg,key1)
actual_msg="".join(dec)
print('The Encrypted message is:',coded_msg)
print('String after Decryption is :',actual_msg)