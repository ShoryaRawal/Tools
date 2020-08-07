from argparse import ArgumentParser
from tkinter import *
from fpdf import FPDF

class Text_To_PDF():     
    def Engine(input_file, output_File):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        input_File = open(input_file, "r")

        for line in input_File :
            pdf.cell(200, 10, txt = line, ln = 1, align = 'C')
        
        pdf.output(output_File)

    def GUI():
        root = Tk()
        root.title("PDF convertor")
        root.attributes("-type", "dialog")
        root.resizable(FALSE, FALSE)
        

    def arguments():
        args = ArgumentParser()
        args.add_argument("Input", help = "Enter the file to read from.")
        args.add_argument("Output", help = "Enter the file to write to.")
        
        return args.parse_args()

    if __name__ == "__main__":
        args = arguments()
        input_file = args.Input
        output_file = args.Output

        Engine(input_file, output_file)
