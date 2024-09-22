from Morse_Code import MORSE_CODE_DICT



def Morse_Code_Converser(text):
    code = ""
    for char in text.upper():
        code += MORSE_CODE_DICT.get(char) + " "
    return code


line=input("Enter the line you want to convert in to Morse Code: ")
print(f"Morse Code: {Morse_Code_Converser(line)}")