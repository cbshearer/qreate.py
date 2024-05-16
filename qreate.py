## following instruction here: https://towardsdatascience.com/create-and-read-qr-code-using-python-9fc73376a8f9
## and here to print qrcodes to terminal: https://github.com/lincolnloop/python-qrcode
## qreate.py

import io
import qrcode ## pip install qrcode
import argparse

## argument setup
parser = argparse.ArgumentParser(description="create a QR code")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "-file", nargs='?', const=True, help="Put QR code into a file.")
group.add_argument("-t", "-terminal", action="store_true", help="Print QR code to screen.", default=True)
group.add_argument("-b", "-both", nargs='?', const=True, help="Create a file and print to screen.")

parser.add_argument("-c", "--content", required=True, help="Content of QR code.")
args = parser.parse_args()
qrinput = args.content

## only print to terminal if t or b
if not args.f or args.b:
    print("\n\n   ", qrinput)
    qr = qrcode.QRCode()
    qr.add_data(qrinput)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())

## set output file if f or b
if args.f:
    qroutput = args.f
elif args.b:
    qroutput = args.b
else:
    qroutput = ""

## if qroutput has data then we output a file
if qroutput:
    ## add png if not included
    if not qroutput.endswith(".png"):
        qroutput = qroutput + ".png"

    ## create qr code and print file name
    img=qrcode.make(qrinput)
    img.save(qroutput)
    print("   ", qroutput, "\n\n")
