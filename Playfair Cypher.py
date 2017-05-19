#In this scheme, pairs of letters are encrypted,
#instead of single letters as in the case of simple substitution cipher.
#In playfair cipher, initially a key table is created.
#The key table is a 5×5 grid of alphabets that acts as the key
#for encrypting the plaintext.
#Each of the 25 alphabets must be unique and one letter of the alphabet
#(usually J) is omitted from the table as we need only 25 alphabets instead of 26.
#If the plaintext contains J, then it is replaced by I.
#creating the main frame of the playfair cipher
def cypher(word,secret_key):
    text=word.lower()
    key=secret_key.lower()
    matrix = [[0 for x1 in range(1,6)] for y in range(1,6)]
    m=[]
    n=[]
    r=[]
    #here text is your text and key is the secret text
    for x in text:
        z=""
        if x != " ":
            m.append(x)
        else:
            z= z + ""
    for x4 in key:
        z=""
        if x4 != " ":
            r.append(x4)
        else:
            z= z + ""
    for x2 in range(0,len(m)-1):
        z = ""
        if m[x2] == m[x2+1]:
            m.insert(x2+1,"x")
        else:
            z= z + ""
    if len(m)%2 !=0:
        m.append("x")
    for x3 in range(0,len(m)-1):
        z = ""
        if m[x3] == "j":
            m[x3] = "i"
        else:
            z= z + ""
    for y in range(0,len(m)-1,2):
        z=""
        z= m[y] + m[y+1]
        n.append(z)
    new=[ r[i] for i in range(len(r)) if not r[i] in r[:i]]
    for i in range(97,123):
        new.append(chr(i))
    mew=[ new[k] for k in range(len(new)) if not new[k] in r[:k]]
    mew = filter(lambda x : x != "j", mew)
    g=0
    a1=[]
    b1=[]
    a2=[]
    b2=[]
    d=0
    for e in range(0,5):
        for f in range(0,5):
            matrix[e][f]=mew[g]
            g=g+1
    for g1 in range(0,len(m)-1,2):
        for e1 in range(0,5):
            for f1 in range(0,5):
                if matrix[e1][f1] == m[g1]:
                    a1.append(e1)
                    b1.append(f1)
    for g2 in range(1,len(m),2):
        for e2 in range(0,5):
            for f2 in range(0,5):
                if matrix[e2][f2] == m[g2]:
                    a2.append(e2)
                    b2.append(f2)
    for g3 in range(0,len(m)-1,2):
        if a1[d] == a2[d]:
            if b1[d] == 4:
                m[g3]=matrix[a1[d]][0]
                m[g3+1]=matrix[a2[d]][b2[d]+1]
                d=d+1
            elif b2[d] == 4:
                m[g3]=matrix[a1[d]][b1[d]+1]
                m[g3+1]=matrix[a2[d]][0]
                d=d+1
            elif b1[d] == 4 and b2[d] == 4:
                m[g3]=matrix[a1[d]][0]
                m[g3+1]=matrix[a2[d]][0]
                d=d+1
            else:
                m[g3]=matrix[a1[d]][b1[d]+1]
                m[g3+1]=matrix[a2[d]][b2[d]+1]
                d=d+1
        elif b1[d] == b2[d]:
            if a1[d] == 4:
                m[g3]=matrix[0][b1[d]]
                m[g3+1]=matrix[a2[d]+1][b2[d]]
                d=d+1
            elif a2[d] == 4:
                m[g3]=matrix[a1[d]+1][b1[d]]
                m[g3+1]=matrix[0][b2[d]]
                d=d+1
            elif a1[d] == 4 and a2[d] == 4:
                m[g3]=matrix[0][b1[d]]
                m[g3+1]=matrix[0][b2[d]]
                d=d+1
            else:
                m[g3]=matrix[a1[d]+1][b1[d]]
                m[g3+1]=matrix[a2[d]+1][b2[d]]
                d=d+1
        else:
            m[g3]=matrix[a1[d]][b2[d]]
            m[g3+1]=matrix[a2[d]][b1[d]]
            d=d+1
    q=[]
    for y in range(0,len(m)-1,2):
        z=""
        z= m[y] + m[y+1]
        q.append(z)
    y= "".join(q)
    return y

