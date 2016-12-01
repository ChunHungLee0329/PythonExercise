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

#Sinature
with open('master-private.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	signer = Signature_pkcs1_v1_5.new(rsakey)
	digest = SHA.new()
	digest.update(strPlainText)
	sign = signer.sign(digest)
	signature = base64.b64encode(sign)
	print "Signature: %s" % signature

#Verify
with open('master-public.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	verifier = Signature_pkcs1_v1_5.new(rsakey)
	digest = SHA.new()
	digest.update(strPlainText)
	is_verify = signer.verify(digest, base64.b64decode(signature))
	print "Verify status: %s" % is_verify
