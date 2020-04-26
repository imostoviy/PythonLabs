#Зашифровать заданную строку:
#по принципу «Азбуки Морзе»;
# Ihor Mostoviy
#25.04.2020

morseDict = { 'A':'._',
              'B':'_...',
              'C':'_._.',
              'D':'_..',
              'E':'.',
              'F':'.._.', 
              'G':'__.', 
              'H':'....', 
              'I':'..', 
              'J':'.___', 
              'K':'_._', 
              'L':'._..', 
              'M':'__', 
              'N':'_.', 
              'O':'___', 
              'P':'.__.', 
              'Q':'__._', 
              'R':'._.', 
              'S':'...', 
              'T':'_', 
              'U':'.._', 
              'V':'..._', 
              'W':'.__', 
              'X':'_.._', 
              'Y':'_.__', 
              'Z':'__..', 
              '1':'.____', 
              '2':'..___', 
              '3':'...__', 
              '4':'...._', 
              '5':'.....', 
              '6':'_....', 
              '7':'__...', 
              '8':'___..', 
              '9':'____.', 
              '0':'_____', 
              ', ':'__..__', 
              '.':'._._._', 
              '?':'..__..', 
              '/':'_.._.', 
              '_':'_...._', 
              '(':'_.__.', 
              ')':'_.__._' }
            
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += morseDict[letter] + ' '
        else: 
            cipher += ' '
  
    return cipher 

def decrypt(message): 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(morseDict.keys())[list(morseDict.values()).index(citext)] 
                citext = '' 
  
    return decipher 

def main():
    string = input("Enter message\n").upper()
    encripted = encrypt(string)
    print(encripted, "\n")

    decrypted = decrypt(encripted).lower()
    print(decrypted)

    return None

main()