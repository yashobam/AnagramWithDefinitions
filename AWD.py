import sys 
import json
def ana(word):
    file=open("data/a.json","r",encoding="utf-8")
    json_string=file.read()
    a=json.loads(json_string)
    file.close()
    file=open("data/b.json","r",encoding="utf-8")
    json_string=file.read()
    b=json.loads(json_string)
    file.close()
    file=open("data/c.json","r",encoding="utf-8")
    json_string=file.read()
    c=json.loads(json_string)
    file.close()
    file=open("data/d.json","r",encoding="utf-8")
    json_string=file.read()
    d=json.loads(json_string)
    file.close()
    file=open("data/e.json","r",encoding="utf-8")
    json_string=file.read()
    e=json.loads(json_string)
    file.close()
    file=open("data/f.json","r",encoding="utf-8")
    json_string=file.read()
    f=json.loads(json_string)
    file.close()
    file=open("data/g.json","r",encoding="utf-8")
    json_string=file.read()
    g=json.loads(json_string)
    file.close()
    file=open("data/h.json","r",encoding="utf-8")
    json_string=file.read()
    h=json.loads(json_string)
    file.close()
    file=open("data/i.json","r",encoding="utf-8")
    json_string=file.read()
    i=json.loads(json_string)
    file.close()
    file=open("data/j.json","r",encoding="utf-8")
    json_string=file.read()
    j=json.loads(json_string)
    file.close()
    file=open("data/k.json","r",encoding="utf-8")
    json_string=file.read()
    k=json.loads(json_string)
    file.close()
    file=open("data/l.json","r",encoding="utf-8")
    json_string=file.read()
    l=json.loads(json_string)
    file.close()
    file=open("data/m.json","r",encoding="utf-8")
    json_string=file.read()
    m=json.loads(json_string)
    file.close()
    file=open("data/n.json","r",encoding="utf-8")
    json_string=file.read()
    n=json.loads(json_string)
    file.close()
    file=open("data/o.json","r",encoding="utf-8")
    json_string=file.read()
    o=json.loads(json_string)
    file.close()
    file=open("data/p.json","r",encoding="utf-8")
    json_string=file.read()
    p=json.loads(json_string)
    file.close()
    file=open("data/q.json","r",encoding="utf-8")
    json_string=file.read()
    q=json.loads(json_string)
    file.close()
    file=open("data/r.json","r",encoding="utf-8")
    json_string=file.read()
    r=json.loads(json_string)
    file.close()
    file=open("data/s.json","r",encoding="utf-8")
    json_string=file.read()
    s=json.loads(json_string)
    file.close()
    file=open("data/t.json","r",encoding="utf-8")
    json_string=file.read()
    t=json.loads(json_string)
    file.close()
    file=open("data/u.json","r",encoding="utf-8")
    json_string=file.read()
    u=json.loads(json_string)
    file.close()
    file=open("data/v.json","r",encoding="utf-8")
    json_string=file.read()
    v=json.loads(json_string)
    file.close()
    file=open("data/w.json","r",encoding="utf-8")
    json_string=file.read()
    w=json.loads(json_string)
    file.close()
    file=open("data/x.json","r",encoding="utf-8")
    json_string=file.read()
    x=json.loads(json_string)
    file.close()
    file=open("data/y.json","r",encoding="utf-8")
    json_string=file.read()
    y=json.loads(json_string)
    file.close()
    file=open("data/z.json","r",encoding="utf-8")
    json_string=file.read()
    z=json.loads(json_string)
    file.close()
    words=[]
    words=list(a)+list(b)+list(c)+list(d)+list(e)+list(f)+list(g)+list(h)+list(i)+list(j)+list(k)+list(l)+list(m)+list(n)+list(o)+list(p)+list(q)+list(r)+list(s)+list(t)+list(u)+list(v)+list(w)+list(x)+list(y)+list(z)
    word=word.upper()
    wordss=list(words)
    for j in range(len(words)):
        wordss[j]=wordss[j].upper()
    for ij in range(len(wordss)):
        if len(wordss[ij])==len(word):
            if sorted(word)==sorted(wordss[ij]):
                print(wordss[ij][0].upper()+wordss[ij][1:].lower())
                if wordss[ij][0].lower()=="a":
                    for il in range(len(a[words[ij]]["meanings"])):
                        x=dict(a[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="b":
                    for il in range(len(b[words[ij]]["meanings"])):
                        x=dict(b[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="c":
                    for il in range(len(c[words[ij]]["meanings"])):
                        x=dict(c[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="d":
                    for il in range(len(d[words[ij]]["meanings"])):
                        x=dict(d[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="e":
                    for il in range(len(e[words[ij]]["meanings"])):
                        x=dict(e[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="f":
                    for il in range(len(f[words[ij]]["meanings"])):
                        x=dict(f[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="g":
                    for il in range(len(g[words[ij]]["meanings"])):
                        x=dict(g[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="h":
                    for il in range(len(h[words[ij]]["meanings"])):
                        x=dict(h[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="i":
                    for il in range(len(i[words[ij]]["meanings"])):
                        x=dict(i[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="j":
                    for il in range(len(j[words[ij]]["meanings"])):
                        x=dict(j[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="k":
                    for il in range(len(k[words[ij]]["meanings"])):
                        x=dict(k[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="l":
                    for il in range(len(l[words[ij]]["meanings"])):
                        x=dict(l[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="m":
                    for il in range(len(m[words[ij]]["meanings"])):
                        x=dict(m[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="n":
                    for il in range(len(n[words[ij]]["meanings"])):
                        x=dict(n[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="o":
                    for il in range(len(o[words[ij]]["meanings"])):
                        x=dict(o[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="p":
                    for il in range(len(p[words[ij]]["meanings"])):
                        x=dict(p[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="r":
                    for il in range(len(r[words[ij]]["meanings"])):
                        x=dict(r[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="s":
                    for il in range(len(s[words[ij]]["meanings"])):
                        x=dict(s[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="t":
                    for il in range(len(t[words[ij]]["meanings"])):
                        x=dict(t[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="u":
                    for il in range(len(u[words[ij]]["meanings"])):
                        x=dict(u[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="v":
                    for il in range(len(v[words[ij]]["meanings"])):
                        x=dict(v[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="w":
                    for il in range(len(w[words[ij]]["meanings"])):
                        x=dict(w[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="x":
                    for il in range(len(x[words[ij]]["meanings"])):
                        a=dict(x[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+a["def"])
                elif wordss[ij][0].lower()=="y":
                    for il in range(len(y[words[ij]]["meanings"])):
                        x=dict(y[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])
                elif wordss[ij][0].lower()=="z":
                    for il in range(len(z[words[ij]]["meanings"])):
                        x=dict(z[words[ij]]["meanings"][il])
                        print("Defination number "+str(il+1)+" is "+x["def"])

ana(sys.argv[1])