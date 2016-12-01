from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

print '\n'

#Caesar function
def convert(strInput, intKey, strStart='a', n=26):
    temp = ord(strStart)
    offset = ((ord(strInput) - temp + intKey)%n)
    return chr(temp + offset)
def caesarEncode(strInput, intKey):
	strOutput = ""
	for temp in strInput:
		if temp.islower():
			strOutput += convert(temp, intKey, 'a', n=26)
		elif temp.isupper():
			strOutput += convert(temp, intKey, 'A', n=26)
		else:
			strOutput += temp
	return strOutput
def caesarDecode(strInput, intKey):
	return caesarEncode(strInput, -intKey)

#generate RSA pem file:public key & private key
random_generator = Random.new().read 
rsa = RSA.generate(1024, random_generator)
private_pem = rsa.exportKey()
with open('master-private.pem', 'w') as f:
    f.write(private_pem)
public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(public_pem)

#Set Caesar index Key	
strPlainText="" 
strCipherText=""
intKey = 3
print "Caesar index key(original): %s" % intKey

#encrypt CipherText=Caesar[PlainText]
strPlainText = "Neil (Chun-Hung) Lee"
strCipherText = caesarEncode(strPlainText, intKey)
print "CipherText is Caesar[PlainText]: %s" % strCipherText

#provide encrypt intKey RSA[intKey]
strPlainKey = str(intKey) 
with open('master-public.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	strCipherKey = base64.b64encode(cipher.encrypt(strPlainKey))
	print "CipherKey is Encryption RSA[intKey]: %s" % strCipherKey 
	print '\n'

#print Sender[Caesar(PlainText, RSA(Key)]
print "Sender[%s, %s]" % (strCipherText, strCipherKey)
print '\n'

#decrypt RSA[intKey]
with open('master-private.pem') as f:
	key = f.read()
	rsakey = RSA.importKey(key)
	cipher = Cipher_pkcs1_v1_5.new(rsakey)
	strPlainKey = str(cipher.decrypt(base64.b64decode(strCipherKey), random_generator))
	print "PlainKey is Decrypt RSA[intKey]: %s" % strPlainKey

#decrypt Caesar[CipherText]
print "PlainText is Decrypt Caesar[PlainText]: %s" % caesarDecode(strCipherText, int(strPlainKey))
