def calculate(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return -1

if __name__ == "__main__":
    print(calculate(1, 2, "+"))