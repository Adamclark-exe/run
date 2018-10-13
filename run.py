'''def last_two(s):
    #do the work
    s1 - s[-2:]
    output = s1*3

    #return the answer
    return output
# test cases
if last_two("hello")=="lololo":
    print("correct")
else:
    print("incorrect")

if last_two("Hi")=="HiHiHi":
    print("correct")
else:
    print("incorrect")

def last_two(s):

    s1 = s[1:-1]
    output = s1*1

    return output
if last_two("hello")=="ell":
    print("correct")
else:
    print("incorrect")

if last_two("java")=="av":
    print("correct")
else:
    print("incorrect")

if last_two("coding")=="odin":
    print("correct")
else:
    print("incorrect")

def left2(l):
    l1 = l[0:2]
    r1 = l[2:]
    output = r1+l1

    return output 

if left2("Hello")=="lloHe":
    print("correct")
else:
    print("incorrect")

if left2("java")=="vaja":
    print("correct")
else:
    print("incorrect")

if left2("Hi")=="Hi":
    print("correct")
else:
    print("incorrect")'''

def make_out_word(m):

    m1 = m[3:4]
    output = m*1

    return output
if make_out_word('<<>>','yay')=="<<yay>>":
    print("correct")
else:
    print("incorrect")

if make_out_words('<<>>','woohoo')=="<<<woohoo>>":
    print("correct")
else:
    print("incorrect")

if make_out_words('<<>>','word')=="<<word>>":
    print("correct")
else:
    print("incorrect")




