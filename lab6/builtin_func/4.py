import time 
import math

def calculate_square_root(num, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(num)
    print(f"Square root of {num} after {milliseconds} milliseconds is {result}")

if __name__ == "__main__":
    num = int(input("Sample Input:\n"))
    milliseconds = int(input())
    calculate_square_root(num, milliseconds)