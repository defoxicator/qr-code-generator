# qr-code-generator
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

In this project I am trying to write my own QR code generator:

## Step by step & comments

STEP 0.
Encode characters in bytes.
After MVP I can prepare checks for different encodings.

STEP 1.
Create data segment.

STEP 2.
Fit to QR code version number.

STEP 3.
Concatenate segments, add padding, make codewords.

STEP 4.
Split blocks, add ECC, interleave.

STEP 5.
Draw fixed patterns.

STEP 6.
Draw codewords and remainder.

STEP 7.
Try applying the masks.

STEP 8.
Find penalty patterns.

STEP 9.
Calculate penalty points, select best mask.  
QR code could be displayed in terminal using # and SPACEs.  
Zig-zag pattern for generating the QR code is starting from bottom  right towards top and then to the left.  

## TODO:
- [X] Incorporate automated testing in the project
- [X] Incorporate automated PEP 8 enforcement (pylint)
- [X] Learn how the QR codes are created
- [X] Write the logic for creating QR codes (MVP) and display them in the console
- [ ] Prepare a GUI (web / desktop)

## Useful links:
[QR Code step by step by Nayuki](https://www.nayuki.io/page/creating-a-qr-code-step-by-step)  
[Wikipedia Page](https://en.wikipedia.org/wiki/QR_code)  
[Unicode to Binary Converter](https://onlinetools.com/unicode/convert-unicode-to-binary)  
[From QR Codes to Voyager: How Reed-Solomon Codes Work](https://medium.com/@rodin.dev/from-qr-codes-to-voyager-how-reed-solomon-codes-work-e249dcfa8474)  
