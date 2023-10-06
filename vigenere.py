
Inpt=input("Enter Text To Encode: ").upper()
Key=input("Enter Key: ").upper()
key=[ord(i) for i in Key]
val=[ord(i) for i in Inpt]

def pad(key,val):
        i=0
        while(len(val)>len(key)):
                key.append(key[i]) 
                i+=1

def en(key,val):
        cipher=[]
        for i in range(len(val)):
                if(chr(val[i])==' '):
                        cipher.append(val[i])
                        continue
                c=(val[i]+key[i])-65
                if(c>90):
                        c=64+(c-90)
                        
                cipher.append(c)

        s=''.join(chr(i) for i in cipher)
        return s,cipher
def dec(key,cipher):
        simple=[]
        for i in range(len(cipher)):
                if(chr(cipher[i])==' '):
                        simple.append(val[i])
                        continue
                c=(cipher[i]+65)-key[i]
                if(c<65):
                        c=(c+90)-64
                simple.append(c)

        s=''.join(chr(i) for i in simple)
        return s,simple
pad(key,val)
en,cipher=en(key,val)
print("Encode:",en)
print("Decode:",dec(key,cipher)[0])
