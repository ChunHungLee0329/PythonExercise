#Caesar Cipher logic 
#A=D, B=E, C=F...

strPlaitText="" 
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

strPlaitText = "Neil (Chun-Hung) Lee"
print "PlainText: %s" % strPlaitText
print "Encrypt to CipherText(Caesar Cipher Encoding): %s" % caesarEncode(strPlaitText, intKey)
print "Decrypt to PlainText(Caesar Cipher Decoding): %s" % caesarDecode(caesarEncode(strPlaitText, intKey), intKey)