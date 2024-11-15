
import string
encode=list(input("Enter message to Decode : "))
crib=list(input("Enter your CRIB(for eg. x.-x.-x.-) : "))
dash=[]
space=[]
dot=[]
for i in range(0,len(crib)):
    if crib[i]=="x":
        space.append(str(i))
    elif crib[i]==".":
        dot.append(str(i))
    elif crib[i]=="-" or "_":
        dash.append(str(i))    

print(dash)
print(space)
print(dot)
Flag=[]

for i in range(0,len(encode)):
    if encode[i] in dash:
        Flag.append("-")
    elif encode[i] in dot:
        Flag.append(".")
    elif encode[i] in space:
        Flag.append(" ") 
    else:
        Flag.append(" "+encode[i]+" ")  

morse="".join(Flag)
print(morse)

# Dictionary mapping Morse code to ASCII letters
morse_to_ascii = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9','{': '{','}':'}','_':'_'
}

def morse_to_text(morse_code):
    # Split the input into words (separated by " / ") and letters (separated by spaces)
    words = morse_code.split(' / ')  # Morse code uses ' / ' to separate words
    decoded_message = []
    
    for word in words:
        # Decode each word by decoding each letter
        letters = word.split()  # Split letters by space
        decoded_word = ''.join(morse_to_ascii[letter] for letter in letters)
        decoded_message.append(decoded_word)
    
    # Join the words with spaces to form the full message
    return ' '.join(decoded_message)

# Example usage
morse_input = "... --- ..."  # SOS in morse code
decoded_text = morse_to_text(morse)
print("Decoded text:", decoded_text)
