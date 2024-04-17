word =input()
print(word)

store=dict()

for ch in word:
    if ch in store:
        store[ch]=store[ch]+1
    else:
        store[ch]=1
print(store)

resultchar = '#'
resulFrequency=0
allkeys=store.keys()
for ele in allkeys:
    if store[ele]>resulFrequency:
        resulFrequency=store[ele]
        resultchar=ele

print(resultchar,resulFrequency)
