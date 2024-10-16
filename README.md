# qreate.py
Simple python script to create QR codes.

## Input:
Use option -c for the content you want in your QR Code.

## Output: 
One of the following is required:
- Use -t or --terminal to:
    - Print the QR Code in your terminal. 
    - The contents of the QR code are printed as plain text above the QR code.
- Use -f or --file to: 
    - Output the QR code to a file (specifying the file name).
    - This file will be a .PNG file placed in the current working directory.
    - The name of the file is printed below the QR code.
- Use -b or --both to do both of the above.

## Examples:
To just print the QR code in the terminal:
```python
python3 qreate.py -c https://www.bing.com -t
```
![image](https://github.com/user-attachments/assets/fc189308-6d3b-46db-b0c0-5b0d1004d2d1)


To just create the QR code in a file:
```python
python3 qreate.py -c https://www.bing.com -f bing.png
```

To both print the QR code in the terminal and create the QR code in a file:
```python
python3 qreate.py -c https://www.bing.com -b bing.png
```
![image](https://github.com/user-attachments/assets/e18cefac-7402-420a-9a4a-34a16cd5f883)
