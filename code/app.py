import unicodedata

# STEP 0.
# Encode characters in bytes

# STEP 1.
# Create data segment

class Input:
    def __init__(self):
        self.text_input:str=input('Please insert text that should be\
                                  converted to QR Code:\n> ')
        
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

class qrCode:
    def __init__(self, size:tuple=(21,21)):
        # Size = (rows, columns)
        self.size=size 
        
    def generate_boundaries(self):
        self.boundaries:list=[]
        # Boundaries
        for col in range(self.size[0]):
            self.row_boundaries:list=[]

            for row in range(self.size[1]):
                self.row_boundaries.append('@')
                        
            self.boundaries.append(self.row_boundaries)
        
        return self.boundaries

        # Timing pattern
        # Row 6, column 6

    def timing_pattern(self, direction:str):
        self.row_timing:list=[]
        
        if direction=='row':
            length=self.size[0]
        elif direction=='column':
            length=self.size[1]

        for i in range(length):
            if i%2==0:
                self.row_timing.append('#')
            else:
                self.row_timing.append(' ')
        
        return self.row_timing

    def draw_timing_pattern(self):

        self.boundaries=self.generate_boundaries()
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

        return self.boundaries

    def one_finding_pattern(self, vertical:str, horizontal:str)->list:
        self.finding_pattern:list=[
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],            
            ['#', '#', '#', '#', '#', '#', '#']
        ]

        padding:list=[' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # Vertical padding        
        if vertical=='top':
            vertical_insert:int=len(self.finding_pattern)
        elif vertical=='bottom':
            vertical_insert:int=0

        self.finding_pattern.insert(vertical_insert, padding)

        # Horizontal padding
        if horizontal=='left':
            horizonal_insert:int=len(self.finding_pattern[0])
        elif horizontal=='right':
            horizonal_insert:int=0

        for i in range(len(self.finding_pattern)):
            self.finding_pattern[i].insert(horizonal_insert, padding[0])

        return self.finding_pattern
    
# Combine finding patterns
    def draw_finding_pattern(self):

        top_left=self.one_finding_pattern(vertical='top', horizontal='left')
        top_right=self.one_finding_pattern(vertical='top', horizontal='right')
        bottom_left=self.one_finding_pattern(vertical='bottom', horizontal='left')
        finding_patterns:dict={'top_left':top_left,
                               'top_right':top_right,
                               'bottom_left':bottom_left}

        for name, pattern in finding_patterns.items():
            for row in range(len(pattern)):
                for column in range(len(pattern[0])):
                    self.boundaries[row-len(pattern) if name =='bottom_left'
                                    else row][column-len(pattern)
                                    if name=='top_right'
                                    else column]=pattern[row][column]

    def combine_qr_code(self):
        self.generate_boundaries()
        self.draw_timing_pattern()
        self.draw_finding_pattern()

    def print_qr_code(self):
        qr_code:str=''
        self.draw_timing_pattern()
        self.draw_finding_pattern()
        for row in range(len(self.boundaries)):
            for column in self.boundaries[row]:
                qr_code=qr_code+' '+column
            qr_code=qr_code+'\n'     

        print(qr_code)           

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
    qrCode().timing_pattern()