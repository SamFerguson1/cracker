def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a.endswith(b) == True or b.endswith(a) == True:
    return True
  return False

    
def main():

    print(end_other("fuck", "poopfuck"))
                      #0123456789
main()
    
