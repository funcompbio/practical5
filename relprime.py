def main(x, y) :
    i = 1
    c = 0
    while (i <= x and i <= y) :
        if (x % i == 0 and y % i == 0) :
            c = c + 1

        i = i + 1

    res = "yes"

    if (c > 1) :
        res = "no"

    return res

if __name__ == "__main__" :
    import sys

    if (len(sys.argv) != 3) :
        print("relprime.py <x> <y>")
    else :
        print(main(int(sys.argv[1]), int(sys.argv[2])))


