'''
Full application to generate the QR to terminal using # and SPACEs.
QR Code is generated using byte encoding in Version 1 of the QR Code.
'''
from collections import Counter
import reedsolo

class UserInput:
    '''
    This class is used to get the input from the user and encode it to
    binary format.
    '''
    def __init__(self, text_input:str=None):
        '''
        This method is initializing the class with user input.
        '''
        if text_input is None:
            self.text_input=input('Please insert text that should be\
converted to QR Code (max 17 characters):\n> ')
            if len(self.text_input) > 17:
                raise ValueError('Sorry, no more characters than 17.')
        else:
            self.text_input=text_input

    # As of now only byte encoding will be used
    def analyze_input(self, encoding_type:str='byte'):
        '''
        This method is analysing and encoding the input in byte format.
        '''
        analyzed_text:list=[]

        # Encode unicode characters to binary
        if encoding_type=='byte':
            for character in self.text_input:
                binary:str=bin(ord(character))[2:]

                # Make it in packets of 8 bits
                while len(binary) < 8:
                    binary='0'+binary

                analyzed_text.append({character:binary})

        return analyzed_text

    def input_to_data_bits(self, method_input=analyze_input):
        '''
        This method is putting analyzed input to binary string.
        '''
        input_bits=method_input(self)
        data_bits:str=''

        for character in input_bits:
            for bit in character.values():
                data_bits+=bit

        return data_bits

class Layout:
    '''
    This class is for generating the layout of the QR Code to be used
    later in the process of generating the QR Code.
    '''
    def __init__(self, size:int=21):
        '''
        This method is initializing the class with respective size of QR Code.
        '''
        self.size=size

        # Size is depending on a QR Code version - for simplicity now I
        # will only use version 1 that is 21 x 21

    # Function to check if argument is callable
    def _is_callable(self, method_input):
        '''
        This is a helper method to check if the argument is callable and
        if not then it is preparing it to run it.
        '''
        if callable(method_input):
            structure=method_input(self)
        else:
            structure=method_input

        return structure

    def generate_boundaries(self):
        '''
        This method is useed to generate the template to build the QR Code
        upon.
        '''
        boundaries:list=[]

        # Set boundaries for the code
        for _ in range(self.size):
            row_boundaries:list=[]

            for _ in range(self.size):
                row_boundaries.append('@')

            boundaries.append(row_boundaries)

        return boundaries

    # Prepare lists that will be used as timing pattern template
    def timing_pattern(self):
        '''
        This method is generating timing patterns for the QR Code.
        '''
        row_timing:list=[]

        for i in range(self.size):
            if i%2==0:
                row_timing.append('#')
            else:
                row_timing.append(' ')

        return row_timing

    # Combine timing patterns from template
    def draw_timing_pattern(self, method_input=generate_boundaries):
        '''
        This method is inserting timing patterns in the template.
        '''
        pattern_template=self.timing_pattern()

        # Check due to passing method as argument
        structure=self._is_callable(method_input=method_input)

        # Drawing timing patterns using template
        for (index, _) in enumerate(pattern_template):
            structure[index][6]=pattern_template[index]

        structure[6]=pattern_template

        return structure

    # Create finding patterns, one for each corner
    def _one_finding_pattern(self, vertical:str, horizontal:str)->list:
        '''
        This method is generating a finding pattern depending on its placement
        in QR Code.
        '''
        # This part is not changing no matter the QR Code size, so
        # is being implemented as a predefined list
        finding_pattern:list=[
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]
        padding:list=[' ', ' ', ' ', ' ', ' ', ' ', ' ']
        vertical_insert:int=None
        horizonal_insert:int=None

        # Vertical padding
        if vertical=='top':
            vertical_insert:int=len(finding_pattern)
        elif vertical=='bottom':
            vertical_insert:int=0

        finding_pattern.insert(vertical_insert, padding)

        # Horizontal padding
        if horizontal=='left':
            horizonal_insert:int=len(finding_pattern[0])
        elif horizontal=='right':
            horizonal_insert:int=0

        for (_, pattern) in enumerate(finding_pattern):
            pattern.insert(horizonal_insert, padding[0])

        return finding_pattern

    # Combine finding patterns
    def draw_finding_pattern(self, method_input=generate_boundaries):
        '''
        This method is combining different finding patterns and inserting
        them in respective places in the template.
        '''
        top_left=self._one_finding_pattern(vertical='top', horizontal='left')
        top_right=self._one_finding_pattern(vertical='top', horizontal='right')
        bottom_left=self._one_finding_pattern(vertical='bottom',
                                             horizontal='left')
        finding_patterns:dict={'top_left':top_left,
                               'top_right':top_right,
                               'bottom_left':bottom_left}

        # Check due to passing method as argument
        structure=self._is_callable(method_input=method_input)

        # Dictionary is used to prevent multiple for loop blocks
        for name, pattern in finding_patterns.items():
            for (row, _) in enumerate(pattern):
                for (column, _) in enumerate(pattern[0]):
                    structure[row-len(pattern) if name =='bottom_left'
                                    else row][column-len(pattern)
                                    if name=='top_right'
                                    else column]=pattern[row][column]

        return structure

    def draw_dummy_format_bits(self, method_input=generate_boundaries):
        '''
        This method is inserting reserved spots for format bits of QR Code.
        '''
        # Check due to passing method as argument
        structure=self._is_callable(method_input=method_input)

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
        '''
        This method is generating the full QR Code template.
        '''
        combined=self.generate_boundaries()
        self.draw_timing_pattern(combined)
        self.draw_finding_pattern(combined)
        self.draw_dummy_format_bits(combined)

        return combined

    # Print the empty QR Code
    def print_qr_code_layout(self):
        '''
        This method is priting the layout / template in a human readable form.
        '''
        combined=self.combine_qr_code_layout()
        qr_code:str=''
        for (_, row) in enumerate(combined):
            for column in row:
                qr_code=qr_code+' '+column
            qr_code=qr_code+'\n'

        return qr_code

