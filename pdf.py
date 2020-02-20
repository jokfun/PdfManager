import argparse
from pdfManager import pdfManager

#This library is used to hide the password entered by the user.
from getpass import getpass

#Create a pdfManager object
output = pdfManager()

#Define the parser and all its arguments
parser = argparse.ArgumentParser(description="Manipulate your pdf files")

parser.add_argument("-f", "--file", nargs="+",
                    help="list of pdf")

parser.add_argument("-m", "--merge", action='store_true',
                    help="merge PDFs")

parser.add_argument("-s", "--split", action='store_true',
                    help="split PDFs")

parser.add_argument("-r", "--rotate", action='store_true',
                    help="rotate the pdf")

parser.add_argument("--rotation", type=int,
                    help="Value of the rotation")

parser.add_argument("--verbose", action='store_true',
                    help="Print the different steps")

parser.add_argument("--txt", action='store_true',
                    help="convert PDF into txt")

parser.add_argument("--encrypt", action='store_true',
                    help="Encrypt a file")

parser.add_argument("--decrypt", action='store_true',
                    help="Decrypt a file")


args = parser.parse_args()


#Execute the different tasks according to the parameters
verbose = False
if args.verbose:
	verbose = True

if args.file:
	if args.merge:
		output.merge(args.file,verbose=verbose)
	if args.split:
		output.split(args.file,verbose=verbose)
	if args.rotate:
		if args.rotation:
			output.rotate(args.file,verbose=verbose,rotation=args.rotation)
		else:
			print("Need the value of the rotation : --rotation value.")
	if args.txt:
		output.toText(args.file,verbose=verbose)
	if args.encrypt:
		password = getpass()
		output.encrypt(args.file,password=password,verbose=verbose)
	if args.decrypt:
		password = getpass()
		output.decrypt(args.file,password=password,verbose=verbose)
else:
	print("Must had files : -f [FILES ...]")