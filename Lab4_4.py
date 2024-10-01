def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one} \n two={two}\n three={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(1,2,3,4,5,6,7,8,9,10)
    print(f"\nresult= {result}")