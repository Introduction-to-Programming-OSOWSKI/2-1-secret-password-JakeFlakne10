#WRITE YOUR CODE IN THIS FILE
from sre_constants import IN


def password(p):
    if p == "Knights19":
        return"ACCESS GRANTED"
    else:
        return"ACCESS DENIED"

print(password("Knights19"))