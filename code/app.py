import reedsolo

class userInput:
    def __init__(self, text_input:str=None):
        
        if text_input is None:
            self.text_input=input('Please insert text that should be\
converted to QR Code (max 17 characters):\n> ')
            if len(self.text_input) > 17:
                raise Exception('Sorry, no more characters than 17.')
        else:
            self.text_input=text_input

    # As of now only byte encoding will be used
    def analyze_input(self, encoding_type:str='byte'):
        analyzed_text:list=list()

        # Encode unicode characters to binary
        for character in self.text_input:
            binary:str=bin(ord(character))[2:]

            # Make it in packets of 8 bits
            while len(binary) < 8:
                binary='0'+binary

            analyzed_text.append({character:binary})

        return analyzed_text

    def input_to_data_bits(self, method_input=analyze_input):
        input_bits=method_input(self)
        data_bits:str=''

        for character in input_bits:
            for bit in character.values():
                data_bits+=bit

        return data_bits

class layout:
    def __init__(self, size:int=21):
        self.size=size 

        # Size is depending on a QR Code version - for simplicity now I
        # will only use version 1 that is 21 x 21
        
    # Function to check if argument is callable
    def is_callable(self, method_input):
        if callable(method_input):
            structure=method_input(self)
        else:
            structure=method_input

        return structure
    
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
        structure=self.is_callable(method_input=method_input)
        
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
        structure=self.is_callable(method_input=method_input)
            
        # Dictionary is used to prevent multiple for loop blocks
        for name, pattern in finding_patterns.items():
            for row in range(len(pattern)):
                for column in range(len(pattern[0])):
                    structure[row-len(pattern) if name =='bottom_left'
                                    else row][column-len(pattern)
                                    if name=='top_right'
                                    else column]=pattern[row][column]

        return structure
    
    def draw_dummy_format_bits(self, method_input=generate_boundaries):
        # Check due to passing method as argument
        structure=self.is_callable(method_input=method_input)

        for i in range(9):
            if i == 6:
                pass
            else:
                structure[8][i]=' '
                structure[i][8]=' '
        
        for i in range(9):
            structure[-i][8]=' '
            structure[8][-i]=' '
        
        structure[-8][8]='#'

        return structure

    # Combine the whole layout of QR Code before adding meaningful data
    # to it
    def combine_qr_code_layout(self):
        combined=self.generate_boundaries()
        self.draw_timing_pattern(combined)
        self.draw_finding_pattern(combined)
        self.draw_dummy_format_bits(combined)

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


