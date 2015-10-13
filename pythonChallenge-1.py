#!/usr/bin/env python

def incrementChar(oldChar, increment):
    charByte = ord(oldChar)
    if (charByte < 97 or charByte > 122 ) :
        return(oldChar)
    charByte += increment
    if (charByte > 122 ) :
        print("Debug: wrap around")
        charByte = charByte-26
    return chr(charByte)

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newSentence = []  


print("limits (a->z): "+str(ord('a'))+"->"+str(ord('z')))
for oldChar in sentence:
    newSentence.append(incrementChar(oldChar, 2))
    
print(''.join(newSentence))

