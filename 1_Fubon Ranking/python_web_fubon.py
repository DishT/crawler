from urllib.request import urlopen
from bs4 import BeautifulSoup
import time 
#nameList = []
fubon_data = []
def crawler(url):
    base_url = 'http://ambassador.fuboncharity.org.tw/project/inside/'
    search_url = base_url + str(url)
    html = urlopen (search_url)
    bsObj = BeautifulSoup(html,"html5lib")
	# 抓主題名稱
    nameList = (bsObj.findAll('span',{"class":"in_title"}))
		
	#nameList.append(bsObj.find('table',{"class":"ticket"}))
    #print(type(nameList))
    nameList = str(nameList).replace("</span>]","").strip(" ").split("</i>")[1]
    #print(nameList)
	
    #抓票數
    numberList = (bsObj.findAll('tr',{"class":"ticket"}))
    #print(str(numberList[0].get_text()).strip(" "))
    #print(str(numberList[0].get_text()).strip(" ").find("3"))
    numberList = str(numberList[0].get_text())
    numberList = numberList[35]+numberList[47]+numberList[59]+numberList[71]
    numberList = int(numberList)
    #print(numberList)
    #儲存名字與票數
    
    fubon_data.append([nameList,numberList])
    return fubon_data

def tickets(fubon_data):
    #print (fubon_data[1])
    return fubon_data[1]

def sort_data(fubon_data):
    data_sort = sorted(fubon_data, key = tickets, reverse = True)
    return data_sort
def file_store(fubon_data):
    tmp = ""
    file = open('fubon_'+num+".txt",'w')
    for i in range(15):
        tmp = str(fubon_data[i][0]+" "+str(fubon_data[i][1])+"\n") 
        file.write(tmp)
    file.close()  
    num +=1
    # 11,23,35,47,59,71 
    #url = nameList[17].get_text()
	#return url

def time_count():

    time_str = time.ctime()
    time_str = time_str.split()
    time_str = time_str[1]+"/"+time_str[2]+"/"+time_str[4]
    return time_str
num = 0
for i in range(186, 416):
    try :
        if i < 415:
            crawler(i)
        else:
            fubon_data = crawler(i)
    except:
        continue

#print (fubon_data)
data_sort = sort_data(fubon_data)

#print(data_sort)

for i in range (15):
    if i ==0:
        print("名次",(i+1),": 票數",data_sort[i][1],"名稱",data_sort[i][0])
    else:
        print("名次",(i+1),": 票數",data_sort[i][1], "差距：",(data_sort[i-1][1]-data_sort[i][1]),"名稱: ",data_sort[i][0])

file_store(data_sort)

