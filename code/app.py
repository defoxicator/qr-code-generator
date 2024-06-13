import unicodedata

# STEP 0.
# Encode characters in bytes

# STEP 1.
# Create data segment

class userInput:
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

class layout:
    def __init__(self, size:int=21):
        self.size=size 
        
    def generate_boundaries(self):
        self.boundaries:list=[]
        
        # Set boundaries for the code
        for col in range(self.size):
            self.row_boundaries:list=[]

            for row in range(self.size):
                self.row_boundaries.append('@')
                        
            self.boundaries.append(self.row_boundaries)
        
        return self.boundaries

    # Prepare lists that will be used as timing pattern template
    def timing_pattern(self):
        self.row_timing:list=[]

        for i in range(self.size):
            if i%2==0:
                self.row_timing.append('#')
            else:
                self.row_timing.append(' ')
        
        return self.row_timing

    # Combine timing patterns from template
    def draw_timing_pattern(self, method_input=generate_boundaries):
        pattern_template=self.timing_pattern()
        
        # Check due to passing method as argument
        if callable(method_input):
            structure=method_input(self)
        else:
            structure=method_input
        
        # Drawing timing patterns using template
        for i in range(len(pattern_template)):
            structure[i][6]=pattern_template[i]
        
        structure[6]=pattern_template

        return structure

    # Create finding patterns, one for each corner
    def one_finding_pattern(self, vertical:str, horizontal:str)->list:
        # This part is not changing no matter the QR Code size, so
        # is being implemented as a predefined list
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
    def draw_finding_pattern(self, method_input=generate_boundaries):
        top_left=self.one_finding_pattern(vertical='top', horizontal='left')
        top_right=self.one_finding_pattern(vertical='top', horizontal='right')
        bottom_left=self.one_finding_pattern(vertical='bottom',
                                             horizontal='left')
        finding_patterns:dict={'top_left':top_left,
                               'top_right':top_right,
                               'bottom_left':bottom_left}

        # Check due to passing method as argument
        if callable(method_input):
            structure=method_input(self)
        else:
            structure=method_input
            
        # Dictionary is used to prevent multiple for loop blocks
        for name, pattern in finding_patterns.items():
            for row in range(len(pattern)):
                for column in range(len(pattern[0])):
                    structure[row-len(pattern) if name =='bottom_left'
                                    else row][column-len(pattern)
                                    if name=='top_right'
                                    else column]=pattern[row][column]

        return structure
    
    # Combine the whole layout of QR Code before adding meaningful data
    # to it
    def combine_qr_code_layout(self):
        combined=self.generate_boundaries()
        self.draw_timing_pattern(combined)
        self.draw_finding_pattern(combined)

        return combined

    # Print the empty QR Code
    def print_qr_code_layout(self):
        combined=self.combine_qr_code_layout()
        qr_code:str=''
        for row in range(len(combined)):
            for column in combined[row]:
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
    layout().print_qr_code_layout()