class qrCode(userInput):
    def __init__(self, text_input:str=None, encoding_type:str='byte', size:int=21, ecc_level='low'):
        super().__init__(text_input=text_input)
        self.encoding_type=encoding_type
        self.size=size
        self.character_count:int=len(self.analyze_input(
            encoding_type=encoding_type
        ))
        self.ecc_level=ecc_level

        # Get data from user input and add to it the encoding bits and count
    def concatenate_data(self, encoding_type:str='byte'):
        encoding_type_dict:dict={
            'numeric': '0001',
            'alphanumeric': '0010',
            'byte': '0100',
            'kanji': '1000'
        }

        character_count_binary:str=str(bin(self.character_count))[2:]
        while len(character_count_binary) < 8:
            character_count_binary='0'+character_count_binary
        
        terminator:str='0000'

        # Padding is alternating EC and 11 hexadecimals to fill out the 
        # QR Code if there is less than max characters.
        # 0xEC = 11101100
        # 0x11 = 00010001
        padding_list:list=['11101100', '00010001']
        padding:str=''
        if self.character_count < 17:
            for i in range(17-self.character_count):
                padding:str=padding+padding_list[i%2]

        concat:str=encoding_type_dict[encoding_type]+character_count_binary+self.input_to_data_bits()+terminator+padding

        return concat

    def split_blocks(self):
        binary_string_data:str=self.concatenate_data()

        # Split blocks to bytes (8 bits)
        n=8
        binary_codewords:list=[]
        hexadecimal_codewords:list=[]
        for i in range(round(len(binary_string_data)/n)):
            binary_codewords.append(binary_string_data[:n])
            binary_string_data=binary_string_data[n:]

        for codeword in binary_codewords:
            hexadecimal_codewords.append(hex(int(codeword, 2)))

        return hexadecimal_codewords

    # Use library with Reed-Solomon error correction codes.
    def error_correction(self):
        ecc_levels:dict={
            'low':0.07, # 7%
            'medium':0.15, # 15%
            'quartile':0.25, # 25%
            'high':0.30 # 30%
        }

        codewords:list=self.split_blocks()
        hexadecimal_string:str=''
        for codeword in codewords:
            if len(codeword[2:])<2:
                hexadecimal_string+=' 0'+codeword[2:].upper()
            else:
                hexadecimal_string+=' '+codeword[2:].upper()

        hexadecimal_string=hexadecimal_string[1:]

        rsc=reedsolo.RSCodec(7) # This depends on a qr code version
        encoded_message=rsc.encode(bytearray.fromhex(hexadecimal_string))
        decimal_ecc=list(encoded_message)[len(hexadecimal_string.split()):]
        hexadecimal_ecc = [hex(x) for x in decimal_ecc]

        return hexadecimal_ecc

    def add_ecc_to_concatenated_data(self):
        concat=self.concatenate_data()
        hexadecimal_ecc=self.error_correction()
        # binary_ecc=[bin(x) for x in hexadecimal_ecc]
        binary_ecc=''
        
        for i in hexadecimal_ecc:
            byte_size_binary=bin(int(i, 16))[2:]
            while len(byte_size_binary) < 8:
                byte_size_binary='0'+byte_size_binary
            
            binary_ecc+=byte_size_binary

        concat+=str(binary_ecc)

        return concat

    def zig_zag_pattern(self):
        zig_zag:list=[]
        boundaries=layout(size=self.size).combine_qr_code_layout()

        def direction_pattern(column:int, direction:str):
            directions:dict={
                'up': range(self.size-1, -1, -1),
                'down': range(self.size)
            }
            
            for row in directions[direction]:
                if boundaries[row][column]=='@':
                    zig_zag.append((row, column))
                if boundaries[row][column-1]=='@':
                    zig_zag.append((row, column-1))

        direction='up'
        for column in range(self.size-1, -1, -2):
            if column<=0:
                continue
            elif column<=6:
                column=column-1
            
            direction_pattern(column, direction)

            direction='down' if direction=='up' else 'up'

        return zig_zag

    # Draw concatenated data with needed bits to the QR Code
    def draw_data(self):
        drawing=layout(size=self.size).combine_qr_code_layout()
        data=self.add_ecc_to_concatenated_data()
        zig_zag=self.zig_zag_pattern()

        for (i,j) in zig_zag:
            drawing[i][j]=' ' if data[0]=='0' else '#'
            data=data[1:] 

        return drawing
    
    def masking_bool(self, i:int, j:int, masking_pattern:str):
        # Masking patterns
        # i - horizontal
        # j - vertical
        masking_patterns:dict={
            '000': (i+j)%2==0,
            '001': i%2==0,
            '010': j%3==0,
            '100': (i+j)%3==0,
            '011': (int(i/2) + int(j/3))%2==0,
            '101': (i*j)%2+(i*j)%3==0,
            '110': ((i*j)%3+i*j)%2==0,
            '111': ((i*j)%3+i+j)%2==0
        }

        return masking_patterns[masking_pattern]
    
    # Get all mask templates under this function and apply every mask to
    # generated QR Code
    # Calculate which mask is most beneficial and select it
    def apply_masking_to_data(self, masking_pattern:str):
        # Masking patterns
        # i - horizontal
        # j - vertical

        zig_zag_pattern=self.zig_zag_pattern()
        masking:dict={}
        data=self.draw_data()
        masked_data:list=data

        # Masking data
        for coordinates in zig_zag_pattern:
            bool=self.masking_bool(i=coordinates[0], j=coordinates[1],
                              masking_pattern=masking_pattern)
            masking[coordinates]=bool

        for coordinates, bool in masking.items():
            if bool==True:
                if masked_data[coordinates[0]][coordinates[1]]=='#':
                    masked_data[coordinates[0]][coordinates[1]]=' '
                elif masked_data[coordinates[0]][coordinates[1]]==' ':
                    masked_data[coordinates[0]][coordinates[1]]='#'

        return masked_data
    
    # Add to the QR Code format bits:
    # ECC Level, Masking, ECC for masking
    def generate_format_bits(self, masking_pattern:str):
        ecc_encoding:dict={
            'low': '01',
            'medium': '00',
            'quartile': '11',
            'high': '10'
        }
        generator_polynominal='10100110111'
        concat:str=ecc_encoding[self.ecc_level]+masking_pattern
        format_bits_list:list=[]

        # while len(concat)<15:
        #     concat=concat+'0'

        concat='011000000000000'
        while concat[0]=='0':
            concat=concat[1:]

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

        elo=int(concat, 2)^int(generator_polynominal, 2)
        

        return bin(elo)[2:]
    

    def draw_format_bits(self):
        ...


    # Apply the best mask
    def draw_masking(self):
        ...

    # Present final QR Code in Version 1
    def print_qr_code(self):
        # combined=self.apply_masking_to_data(masking_pattern='000')
        # qr_code:str=''
        # for row in range(len(combined)):
        #     for column in combined[row]:
        #         qr_code=qr_code+' '+column
        #     qr_code=qr_code+'\n'     

        # print(qr_code)
        ...
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
    print(qrCode(text_input='Hello, world! 123').generate_format_bits(masking_pattern='000'))