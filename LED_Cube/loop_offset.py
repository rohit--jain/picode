# testing my loop index offsets

def abc():
    print("abc")

def bcd():
    print("bcd")

def cde():
    print("cde")

def de_f():
    print("def")

buffer = {
        0 : abc,
        1 : bcd,
        2 : cde,
        3 : de_f 
    }

def main():
    
    for i in range(0,1):
        buffer[i]()

if __name__ == "__main__":main()