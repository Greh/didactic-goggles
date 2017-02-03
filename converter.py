#Hex to Base64 converter
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fixit', type=str)
    args = parser.parse_args()
    newstr = hex_to_base64(args.fixit)
    print newstr

def hex_to_base64(word):
    alist = list(word.lower())
    blist = []
    #parse ascii into numbers
    for item in alist:
        if item.isdigit():
            blist.append(int(item))
            pass
        elif ord(item) >= ord('a') and ord(item) <= ord('f'):
            blist.append(ord(item) - ord('a') + 10)
        else:
            raise RuntimeError('invalid string')
    elist, flag = list_of_threes(blist)
    newword=''
    for i in elist:
        if i>=0 and i<=25:
            newword = newword + chr(ord('A')+i)
        elif i>=26 and i <=51:
            newword = newword + chr(ord('a') -26 + i)
        elif i>=52 and i <=61:
            newword = newword + str(i-52)
        elif i==62:
            newword = newword + '+'
        elif i==63:
            newword = newword + '/'
        else:
            raise RuntimeError("you're bad at math")
    flag = flag*'='
    newword = newword+flag

    return newword

def list_of_threes(blist):
    flag = 0
    if len(blist)%3 ==1:
        blist = blist + [0, 0]
        flag = 1
    if len(blist)%3 ==2:
        blist.append(0)
        flag = 2

    clist = [-1]*(len(blist)/3)
    for i in xrange(0, len(blist)/3):
        clist[i] = [blist[i*3], blist[i*3+1], blist[i*3+2]]
        if clist[i] == -1:
            raise RuntimeError('list index error')
    dlist = []
    for element in clist:
        dlist.append(to_two_chunks(element))
    elist = []
    for element in dlist:
        elist = elist + element
    return elist, flag

def to_two_chunks(sublist):
    #60 = 111100, 3 = 000011, 48 = 110000, 15 = 001111
    newlist = [((sublist[0]<<2) & 60) + ((sublist[1]>>2) & 3),
               ((sublist[1]<<4) & 48) + ((sublist[2]) & 15)]
    return newlist

if __name__ == "__main__":
    main()
