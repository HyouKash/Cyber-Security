def chiffre(message, masque):
    new_message = []
    for i in range(len(message)):
        a = message[i]
        b = masque[i]
        new_message.append(ord(a)^ord(b))
    return new_message

def dechiffre(message_chiffre, masque):
    new_message = []
    for i in range(len(message_chiffre)):
        a = message_chiffre[i]
        b = masque[i]
        new_message.append(chr(a^ord(b)))
    return new_message
        
print(chiffre("Salut ca va", "AMASQUEVERYLONGBUTITSNORMAL"))
print(dechiffre("[16, 36, 56, 33, 49, 112, 175, 51, 97, 37, 36]", "AMASQUEVERYLONGBUTITSNORMAL"))