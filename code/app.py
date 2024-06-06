import unicodedata

# STEP 0.
# Encode characters in bytes

# STEP 1.
# Create data segment

class Input:
    def __init__(self):
        self.text_input:str=input("Please insert text that shouldbe converted to QR Code:\n> ")
        
    def analyze_input(self):
        
# Encode unicode characters to binary
        analyzed_text:list=list()

        for character in text_input:
            binary:str=bin(ord(character))[2:]

# Make it in packets of 8 bits
            while len(binary) < 8:
                binary='0'+binary

            analyzed_text.append({character:binary})

        return(analyzed_text)

# STEP 2.
# Fit to version number

class Version:
# Versions as dict like
# version_x_y:dict={number_of_bits:number_of_codewords}
    def __init__(self):
        version_1_9:dict={148:19}
        version_10_26:dict={156:20}
        version_27_40:dict={156:20}

# STEP 3.
# Concatenate segments, add padding, make codewords

# STEP 4.
# Split blocks, add ECC, interleave

# STEP 5.
# Draw fixed patterns

class QrCode:
    def __init__(self):
# Size in col, rows
        self.size=(21,21)
        self.boundaries:list=[]
    # Boundaries
        for col in range(self.size[0]):
            self.row_boundaries:list=[]

            for row in range(self.size[1]):
                self.row_boundaries.append("@")
                        
            self.boundaries.append(self.row_boundaries)

# Timing pattern
# Row 6, column 6
    def draw_timing_pattern(self):
        for row in self.size:
            pass

    def print_qr_code(self):
        for col in self.boundaries:
            print(col)


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
    QrCode().print_qr_code()