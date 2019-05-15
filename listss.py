words=['Subodh','Neeraj','Arun']

for w in words[:]:

    if len(w)<5:
    	words.insert(0,w)
    elif len(w)>=6:
        words.append("Yadav")




print(words) 	