import requests
import json
from pprint import pprint 
from bs4 import BeautifulSoup

url="https://affyo.com/networks/gamblingpro/"
page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")

def scrape():
    list1=[]
    # 1st
    main_dic={}
    table=soup.find('table',id="ne-ca-ra",class_="ne-ca-ta")
    tr=table.find_all('tr')
    c=1
    dic1={}
    for i in tr:
        if c>1:
            positions=i.find("th").get_text()
            # print(positions)
            value=i.find("td",class_="ce").get_text()
            # print(value)
            dic1[positions]=value
        c=c+1
    main_dic["Rating"]=dic1
    # list1.append(dic2)
    # print(dic2)

    # 2nd

    dic2={}
    table=soup.find('table',id="ne-ca-me",class_="ne-ca-ta ne-ta")
    tr=table.find_all('tr')
    # print(tr)
    c=1
    for i in tr:
        if c>1:
            positions=i.find("th").get_text()
            value=i.find("td").get_text()
            dic2[positions]=value
        c=c+1
    main_dic["Contact"]=dic2
    # list1.append(main_dic)
    # pprint(list1)

    # 3rd
    dic3={}
    table=soup.find('table',id="ne-ov-3-ta",class_="ne-ta")
    tr=table.find_all('tr')
    c=1
    for i in tr:
        if c>1:
            positions=i.find("th").get_text()
            value=i.find("td").get_text()
            dic3[positions]=value
        c=c+1
    main_dic["tracking"]=dic3
    # list1.append(main_dic)
    # print(list1)

    # 4th
    dic4={}
    table=soup.find('table',id="ne-ov-ta",class_="ne-ta")
    tr=table.find_all('tr')
    c=1
    for i in tr:
        if c>1:
            positions=i.find("th").get_text()
            value=i.find("td")
            span=value.find_all("span",class_="ne-ta-la")
            a=[]
            for h in span:
                span_value=h.find("a").get_text()
                a.append(span_value)
            dic4[positions]=a
        c=c+1
    main_dic["Offers"]=dic4
    # list1.append(main_dic)
    # print(list1)

    # 5th
    dic5={}
    table=soup.find('table',id="ne-ov-2-ta",class_="ne-ta")
    tr=table.find_all('tr')
    c=1
    for i in tr:
        if c>1:
            positions=i.find("th").get_text()
            value=i.find("td")
            span=value.find_all("span",class_="ne-ta-la")
            a=[]
            for h in span:
                span_value=h.find("a").get_text()
                a.append(span_value)
            dic5[positions]=a
        c=c+1
    main_dic["Payment"]=dic5
    list1.append(main_dic)
    print(main_dic)

    file1=open("imdb_project.json","w")
    file2=json.dump(main_dic,file1,indent=6)
    file1.close()



      

scrape()