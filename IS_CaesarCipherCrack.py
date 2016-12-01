#Caesar Cipher logic 
#A=D, B=E, C=F...

strPlainText="" 
strCipherText=""

intKey=3
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

#define the PlainText & CipherText
strPlainText = "Welcome to Taiwan!"
strCipherText = caesarEncode(strPlainText, intKey)
print "Key: %s" % intKey
print "PlainText: %s" % strPlainText
print "CipherText: %s " % strCipherText
print '\n'

#1~26 is a key range, try all possible key
print "Caesar Crack All possible key below:"
for i in range(26):
	print "If key=%s then PlainText: %s" % (i+1,caesarDecode(strCipherText, i+1))
