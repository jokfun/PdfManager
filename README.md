# Manipulate PDF Files

Merge, split, encrypt... your files files by using a command line python program

## List of available possibilities

1. __Merge__
	Merge different pdfs into a single one
2. __Split__
	Separate all the pages of a pdf, they will be renamed in the following order
3. __Rotate__
	Rotate the pages of a pdf by 90, 180 or 270 degrees.
4. __toText__
	Convert an entire pdf into text, which will be saved in a .txt file.
	__WARNING__ the contents may not be readable.
5. __Encrypt__
	Encrypt a pdf with a password. Be careful, it will be a copy of the pdf, the original will not be encrypted.
6. __Decrypt__
	Decrypt a pdf if you have the password.

## Examples

### Split a single pdf :
```
python pdf.py -f test.pdf -s
``` 

### Merge 3 pdfs, the order passed in parameter will be the order of the merge
```
python pdf.py -f file1.pdf file2.pdf file3.pdf -m
```

### Encrypt the contents of two documents and display the different steps
```
python pdf.py -f file1.pdf file2.pdf --encrypt --verbose
Password:
```

## All possibilities

```
python pdf.py --help

usage: pdf.py [-h] [-f FILE [FILE ...]] [-m] [-s] [-r] [--rotation ROTATION]
              [--verbose] [--txt] [--encrypt] [--decrypt]

Manipulate your pdf files

optional arguments:
  -h, --help            show this help message and exit
  -f FILE [FILE ...], --file FILE [FILE ...]
                        list of pdf
  -m, --merge           merge PDFs
  -s, --split           split PDFs
  -r, --rotate          rotate the pdf
  --rotation ROTATION   Value of the rotation
  --verbose             Print the different steps
  --txt                 convert PDF into txt
  --encrypt             Encrypt a file
  --decrypt             Decrypt a file
```

## Author

Raphael Teitgen raphael.teitgen@gmail.com


