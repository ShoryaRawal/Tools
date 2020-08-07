import tkinter
from argparse import ArgumentParser, ArgumentError
 
def Dec_to_bin(num) :
    if num > 1 :
        Dec_to_bin(num // 2)
    print(num % 2, end = "")

def Str_to_bin(str) :
    res = ''.join(format(ord(i), 'b') for i in str)
    print(res)

def argumnets() :
    argumnets = ArgumentParser()

    argumnets.add_argument("-g", "--gui", action = "store_true")
    argumnets.add_argument("-s", "--string", action = "store_true")
    argumnets.add_argument("Value", help = "Input a value for converting.", nargs = "?", const = 0)

    return argumnets.parse_args()

def gui() :
    window = tkinter.Tk()
    window.title("Convert to binary")

    frm_entry = tkinter.Frame(master = window)
    frm_entry.grid(row = 0, column = 0, padx = 10)

    ent_value = tkinter.Entry(master = frm_entry, width = 10)
    ent_value.grid(row = 0, column = 0, sticky = "e")

    lb_result = tkinter.Label(master = window, text = "Binary")
    lb_result.grid(row = 0, column = 2, padx = 10)

    def val_to_bin() :
        value = ent_value.get()
        idk = float(value)
        if idk.is_integer() :
            num = int(value)
            val = bin(num)
            res = val[2:]
        else :
            res = ''.join(format(ord(i), 'b') for i in value)
        
        lb_result["text"] = f"{res}"

    btn_convert = tkinter.Button(
        master = window,
        text = "\N{RIGHTWARDS BLACK ARROW}",
        command = val_to_bin
    )
    btn_convert.grid(row =0, column = 1, pady = 10)

    window.mainloop()

if __name__ == "__main__":
    args = argumnets()

    if args.gui :
        gui()
    else :
        value = args.Value
        if args.string :
            Str = value    
            Str_to_bin(Str)
            print("")
        else :
            num = int(value)
            Dec_to_bin(num)
            print("")