import requests
import random
import datetime
cookies = {
    '_ga': 'GA1.1.763349015.1701265994',
    'wnbell_last_count': '1',
    'pll_language': 'bg',
    '__wpdm_client': 'd72a32eeb062cd08e39786a0f47db4b4',
    '_ga_5LBFZ1MK81': 'GS1.1.1714041511.12.1.1714042535.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.763349015.1701265994; wnbell_last_count=1; pll_language=bg; __wpdm_client=d72a32eeb062cd08e39786a0f47db4b4; _ga_5LBFZ1MK81=GS1.1.1714041511.12.1.1714042535.0.0.0',
    'origin': 'https://ibex.bg',
    'priority': 'u=0, i',
    'referer': 'https://ibex.bg/%d0%b4%d0%b0%d0%bd%d0%bd%d0%b8-%d0%b7%d0%b0-%d0%bf%d0%b0%d0%b7%d0%b0%d1%80%d0%b0/%d0%bf%d0%b0%d0%b7%d0%b0%d1%80%d0%b5%d0%bd-%d1%81%d0%b5%d0%b3%d0%bc%d0%b5%d0%bd%d1%82-%d0%b4%d0%b5%d0%bd-%d0%bd%d0%b0%d0%bf%d1%80%d0%b5%d0%b4/aggregated-curves-bg/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
# promqna da datata i chasa
data = {
    'date': '2024-04-20',
    'singleHour': '14',
}
date = datetime.datetime.now()
day=str(date.year)+'-'+str(date.month)+'-'+str(date.day)+ "_"+str(date.hour)
giantForFlag=0
# data['date']= "2024-"+str(random.randint(2, 4))+"-"+str(random.randint(8, 29))
# data['singleHour']=str(random.randint(0, 23))
# day=  data['date']+ "_"+data["singleHour"]
# data['date']="2024-4-12"
# data['singleHour']='15'
# day="2024-4-12_15"
while True:
    data['date']=str(date.year)+'-'+str(date.month)+'-'+str(date.day)
    data['singleHour']=str(date.hour)

    response = requests.post(
        'https://ibex.bg/%d0%b4%d0%b0%d0%bd%d0%bd%d0%b8-%d0%b7%d0%b0-%d0%bf%d0%b0%d0%b7%d0%b0%d1%80%d0%b0/%d0%bf%d0%b0%d0%b7%d0%b0%d1%80%d0%b5%d0%bd-%d1%81%d0%b5%d0%b3%d0%bc%d0%b5%d0%bd%d1%82-%d0%b4%d0%b5%d0%bd-%d0%bd%d0%b0%d0%bf%d1%80%d0%b5%d0%b4/aggregated-curves-bg/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    # print(response.content)
    TrimedS = str(response.content).replace(";\\t\\t\\t\\t\\t\\t\\t\\t\\r\\n\\t\\tvar","")
    TrimedS =TrimedS.replace("=",":")
    TrimedS = TrimedS.replace(";\\r\\n\\t\\tvar","")

    file = open('myfile.txt', 'w')
    file.write(TrimedS)
    file.close()
    keyWords=["sellData","buyData","[","]"]
    count=[0,0]
    flag =0
    flagEnd =0
    with open("myfile.txt", 'r') as file:
        for line in file:
    
            # reading each word        
            for word in line.split():
                if(word!=keyWords[0] and flag==0):
                    count[0]=count[0]+1
                else: flag=1
                if(word!=keyWords[3]):
                    count[1]=count[1]+1
                elif(flagEnd<1):
                    flagEnd= flagEnd+1
                    count[1]=count[1]+1
                else: break
            masivOtDumi= line.split()
            file1 = open("final.txt", 'w')
            file1.write("{")
            try:
                for i in range(count[0],count[1]+1):
                    if(masivOtDumi[i]=="buyData"):
                        file1.write(", ")
                    file1.write(masivOtDumi[i])
                file1.write("}")
            except:
                print("Nqma takava data")
                giantForFlag= giantForFlag+1
    file1.close()           
    file.close()
    if(giantForFlag==3):
        break
    
    
    day=  data['date']+ "_"+data["singleHour"]
    jsonName = str(day)+".json"
    print(day)
    jF= open(jsonName,"w")
    with open('final.txt',"rb") as f:
        
        while True:
            c = f.read(1).decode("utf-8")
            if not c:
                break
            if(c=='x'):
                jF.write("\"")
                jF.write(c)
                jF.write("\"")
            elif(c=='y'):
                yC = f.read(1).decode("utf-8")
                if(yC=='D'): 
                    jF.write(c)
                    jF.write(yC)
                else:
                    jF.write("\"")
                    jF.write(c)
                    jF.write("\"")
                    jF.write(":")
            elif(c=='s'or c=='b'):
                jF.write("\"")
                jF.write(c)
            elif(c=='a'):
                d = f.read(1).decode("utf-8")
                if(d!='t'):
                    jF.write(c)
                    jF.write("\"")
                    jF.write(":")
                else: 
                    jF.write(c)
                    jF.write(d)
            elif(c=='{' or c=='['):
                jF.write(c)
                jF.write("\n")
            elif(c=='}'):
                jF.write("\n")
                jF.write(c)
            elif(c==','):
                comma = f.read(1).decode("utf-8")
                if(comma==']'):jF.write("\n")
             
                else:
                    jF.write(c)
                    jF.write("\n")
                f.seek(-1, 1)
            else:jF.write(c)
    f.close()
    jF.close()
    date = date - datetime.timedelta(hours=1)