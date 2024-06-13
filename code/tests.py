import unittest
import app

class qrCodeTest(unittest.TestCase):
    def test_boundaries(self):
        actual=app.qrCode(size=(21,21)).generate_boundaries()
        expected=[['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@']]
        
        self.assertEqual(actual, expected)

    def test_timing_pattern(self):
        actual=app.qrCode(size=(21,21)).timing_pattern(direction='row')
        expected=['#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#']

        self.assertEqual(actual, expected)

    def test_draw_timing_pattern(self):
        actual=app.qrCode(size=(21,21)).draw_timing_pattern()
        expected=[['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@',' ','@','@','@','@','@','@','@','@','@','@','@','@','@','@'],
                  ['@','@','@','@','@','@','#','@','@','@','@','@','@','@','@','@','@','@','@','@','@']]

        self.assertEqual(actual, expected)

    def test_one_finding_pattern_top_left(self):
        actual=app.qrCode().one_finding_pattern(vertical='top', horizontal='left')
        expected=[['#', '#', '#', '#', '#', '#', '#', ' '],
                  ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
                  ['#', '#', '#', '#', '#', '#', '#', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        self.assertEqual(actual, expected)

    
    def test_one_finding_pattern_top_right(self):
        actual=app.qrCode().one_finding_pattern(vertical='top', horizontal='right')
        expected=[[' ', '#', '#', '#', '#', '#', '#', '#'],
                  [' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
                  [' ', '#', ' ', '#', '#', '#', ' ', '#'],
                  [' ', '#', ' ', '#', '#', '#', ' ', '#'],
                  [' ', '#', ' ', '#', '#', '#', ' ', '#'],
                  [' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
                  [' ', '#', '#', '#', '#', '#', '#', '#'],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        
        self.assertEqual(actual, expected)

    
    def test_one_finding_pattern_bottom_left(self):
        actual=app.qrCode().one_finding_pattern(vertical='bottom', horizontal='left')
        expected=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['#', '#', '#', '#', '#', '#', '#', ' '],
                  ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', '#', '#', '#', ' ', '#', ' '],
                  ['#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
                  ['#', '#', '#', '#', '#', '#', '#', ' ']]
        
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()