import argparse as ap
import pikepdf as pdf

par=ap.ArgumentParser()
par.add_argument('-p', '--pdf',required=True, help="name of the pdf file you want to split")
par.add_argument('-s', '--start',required=True, help="where you want to start the file to split from")
par.add_argument('-e', '--end',required=True, help="till where you want to split the pdf")
par.add_argument('-o','--output',required=True, help="what do you want to name the file")

arg=par.parse_args()

file=arg.pdf
s=int(arg.start)-1
e=int(arg.end)
o=arg.output

with pdf.Pdf.open(file) as file_pdf:
    new_pdf = pdf.Pdf.new()
    for page in file_pdf.pages[s:e]:
        new_pdf.pages.append(page)

    new_pdf.save(o)

print("done!!")