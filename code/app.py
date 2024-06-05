import unicodedata

# STEP 0.
# Encode characters in bytes

text_input:str=input("Please insert text that shouldbe converted to QR Code:\n> ")

def analyze_input(text_input=text_input):
    
# Encode unicode characters to binary
    analyzed_text:list=list()

    for character in text_input:
        binary:str=bin(ord(character))[2:]

        # make it in packets of 8 bits

        analyzed_text.append({character:binary})

    return(analyzed_text)

# STEP 1.
# Create data segment

# STEP 2.
# Fit to version number

# STEP 3.
# Concatenate segments, add padding, make codewords

# STEP 4.
# Split blocks, add ECC, interleave

# STEP 5.
# Draw fixed patterns

# STEP 6.
# Draw codewords and remainder

# STEP 7.
# Try applying the masks

# STEP 8.
# Find penalty patterns

# STEP 9.
# Calculate penalty points, select best mask

# QR code could be displayed in terminal using # and SPACE



# Zig-zag pattern for generating the QR code is starting from bottom 
# right towards top and then to the left

if __name__ == "__main__":
    print(analyze_input())