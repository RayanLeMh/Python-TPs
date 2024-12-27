
word = input("Enter a word : ")
palindrom = True 
start=0
end=len(word)-1

while start < end:  
    if word[start] != word[end]:  
        palindrom = False
        break  
    start += 1
    end -= 1

if palindrom : print("yes , it's palindrom")    
else : print("no , it's not palindrom") 