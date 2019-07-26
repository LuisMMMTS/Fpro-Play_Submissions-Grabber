#requires html2text--you can install through pip command
import requests
import html2text
import os
import sys
html2text.HTML2Text().ignore_links = False #in case your code has a weblink the parser wont ignore them
session = requests.session()

print('Enter username and token or just the login link sent by FPRO Team')
username =input("username_ex:up201808912"+" "+":")
token =input('from "token=" TO THE END OF THE LINK->EX: vOlMPQ99eIB0cBumyX-yvbUD2glgsk10fKSmxJmeeVE"'+" "+":")
link=input("link"+" "+":")


def fpro__login_and_html(username,token,link):
    if token!="" and (" " not in token):
        list_text = session.get('http://fpro.fe.up.pt/play/?username=%s&token=%s' % (username, token)).text
        list_text=list_text.split("\n")
        return list_text
    elif link=="":
        sys.exit("wrong inputs")
    else:
        list_text = session.get(link).text
        list_text=list_text.split("\n")
        return list_text

def exercises_links(list_text):
    new_list=[]
    links=[]

    for i in range(len(list_text)):
        if list_text[i]=="<s>":
            new_list.append(i)

    for i in new_list:
        links.append(list_text[i+1])

    for i in links:
        pasta=i.split("/")[2]
        file=i.split(">")[1]
        file=file.split("<")[0]
        file=html2text.html2text(file)
        file=file.replace('\\',"")
        file=file.replace("\n","")
        new_link=i.split('"')[3]
        new_link="http://fpro.fe.up.pt"+new_link
        writing(pasta,file,new_link)
    
    
    
def writing(pasta,file,link):
    current_path=sys.argv[0]
    if not os.path.isdir(str(sys.argv[0]).replace(os.path.basename(sys.argv[0]),"")+pasta):
        #file=open(pasta+"/"+file+".txt","w")
        os.makedirs(pasta)
    #else:
        #os.makedirs(pasta)
    file=open(pasta+"/"+file+".py","w",encoding = 'utf-8')
    code = session.get(link).text
    code = code.split("\n")
    for i in range(len(code)):
        if '<p class="lead">' in code[i]:
            comment=code[i].split("<p>")[1]
            comment=code[i].split("</code>")
        if '<textarea name="code"' in code[i]:
            try:
                codigo=code[i].split("autofocus disabled>")[1]
            except:
                codigo=code[i].split("autofocus>")[1]
            codigo=html2text.html2text(codigo)[:-2]
            j=i
            while "</textarea>" not in code[j]:
                codigo+='\n'
                j+=1
                p=0
                while code[j]!="" and (p in range(len(code[j]))) and (code[j][p]=='\t' or code[j][p]==' '):
                    if code[j][p]=='\t':
                        codigo+='\t'
                    codigo+=" "
                    p+=1
                codigo+=html2text.html2text(code[j][p:])[:-2]
            if "</textarea>" in codigo:
                codigo=codigo.split("</textarea>")[0]
#            codigo=html2text.html2text(str(codigo)[1:-1])
            comment=html2text.html2text(str(comment)[1:-1])
    file.write('"""'+comment+'"""'+2*('\n'))
    file.write(codigo)
    file.close()
            
            
exercises_links(fpro__login_and_html(username,token,link))
