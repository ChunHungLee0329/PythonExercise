from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

#Sender/Receiver know the value
random_generator = Random.new().read 
rsa = RSA.generate(1024, random_generator)

#Receiver create the own private key
private_pem = rsa.exportKey()
with open('master-private.pem', 'w') as f:
    f.write(private_pem)

#create a public key to all body who want to send the message to Receiver 
public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(public_pem)

#testing script
strPlainText = "88"
strCipherText = ""
strPlainText = str(strPlainText)
print "PlainText: %s" % strPlainText

#sending message with RSA public key 
with open('master-public.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	strCipherText = base64.b64encode(cipher.encrypt(strPlainText))
	print "ChiperText: %s" % strCipherText

#receiver message with RSA private key
with open('master-private.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	strPlainText = cipher.decrypt(base64.b64decode(strCipherText), random_generator)
	print "PlainText: %s" % strPlainText
