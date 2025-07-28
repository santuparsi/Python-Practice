f=open('note2.txt','a') # append the text
f.write('Ding dong bell!!')
f.close()
# open and read the file after appending
f=open('note2.txt')
print(f.read())