class QRCode(UserInput):
    '''
    Generating QR Code using user input.
    '''
    def __init__(self,
                 text_input:str=None,
                 encoding_type:str='byte',
                 size:int=21,
                 ecc_level:str='low',
                 masking_pattern:int=None):
        self.text_input=text_input
        super().__init__(text_input=self.text_input)
        self.encoding_type=encoding_type
        self.size=size
        self.character_count:int=len(self.analyze_input(
            encoding_type=encoding_type
        ))
        self.ecc_level=ecc_level
        self.masking_pattern=masking_pattern
        self.possible_masks:dict={
            0:'000',
            1:'001',
            2:'010',
            3:'100',
            4:'011',
            5:'101',
            6:'110',
            7:'111'
        }

    def _is_callable(self, method_input):
        '''
        This is a helper method to check if the argument is callable and
        if not then it is preparing it to run it.
        '''
        if callable(method_input):
            structure=method_input(self)
        else:
            structure=method_input

        return structure

    def _concatenate_data(self, encoding_type:str='byte'):
        '''
        This method is getting data from user input and adding to it the
        encoding bits and count.
        '''
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

        encoding:str=encoding_type_dict[encoding_type]
        encoding_character_count:str=character_count_binary
        encoding_input:str=self.input_to_data_bits()
        concat:str=encoding+encoding_character_count+encoding_input+terminator+padding

        return concat

    def _split_blocks(self):
        '''
        This method is splitting the bits into bytes.
        '''
        binary_string_data:str=self._concatenate_data()

        # Split blocks to bytes (8 bits)
        n=8
        binary_codewords:list=[]
        hexadecimal_codewords:list=[]
        for _ in range(round(len(binary_string_data)/n)):
            binary_codewords.append(binary_string_data[:n])
            binary_string_data=binary_string_data[n:]

        for codeword in binary_codewords:
            hexadecimal_codewords.append(hex(int(codeword, 2)))

        return hexadecimal_codewords

    def _error_correction(self):
        '''
        This method is using reedsolo library to generate error correction
        codes with Reed-Solomon algorithm.
            
        Expected ECC:
            low = 7%
            medium =  15%
            quartile = 25%
            high = 30%
        '''

        codewords:list=self._split_blocks()
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

    def _add_ecc_to_concatenated_data(self):
        '''
        This method iis appending error correction codes to the data binary
        string.
        '''
        concat=self._concatenate_data()
        hexadecimal_ecc=self._error_correction()
        # binary_ecc=[bin(x) for x in hexadecimal_ecc]
        binary_ecc=''

        for i in hexadecimal_ecc:
            byte_size_binary=bin(int(i, 16))[2:]
            while len(byte_size_binary) < 8:
                byte_size_binary='0'+byte_size_binary

            binary_ecc+=byte_size_binary

        concat+=str(binary_ecc)

        return concat

    def _zig_zag_pattern(self):
        '''
        This method is generating coordinates of the zig zag pattern that
        will be used to insert data into respective places in QR Code
        '''
        zig_zag:list=[]
        boundaries=Layout(size=self.size).combine_qr_code_layout()

        def _direction_pattern(column:int, direction:str):
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
            if column<=6:
                column=column-1

            _direction_pattern(column, direction)

            direction='down' if direction=='up' else 'up'

        return zig_zag

    def _draw_data(self):
        '''
        This method is drawing concatenated data to QR Code
        '''
        drawing=Layout(size=self.size).combine_qr_code_layout()
        data=self._add_ecc_to_concatenated_data()
        zig_zag=self._zig_zag_pattern()
        for (i, j) in zig_zag:
            drawing[i][j]=' ' if data[0]=='0' else '#'
            data=data[1:]

        return drawing

    def _masking_bool(self, i:int, j:int):
        '''
        This is helper method to select masking pattern from a dict
        '''
        # Masking patterns
        # i - horizontal
        # j - vertical
        masking_patterns:dict={
            0: (i+j)%2==0,
            1: i%2==0,
            2: j%3==0,
            3: (i+j)%3==0,
            4: (int(i/2) + int(j/3))%2==0,
            5: (i*j)%2+(i*j)%3==0,
            6: ((i*j)%3+i*j)%2==0,
            7: ((i*j)%3+i+j)%2==0
        }

        return masking_patterns[self.masking_pattern]

    # Get all mask templates under this function and apply every mask to
    # generated QR Code
    # Calculate which mask is most beneficial and select it
    def _apply_masking_to_data(self):
        '''
        This method is applying masking to the data.
        '''
        # Masking patterns
        # i - horizontal
        # j - vertical

        zig_zag_pattern=self._zig_zag_pattern()
        masking:dict={}
        data=self._draw_data()
        masked_data:list=data

        # Masking data
        for coordinates in zig_zag_pattern:
            selected_masking_pattern=self._masking_bool(i=coordinates[0],
                                                                  j=coordinates[1])
            masking[coordinates]=selected_masking_pattern

        for coordinates, mask_bool in masking.items():
            if mask_bool is True:
                if masked_data[coordinates[0]][coordinates[1]]=='#':
                    masked_data[coordinates[0]][coordinates[1]]=' '
                elif masked_data[coordinates[0]][coordinates[1]]==' ':
                    masked_data[coordinates[0]][coordinates[1]]='#'

        return masked_data

    # Leaving it as it works but will be covered with a table
    # # Add to the QR Code format bits:
    # # ECC Level, Masking, ECC for masking
    # def generate_format_bits(self):
    #     ecc_encoding:dict={
    #         'low': '01',
    #         'medium': '00',
    #         'quartile': '11',
    #         'high': '10'
    #     }
    #     generator_polynominal='10100110111'
    #     to_encode:str=ecc_encoding[self.ecc_level]+self.masking_pattern
    #     concat:str=to_encode

    #     while len(concat)<15:
    #         concat=concat+'0'

    #     i=0
    #     generator:str=''
    #     while len(concat)!=10:
    #         if len(concat)>10:
    #             while concat[0]=='0':
    #                 concat=concat[1:]

    #             generator=generator_polynominal+'0'*(len(concat)-len(generator_polynominal))
    #             concat=str(bin(int(concat, 2)^int(generator, 2)))[2:]

    #         if len(concat)<10:
    #             while len(concat)<10:
    #                 concat='0'+concat

    #     encoded=to_encode+concat

    #     return encoded

    def _format_bits(self):
        '''
        This is helper method to select format bits.
        '''
        format_bits_masked:dict={
            ('low', 0): '111011111000100',
            ('low', 1):	'111001011110011',
            ('low', 2): '111110110101010',
            ('low', 3): '111100010011101',
            ('low', 4): '110011000101111',
            ('low', 5): '110001100011000',
            ('low', 6): '110110001000001',
            ('low', 7): '110100101110110',
            ('medium', 0): '101010000010010',
            ('medium', 1): '101000100100101',
            ('medium', 2): '101111001111100',
            ('medium', 3): '101101101001011',
            ('medium', 4): '100010111111001',
            ('medium', 5): '100000011001110',
            ('medium', 6): '100111110010111',
            ('medium', 7): '100101010100000',
            ('quartile', 0): '011010101011111',
            ('quartile', 1): '011000001101000',
            ('quartile', 2): '011111100110001',
            ('quartile', 3): '011101000000110',
            ('quartile', 4): '010010010110100',
            ('quartile', 5): '010000110000011',
            ('quartile', 6): '010111011011010',
            ('quartile', 7): '010101111101101',
            ('high', 0): '001011010001001',
            ('high', 1): '001001110111110',
            ('high', 2): '001110011100111',
            ('high', 3): '001100111010000',
            ('high', 4): '000011101100010',
            ('high', 5): '000001001010101',
            ('high', 6): '000110100001100',
            ('high', 7): '000100000111011'
        }
        masked:str=format_bits_masked[self.ecc_level, self.masking_pattern]

        return masked

    def draw_format_bits(self):
        '''
        This method is used to draw format bits to QR Code.
        '''
        structure:list=self._apply_masking_to_data()
        binary_format_bits=self._format_bits()
        format_bits:str=''

        for _ in enumerate(binary_format_bits):
            format_bits=format_bits+'#' if binary_format_bits[0]=='1' else format_bits+' '
            binary_format_bits=binary_format_bits[1:]

        # Split format bits string in half
        bottom_left_format_bits:str=format_bits[0:7]
        top_right_format_bits:str=format_bits[7:15]

        # Apply first half to bottom left
        for row in range(len(structure)-1, -1, -1):
            if row > len(structure)-8:
                structure[row][8]=bottom_left_format_bits[0]
                bottom_left_format_bits=bottom_left_format_bits[1:]

        # Apply second half to top right
        for column in range(len(structure[0])-1, -1, -1):
            if column > len(structure)-9:
                structure[8][column]=top_right_format_bits[-1]
                top_right_format_bits=top_right_format_bits[:-1]

        # Apply full length to top left
        for column in range(len(structure[0])):
            if column < 8 and column != 6:
                structure[8][column]=format_bits[0]
                format_bits=format_bits[1:]

        for row in range(len(structure)-1, -1, -1):
            if row < 9 and row != 6:
                structure[row][8]=format_bits[0]
                format_bits=format_bits[1:]

        return structure

    def _calculate_penalty_first(self, method_input=draw_format_bits):
        '''
        This is helper method to calculate first condition penalty points.
        First condition is + 3 points for each row or column of five of the
        same area type (dark / light) and +1 point for each additional beyond
        that.
        '''
        structure=self._is_callable(method_input=method_input)
        penalty_count:int=0

        # Five or more of same symbols in a row
        for row in structure:
            actual_cell:str=''
            last_cell:str=''
            count:int=0

            for cell in row:
                actual_cell:str=cell

                if actual_cell==last_cell:
                    count+=1
                else:
                    count=1

                last_cell=actual_cell

                if count==5:
                    penalty_count+=3
                elif count>5:
                    penalty_count+=1

        # Five or more of same symbols in a column
        for column_index in range(len(structure[0])):
            actual_cell:str=''
            last_cell:str=''
            count:int=0

            for (row_index, _) in enumerate(structure):
                actual_cell=structure[row_index][column_index]
                if actual_cell==last_cell:
                    count+=1
                else:
                    count=1

                last_cell=actual_cell

                if count==5:
                    penalty_count+=3
                elif count>5:
                    penalty_count+=1

        return penalty_count

    def _calculate_penalty_second(self, method_input=draw_format_bits):
        '''
        This is helper method to calculate ssecond condition penalty points.
        Second condition is +3 penalty points for each two by two blocks
        of the same symbol type (dark / light)
        '''
        structure=self._is_callable(method_input=method_input)
        penalty_count:int=0

        for row_index in range(len(structure)-1):
            for column_index in range(len(structure[0])-1):
                cell_1=structure[row_index][column_index]
                cell_2=structure[row_index+1][column_index]
                cell_3=structure[row_index][column_index+1]
                cell_4=structure[row_index+1][column_index+1]

                if cell_1 == cell_2 == cell_3 == cell_4:
                    penalty_count+=3

        return penalty_count

    def _calculate_penalty_third(self, method_input=draw_format_bits):
        '''
        This is helper method to calculate ssecond condition penalty points.
        Third condition is +40 penalty points for 'Finder pattern'-like patterns.
        '''
        structure=self._is_callable(method_input=method_input)

        penalty_count:int=0
        penalty_pattern_1:list=['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ']
        penalty_pattern_2:list=[' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#']
        lists_to_check:list=[]

        for (row_index, _) in enumerate(structure):
            for (column_index, _) in enumerate(structure[row_index]):
                if column_index+10 < self.size:
                    lists_to_check.append(structure[row_index][column_index:column_index+11])

        for (column_index, _) in enumerate(structure[0]):
            for (row_index, _) in enumerate(structure):
                if row_index+10 < self.size:
                    column_list=[structure[i][column_index] for i in range(row_index, row_index+11)]
                    lists_to_check.append(column_list)

        for check in lists_to_check:
            if check==penalty_pattern_1:
                penalty_count+=40

            if check==penalty_pattern_2:
                penalty_count+=40

        return penalty_count

    def _calculate_penalty_fourth(self, method_input=draw_format_bits):
        '''
        This is helper method to calculate ssecond condition penalty points.
        Fourth condition is dark to light ratio
        '''
        structure=self._is_callable(method_input=method_input)
        dark_count:int=0
        total_count:int=0

        for (row_index, _) in enumerate(structure):
            count=Counter(structure[row_index])
            dark_count+=count['#']
            total_count+=(count['#']+count[' '])

        percent_count=(dark_count/total_count)*100
        small_percent_count=abs(percent_count//5*5-50)
        large_percent_count=abs(percent_count//5*5+5-50)
        penalty_count=int(min(small_percent_count, large_percent_count))

        return penalty_count

    def _calculate_penalty(self):
        '''
        This method is calculating penalty points based on four conditions.
        '''
        penalty_dict:dict={}

        for mask in self.possible_masks:
            inner_call=QRCode(text_input=self.text_input,
                              encoding_type=self.encoding_type,
                              size=self.size,
                              ecc_level=self.ecc_level,
                              masking_pattern=mask)
            structure:list=inner_call.draw_format_bits()
            penalty_count:int=0

            # First condition
            penalty_count+=self._calculate_penalty_first(method_input=structure)

            # Second condition
            penalty_count+=self._calculate_penalty_second(method_input=structure)

            # Third condition
            penalty_count+=self._calculate_penalty_third(method_input=structure)

            # Fourth condition
            penalty_count+=self._calculate_penalty_fourth(method_input=structure)

            penalty_dict[penalty_count]=mask

        return penalty_dict

    def print_qr_code(self):
        '''
        This method is presenting the final QR Code in Version 1.
        '''
        penalty_counts=self._calculate_penalty()
        qr_code:str=''

        if self.masking_pattern is None:
            selected_mask=penalty_counts[min(penalty_counts)]
            inner_call=QRCode(text_input=self.text_input,
                              encoding_type=self.encoding_type,
                              size=self.size,
                              ecc_level=self.ecc_level,
                              masking_pattern=selected_mask)
            qr_code=qr_code+'Selected mask = '+str(selected_mask)+'\n\n'
        else:
            inner_call=QRCode(text_input=self.text_input,
                              encoding_type=self.encoding_type,
                              size=self.size,
                              ecc_level=self.ecc_level,
                              masking_pattern=self.masking_pattern)
            qr_code=qr_code+'Selected mask = '+str(self.masking_pattern)+'\n\n'

        combined=inner_call.draw_format_bits()
        for (row, _) in enumerate(combined):
            for column in combined[row]:
                qr_code=qr_code+' '+column
            qr_code=qr_code+'\n'

        return qr_code

if __name__ == '__main__':
    print(QRCode().print_qr_code())