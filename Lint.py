from ast import *
from utils import input_int, add64, sub64, neg64

def main():
    eight = Constant(8)
    neg_eight = UnaryOp(USub(), eight)
    read = Call(Name('input_int'), [])
    ast1_1 = BinOp(read, Add(), neg_eight)

    ast1_2 = parse("print(10 + -(12 + 20))")
    print(ast1_2)

if __name__ == '__main__':
    main()