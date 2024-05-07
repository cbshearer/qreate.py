## qreate.py
## pip install qrcode
import qrcode
import argparse

## argument setup
parser = argparse.ArgumentParser(description="create a QR code")
parser.add_argument("-c", "--content", required=True, help="Content of QR code.")
parser.add_argument("-f", "--file", required=True, help="File path or name")
args = parser.parse_args()
qrinput = args.content
qroutput = args.file

## add png if not included
if not qroutput.endswith(".png"):
    qroutput = qroutput + ".png"

# create qr code
img=qrcode.make(qrinput)
img.save(qroutput)
