from random import randint
from passlib.hash import sha256_crypt

def generate_otp(length=6):
    range_start = 10 ** (length - 1)
    range_end = (10**length) - 1
    otp = randint(range_start,range_end)
    return (otp) 

def generate_hash(string):
    return sha256_crypt.encrypt(string)