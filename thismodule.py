print("__name__: %s" %(__name__))

if __name__ == "__main__" :
  import sys
  i = 0
  while i < len(sys.argv) :
    print("argument vector position %d: %s" %(i, sys.argv[i]))
    i = i + 1
