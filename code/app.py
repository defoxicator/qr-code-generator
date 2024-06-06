import unicodedata

# STEP 0.
# Encode characters in bytes

# STEP 1.
# Create data segment

class Input:
    def __init__(self):
        self.text_input:str=input('Please insert text that shouldbe converted to QR Code:\n> ')
        
    def analyze_input(self):
        
# Encode unicode characters to binary
        analyzed_text:list=list()

        for character in self.text_input:
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
                self.row_boundaries.append('@')
                        
            self.boundaries.append(self.row_boundaries)

# Timing pattern
# Row 6, column 6
    def draw_timing_pattern(self):
# Row timing pattern
        self.row_timing:list=[]
        for i in range(len(self.boundaries[5])):
            if i%2==0:
                self.row_timing.append('#')
            else:
                self.row_timing.append(' ')

        self.row_timing.reverse()
        self.boundaries[6]=self.row_timing

# Column timing pattern
        self.col_timing:list=[]
        for i in range(len(self.boundaries[5])):
            if i%2==0:
                self.col_timing.append('#')
            else:
                self.col_timing.append(' ')

        for i in range(len(self.boundaries)):
            self.boundaries[i][6]=self.col_timing[i]

    def one_finding_pattern(self, side:str)->list:
        self.finding_pattern:list=[
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],            
            ['#', '#', '#', '#', '#', '#', '#']
        ]

        self.padding:list=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        if side=='top_left':
            for i in range(len(self.finding_pattern)):
                self.finding_pattern[i].append(self.padding[i])
            self.finding_pattern.insert(len(self.finding_pattern), self.padding)
        elif side=='top_right':
            for i in range(len(self.finding_pattern)):
                self.finding_pattern[-i].append(self.padding[i])
            self.finding_pattern.insert(len(self.finding_pattern), self.padding)
        elif side=='bottom_left':
            for i in range(len(self.finding_pattern)):
                self.finding_pattern[i].append(self.padding[i])
            self.finding_pattern.insert(0, self.padding)

        return self.finding_pattern
    
# Combine finding patterns
    def draw_finding_pattern(self):
        print('top_left\n',self.one_finding_pattern(side='top_left'))
        print('top_right\n',self.one_finding_pattern(side='top_right'))
        print('bottom_left\n',self.one_finding_pattern(side='bottom_left'))
             

    def print_qr_code(self):
        self.draw_timing_pattern()
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

if __name__ == '__main__':
    QrCode().draw_finding_pattern()