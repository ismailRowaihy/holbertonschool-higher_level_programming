#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        print(f"{len(sys.argv) - 1} argument:") if len(sys.argv) == 2 else\
         print(f"{len(sys.argv) - 1} arguments:")

        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
    else:
        print(f"0 arguments.")
