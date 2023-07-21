def is_valid_square(n):
    sq=int(n**0.5)
    if sq==n:
        return True
    else:
        return False
n=int(input())
print(is_valid_square(n))