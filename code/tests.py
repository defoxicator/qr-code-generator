import unittest
import app

class userInputTest(unittest.TestCase):
    def test_analyze_input(self):
        actual=app.userInput(text_input='Hello, world! 123').analyze_input()
        expected=[
            {'H': '01001000'},
            {'e': '01100101'},
            {'l': '01101100'},
            {'l': '01101100'},
            {'o': '01101111'},
            {',': '00101100'},
            {' ': '00100000'},
            {'w': '01110111'},
            {'o': '01101111'},
            {'r': '01110010'},
            {'l': '01101100'},
            {'d': '01100100'},
            {'!': '00100001'},
            {' ': '00100000'},
            {'1': '00110001'},
            {'2': '00110010'},
            {'3': '00110011'}
        ]

        self.assertEqual(actual, expected)

    def test_input_to_data_bits(self):
        actual=app.userInput(
            text_input='Hello world!123'
        ).input_to_data_bits()
        expected:str='010010000110010101101100011011000110111100100000011101110110111101110010011011000110010000100001001100010011001000110011'

        self.assertEqual(actual, expected)

class layoutTest(unittest.TestCase):
    def test_boundaries(self):
        actual=app.layout(size=21).generate_boundaries()
        expected=[
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
        ]
       
        self.assertEqual(actual, expected)

    def test_timing_pattern(self):
        actual=app.layout(size=21).timing_pattern()
        expected=['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#']

        self.assertEqual(actual, expected)

    def test_draw_timing_pattern(self):
        actual=app.layout(size=21).draw_timing_pattern()
        expected=[
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
        ]

        self.assertEqual(actual, expected)

    def test_one_finding_pattern_top_left(self):
        actual=app.layout().one_finding_pattern(vertical='top', horizontal='left')
        expected=[
            ['#', '#', '#', '#', '#', '#', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', '#', '#', '#', '#', '#', '#', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        
        self.assertEqual(actual, expected)

    
    def test_one_finding_pattern_top_right(self):
        actual=app.layout().one_finding_pattern(
            vertical='top', horizontal='right'
        )
        expected=[
            [' ', '#', '#', '#', '#', '#', '#', '#'],
            [' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            [' ', '#', ' ', '#', '#', '#', ' ', '#'],
            [' ', '#', ' ', '#', '#', '#', ' ', '#'],
            [' ', '#', ' ', '#', '#', '#', ' ', '#'],
            [' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            [' ', '#', '#', '#', '#', '#', '#', '#'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        
        self.assertEqual(actual, expected)

    
    def test_one_finding_pattern_bottom_left(self):
        actual=app.layout().one_finding_pattern(
            vertical='bottom', horizontal='left'
        )
        expected=[
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['#', '#', '#', '#', '#', '#', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', '#', '#', '#', '#', '#', '#', ' ']
        ]
        
        self.assertEqual(actual, expected)

    def test_draw_finding_pattern(self):
        actual=app.layout(size=21).draw_finding_pattern()
        expected=[
            ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '@', '@', '@', '@', ' ', '#', '#', '#', '#', '#', '#', '#'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', '@', '@', '@', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
        ]

        self.assertEqual(actual, expected)

    def test_draw_dummy_format_bits(self):
        actual=app.layout(size=21).draw_dummy_format_bits()
        expected=[
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            [' ', ' ', ' ', ' ', ' ', ' ', '@', ' ', ' ', '@', '@', '@', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
        ]

        self.assertEqual(actual, expected)

    def test_combine_qr_code_layout(self):
        actual=app.layout().combine_qr_code_layout()
        expected=[
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', '@', '@', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '@', '@', '@', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['@', '@', '@', '@', '@', '@', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']
        ]

        self.assertEqual(actual, expected)

class testQrCode(unittest.TestCase):
    def test_concatenate_data(self):
        actual=app.qrCode(text_input='Hello, world! 123').concatenate_data(encoding_type='byte')
        expected:str='01000001000101001000011001010110110001101100011011110010110000100000011101110110111101110010011011000110010000100001001000000011000100110010001100110000'

        self.assertEqual(actual, expected)

    def test_split_blocks(self):
        acutal=app.qrCode(text_input='Hello, world! 123').split_blocks()
        expected:list=['0x41', '0x14', '0x86', '0x56', '0xc6', '0xc6', '0xf2', '0xc2', '0x7', '0x76', '0xf7', '0x26', '0xc6', '0x42', '0x12', '0x3', '0x13', '0x23', '0x30']

        self.assertEqual(acutal, expected)

    def test_error_correction(self):
        actual=app.qrCode(text_input='Hello, world! 123').error_correction(ecc_level='low')
        expected:list=['0x85', '0xa9', '0x5e', '0x7', '0xa', '0x36', '0xc9']

        self.assertEqual(actual, expected)

    def test_add_ecc_to_concatenated_data(self):
        actual=app.qrCode(text_input='Hello, world! 123').add_ecc_to_concatenated_data()
        expected:str='0100000100010100100001100101011011000110110001101111001011000010000001110111011011110111001001101100011001000010000100100000001100010011001000110011000010000101101010010101111000000111000010100011011011001001'

        self.assertEqual(actual, expected)

    def test_draw_data(self):
        actual=app.qrCode(text_input='Hello, world! 123').draw_data()
        expected=[
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['#', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#'],
            [' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' '],
            [' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', ' '],
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' '],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' '],
            ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ']
        ]

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()