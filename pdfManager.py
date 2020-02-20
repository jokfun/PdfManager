import PyPDF2
from random import randint

class pdfManager:
    def __init__(self):
        pass

    def merge(self,args,name="merged",verbose=False):
        """
            Merge different pdfs into a single one

            Required parameters :
            args : a list of pdfs

            Optional parameters :
            name : name of the output
            verbose : show the different steps
        """
        newPdf = PyPDF2.PdfFileMerger()
        for pdf in args:
            if verbose:
                print("Opening",pdf,"..")
            try:
                f = open(pdf,"rb")
                newPdf.append(f)
                if verbose:
                    print("Done.")
            except Exception as e:
                print("Error : Can't open",pdf)
        name = name+str(randint(1000,9999))+".pdf"
        if verbose:
            print("Creating",name)
        try:
            out = open(name,"wb")
            newPdf.write(out)
            out.close()
            if verbose:
                print("Tash finished.")
        except Exception as e:
            print("Error : Can't create",name+".pdf")

    def split(self,args,name="splited",verbose=False):
        """
            Separate all the pages of a pdf, they will be renamed in the following order

            Required parameters :
            args : a list of pdfs

            Optional parameters :
            name : name of the output
            verbose : show the different steps
        """
        for pdf in args:
            if verbose:
                print("Opening",pdf)
            try:
                f = open(pdf,"rb")
                if verbose:
                    print("Done.")
                reader = PyPDF2.PdfFileReader(f)
                for i in range(reader.numPages):
                    result = pdf.split(".")[0]
                    result = result+"_"+name+"_"+str(i)+".pdf"
                    newPdf = PyPDF2.PdfFileWriter() 
                    newPdf.addPage(reader.getPage(i))
                    if verbose:
                        print("Creating page",name+str(i)+".pdf")
                    try:
                        out = open(result,"wb")
                        newPdf.write(out)
                        out.close()
                        if verbose:
                            print("Done")
                    except Exception as e:
                        print("Error : Can't create",result)
            except Exception as e:
                print(e)
                print("Error : Can't open",pdf)
        if verbose:
            print("Task finished.")


    def rotate(self,args,name="rotated",verbose=False,rotation=90):
        """
            Rotate the pages of a pdf by 90, 180 or 270 degrees.
            Required parameters :
            args : a list of pdfs

            Optional parameters :
            name : name of the output
            verbose : show the different steps
            rotation : the value of the roration, default : 90, must be 90,180 or 270
        """
        for pdf in args:
            if verbose:
                print("Opening",pdf)
            try:
                pdfFile = open(pdf,"rb")
                if verbose:
                    print("Done.")
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                output = PyPDF2.PdfFileWriter()
                for i in range(pdfReader.numPages):
                    page = pdfReader.getPage(i)
                    if rotation in [90,180,270]:
                        page.rotateClockwise(rotation)
                    elif verbose:
                        print("Rotation must be 90,180 or 270.")
                    output.addPage(page)
                name = pdf.split(".")[0] +"_"+name+"_"+str(randint(1000,9999))+".pdf"
                if verbose:
                    print("Creating",name+".pdf","file")
                try:
                    out = open(name,"wb")
                    if verbose:
                        print("Done")
                    output.write(out)
                except Exception as e:
                    print("Error : Can't create",name)
                pdfFile.close()
            except Exception as e:
                print("Error : Can't open",pdf)
        if verbose:
            print("Task finished.")


    def toText(self,args,name="toText",verbose=False):
        """
            Convert an entire pdf into text, which will be saved in a .txt file.

            Required parameters :
            args : a list of pdfs

            Optional parameters :
            name : name of the output
            verbose : show the different steps
        """
        for pdf in args:
            if verbose:
                print("Opening",pdf)
            try:
                pdfFile = open(pdf,"rb")
                if verbose:
                    print("Done.")
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                name_out = pdf.split(".")[0]
                name_out = name_out + "_" + name+"_"+str(randint(1000,9999))+".txt"
                if verbose:
                    print("Creating",name+".pdf","file")
                try:
                    out = open(name_out,"w")
                    if verbose:
                        print("Done.")
                    for i in range(pdfReader.numPages):
                        out.write(pdfReader.getPage(i).extractText())
                    out.close()
                except Exception as e:
                    print("Error : Can't write in",name_out)
                pdfFile.close()
                out.close()
            except Exception as e:
                print("Error : Can't open",pdf)
        if verbose:
            print("Task finished.")

    def encrypt(self,args,password,name="",verbose=False):
        """
            Encrypt a pdf with a password. Be careful, it will be a copy of the pdf, the original will not be encrypted.

            Required parameters :
            args : a list of pdfs
            password : the password (be careful)

            Optional parameters :
            name : name of the output
            verbose : show the different steps
        """
        for pdf in args:
            if verbose:
                print("Opening",pdf)
            try:
                pdfFile = open(pdf,"rb")
                if verbose:
                    print("Done.")
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted:
                    print(pdf,"already encrypted.")
                else:
                    output = PyPDF2.PdfFileWriter()
                    for i in range(pdfReader.numPages):
                        output.addPage(pdfReader.getPage(i))
                    output.encrypt(password)
                    out_name = pdf.split(".")[0]+name+"_"+str(randint(1000,9999))+".pdf"
                    if verbose:
                        print("Creating",out_name)
                    try:
                        out = open(out_name,"wb")
                        output.write(out)
                        if verbose:
                            print("Done.")
                    except Exception as e:
                        print("Error : Can't create encrypted",pdf)
            except Exception as e:
                print("Error : Can't open",pdf)
        if verbose:
            print("Task finished")

    def decrypt(self,args,password,name="",verbose=False):
        """
            Decrypt a pdf if you have the password.

            Required parameters :
            args : a list of pdfs
            password : the password (be careful)

            Optional parameters :
            name : name of the output
            verbose : show the different steps
        """
        for pdf in args:
            if verbose:
                print("Opening",pdf)
            try:
                pdfFile = open(pdf,"rb")
                if verbose:
                    print("Done.")
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if not pdfReader.isEncrypted:
                    print(pdf,"is not encrypted.")
                else:
                    pdfReader.decrypt(password)
                    output = PyPDF2.PdfFileWriter()
                    for i in range(pdfReader.numPages):
                        output.addPage(pdfReader.getPage(i))
                    out_name = pdf.split(".")[0]+name+"_"+str(randint(1000,9999))+".pdf"
                    if verbose:
                        print("Creating",out_name)
                    try:
                        out = open(out_name,"wb")
                        output.write(out)
                        if verbose:
                            print("Done.")
                    except Exception as e:
                        print("Error : Can't create encrypted",pdf)
            except Exception as e:
                print("Error : Can't open",pdf)
        if verbose:
            print("Task finished")
