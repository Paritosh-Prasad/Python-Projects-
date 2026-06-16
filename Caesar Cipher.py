# Caesar cipher project no 04
# Caesar cipher is where each letter in the plaintext is shifted by a fixed number of positions(key) down the alphabet


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(text,skey) : # This is for encryption of text message
    ctext =""
    for char in text :
        if char in letters :
            pos = letters.index(char)
            npos = (pos + skey)%26
            ctext +=letters[npos]
        else :
            ctext += char
    print(f"Here is your ciphered text : {ctext}")


def decryption(text,skey) : # This is for decryption of text message
    ptext =""
    for char in text :
        if char in letters :
            pos = letters.index(char)
            npos = (pos -skey)%26
            ptext +=letters[npos]
        else :
            ptext += char
    print(f"Here is your plain text : {ptext}")

end = False

while not end :  # loop for user to use the program
    print("Type encrypt for encryption.\nType decrypt for decryption.")
    to_do= input("Enter what you want to do : ")
    skey = int(input(f"Enter the shift key for {to_do} process : "))

    text = input(f"enter the text you want to {to_do} : ").lower()

    if to_do =="encrypt" :
        encryption(text,skey)
    elif to_do =="decrypt" :
        decryption(text,skey)
    else :
        print("Enter valid command")
    again = input("Enter 'yes' to continue and 'no' to leave : ")
    if again == "no" :
        end = True
        print("Thankyou.\nGood bye")
    else :
        end = False
