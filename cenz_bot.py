import json
list_1=[]

with open('cenz.txt', encoding='UTF-8') as r:
	for i in r:
		n=i.lower().split('\n')[0]
		if n!= ' ':
			list_1.append(n)

with open('cenz.json', 'w', encoding='UTF-8') as e:
	json.dump(list_1,e)