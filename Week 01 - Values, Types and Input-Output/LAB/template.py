"""
RECORD CHECK  -  my version
===========================

Name  :keshav
Lane  :  AI
Date  : 5 oct 2026

Run it:   python template.py
Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("hostname : ")   
first = float(input("gb used : "))      
second = float(input("gb total : "))  

difference = first - second   
percent = (first / second) * 100   

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)
print(f" used : {first:>10.2f} ")
print(f" total : {second:>10.2f} ")
print(f" difference : {difference:>+10.2f} ")
print(f" of total : {percent:>9.1f} % ")
print(f" free : {second - first:>10.2f} ")
print("=" * 34)
