import requests
from bs4 import BeautifulSoup

re = requests.get('http://www.businessweekly.com.tw/channel.aspx?id=0000000187&p=30')
#print (re.status_code)
#print (re.text)

soup = BeautifulSoup(re.text, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup)

#table_list = soup.find_all('div',{'class':'one-fourth'})
#for i in table_list:
#    print(table_list[i])