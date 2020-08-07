from argparse import ArgumentParser, ArgumentTypeError

def fahrenheit_to_celsius(value):
    fahrenheit = value
    celsius = (5/9) * (float(fahrenheit) - 32)
    print(str(celsius))

def valid_int(n) :
    if not n.digit():
        raise ArgumentTypeError("Mode must be a number")

    n = int(n)

    if n > 2:
        raise ArgumentTypeError("There are only 2 modes(1: c - f, 2: f - c)")

    elif n < 1:
        raise ArgumentTypeError("There are only 2 modes(1: c - f, 2: f - c)")

    return n

def args() :
    args = ArgumentParser()
    
    args.add_argument("mode")
    args.add_argument("Value_in_celcuis")

    return args.parse_args()

if __name__ == "__main__" :
    arguments =  args()
    
    mode = arguments.mode
    value = arguments.Value_in_celcuis

    if mode == 1 :
        pass
    elif mode == 2 :
        fahrenheit_to_celsius(value)