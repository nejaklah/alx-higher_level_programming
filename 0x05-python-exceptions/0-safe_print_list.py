
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        print("")
        return i
    except Exception:
        print("")
        return i
