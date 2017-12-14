import pickle
a="I love Python"
output=open('Test.TXT','wb')
pickle.dump(a,output)
output.close()


f=open('Test.TXT','rb')
a=pickle.load(f)
print(a)
f.close()
