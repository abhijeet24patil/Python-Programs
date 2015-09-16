import re

def wordCount(text):
    dic={}
    tokens=re.split(r'\W*',text)
    tok=[word.lower() for word in tokens if len(word)>=2]
    for word in tok:
        dic[word]=tok.count(word)
    print('word  ====>','  Count')
    for key in dic.keys():
        print(key,':',dic[key])


    
    
