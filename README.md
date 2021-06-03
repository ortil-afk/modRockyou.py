# modRockyou.py
Quick Python Script to modify the Rockyou.txt file to certain characters

## What Is The Purpose of this?
This is a quick python script to use, when cracking hashes with either Hashcat or John the Ripper. In the Event that you know the Password Policy or how many characters the Password would be, this script makes a custom wordlist from the Rockyou.txt file. This is good to be used in CTF's where you know the character amount, and do not want to unnecessarily try passwords that are either too long or too short. 

## Installation
Download the modRockyou.py file to the directory where your rockyou.txt file is located.

## How to use:
The script was made using Python3 so either:
```bash
python modRockyou.py
```
or 
```bash
python3 modRockyou.py
```
from there it will ask for input on how many letters you would like your modified file to be, and wether you want less than (<), equal to (=), or greater than (>) the amount of characters for your modified wordlist.
The modified file will be made within this directory, and will be labeled with the number of characters that are present.

## Modifications
For simplicity sake I only made it based on the Rockyou.txt file, since that is a common file to be used. in the event that you would like to change the wordlist, you can edit the file in python where the wordlist is declared:
```python
with open('rockyou.txt', errors="ignore") as f:
    # can modify the word limit to be <=, ==, or >=
```

## Disclaimer
This tool is to be used for Cybersecurity Research uses only, and not to be used for any malicious act. Only use this tool if you have permisssion to see/use the passwords that could be cracked using this tool.
