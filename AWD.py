import sys 
import json
from os import system
from itertools import combinations,permutations

class Anagram:
    def __init__(self):
        self.words={}
        file=open("data/wordsDict.json","r",encoding="utf-8")
        json_string=file.read()
        self.words=json.loads(json_string)
        file.close()

    def ana(self,word):
        words=self.words
        word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
        anawords={}
        if word in words:
            for key,val in words[word]["word"].items():
                anawords[key]=[]
                for i in val:
                    anawords[key].append(i["def"])

        return anawords

    def printanawords(self,word):
        words=self.words
        anawords=self.ana(word)
        if anawords !={}:
            for key,val in anawords.items():
                print(key)
                
        else:
            print("Word not found")

    def printana(self,word):
        words=self.words
        anawords=self.ana(word)
        c=0
        if anawords !={}:
            for key,val in anawords.items():
                print(key+":")
                c=0
                for i in val:
                    print(str(c+1)+") "+i)
                    c=c+1
        else:
            print("Word not found")

    def anaCombinations(self,word,n):
        words=self.words
        allwords=[''.join(l) for i in range(len(word),n-1,-1) for l in combinations(word, i)]
        allwords=sorted(list(set(allwords)),key=len,reverse=True)
        c=0
        anacombwords={}
        for i in allwords:
            self.word=i
            anawords=self.ana(i)
            if anawords !={}:
                for key,val in anawords.items():
                    try:
                        anacombwords[len(i)][key]=[]
                    except:
                        anacombwords[len(i)]={key:[]}
                    for k in val:
                        anacombwords[len(i)][key].append(k)
        return anacombwords

    def printAnaCombinations(self,word,n):
        words=self.words
        word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
        anacombwords=self.anaCombinations(word,n)
        c=0
        if anacombwords !={}:
            for key1,val1 in anacombwords.items():
                print("\nWords with length {}:".format(key1))
                for key,val in val1.items():
                    print("\n"+key+":")
                    c=0
                    for i in val:
                        print(str(c+1)+") "+i)
                        c=c+1
        else:
            print("No words not found")

    def printAnaCombinationswords(self,word,n):
        words=self.words
        word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
        anacombwords=self.anaCombinations(word,n)
        if anacombwords !={}:
            for key1,val1 in anacombwords.items():
                print("\nWords with length {}:".format(key1))
                for key,val in val1.items():
                    print(key)
        else:
            print("No words not found")

    def insidestr(a,b):
        c=0
        if len(b)>len(a):
            return False 
        else:
            for i in b:
                if i in a:
                    c=c+1
            if c==len(b):
                return True
            else:
                return False

    def subtractstr(a,b):
        for i in b:
            if i in a:
                a=a[:a.find(i)]+a[a.find(i)+1:]
        return a


def select(Ana):
    print("""\nType 1 for anagram of full word only (Without Definitions)\nType 2 for anagram of full word only (With Definitions)\nType 3 for anagram of all contained words (Without Definitions)\nType 4 for anagram of all contained words (With Definitions)\nType 5 to clear screen\nType 999 to exit\n""")
    ch=int(input("Enter your choice: "))
    

    if ch==1:
        word=input("Enter your word: ")
        Ana.printanawords(word)
        select(Ana)
    elif ch==2:
        word=input("Enter your word: ")
        Ana.printana(word)
        select(Ana)
    elif ch==3:
        word=input("Enter your word: ")
        Ana.printAnaCombinationswords(word,int(input("Enter shortest desired length of anagrams: ")))
        select(Ana)
    elif ch==4:
        word=input("Enter your word: ")
        Ana.printAnaCombinations(word,int(input("Enter shortest desired length of anagrams: ")))
        select(Ana)
    elif ch==5:
        system('cls')
        select(Ana)
    elif ch!=999:
        print("\nThat choice doesn't exist\n")
        time.sleep(2)
        select(Ana)

def start():
    Ana=Anagram()
    try:
        select(Ana)
    except:
        print("Some error occoured")
        start()
start()
