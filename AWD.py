import sys 
import json
import time
from os import system
from itertools import combinations,permutations

def ana(words,word):
    word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
    anawords={}
    if word in words:
        for key,val in words[word]["word"].items():
            anawords[key]=[]
            for i in val:
                anawords[key].append(i["def"])

    return anawords

def printanawords(words,word):
    anawords=ana(words,word)
    if anawords !={}:
        for key,val in anawords.items():
            print(key)
            
    else:
        print("Word not found")

def printana(words,word):
    anawords=ana(words,word)
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

def anaCombinations(words,word,n):
    allwords=[''.join(l) for i in range(len(word),n-1,-1) for l in combinations(word, i)]
    allwords=sorted(list(set(allwords)),key=len,reverse=True)
    c=0
    anacombwords={}
    for i in allwords:
        anawords=ana(words,i)
        if anawords !={}:
            for key,val in anawords.items():
                try:
                    anacombwords[len(i)][key]=[]
                except:
                    anacombwords[len(i)]={key:[]}
                for k in val:
                    anacombwords[len(i)][key].append(k)
    return anacombwords

def printAnaCombinations(words,word,n):
    word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
    anacombwords=anaCombinations(words,word,n)
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

def printAnaCombinationswords(words,word,n):
    word="".join(sorted(word.lower().replace(" ","").replace("-","").replace("_","")))
    anacombwords=anaCombinations(words,word,n)
    if anacombwords !={}:
        for key1,val1 in anacombwords.items():
            print("\nWords with length {}:".format(key1))
            for key,val in val1.items():
                print(key)
    else:
        print("No words not found")


def select(words):
    
    print("""
Type 1 for anagram of full word only (Without Definitions)
Type 2 for anagram of full word only (With Definitions)
Type 3 for anagram of all contained words (Without Definitions)
Type 4 for anagram of all contained words (With Definitions)
Type 5 to clear screen
Type 999 to exit
        """)
    ch=int(input("Enter your choice: "))
    print()
    if ch==1:
        printanawords(words,input("Enter your word: "))
        select(words)
    elif ch==2:
        printana(words,input("Enter your word: "))
        select(words)
    elif ch==3:
        printAnaCombinationswords(words,input("Enter your word: "),int(input("Enter shortest desired length of anagrams: ")))
        select(words)
    elif ch==4:
        printAnaCombinations(words,input("Enter your word: "),int(input("Enter shortest desired length of anagrams: ")))
        select(words)
    elif ch==5:
        system('cls')
        select(words)
    elif ch!=999:
        print("\nThat choice doesn't exist\n")
        time.sleep(2)
        select(words)
def start():
    words={}
    file=open("data/wordsDict.json","r",encoding="utf-8")
    json_string=file.read()
    words=json.loads(json_string)
    file.close()
    try:
        select(words)
    except:
        print("Some error occoured")
        start()
start()
