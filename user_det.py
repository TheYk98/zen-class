import cryptography as kryp
from Crypto.Cipher import AES
import base64
file=open('user.txt','w')

usr=input("enter username")
passw=input("enter password")

file.write("uername:"+usr+" ")

'''
secret_key = '1234567890123456' 
cipher = AES.new(secret_key,AES.MODE_ECB) 
encoded = base64.b64encode(cipher.encrypt(passw))
'''

file.write("password:"+passw+"\n")
file.close()
file2=open('user.txt','r')
for i in file2:
    print(i)
file2.close()
#Why tho?