def palindromic(s: str):
    return s == s[::-1]

#def palindromic2(n):
#    

def main():
    print(sum(i for i in range(1, 1000000) if palindromic("{0:b}".format(i)) and palindromic("{}".format(i))))
    
main()
