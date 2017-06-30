import lxml.html as html
from pandas import DataFrame
import requests
from lxml import etree

dn_technopoint = 'https://technopoint.ru'
url_technopoint_page = '%s/catalog/17a7561d16404e77/videokarty/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }


page = requests.get(url_technopoint_page % (dn_technopoint), headers = headers)

tree = html.fromstring(str(page.text))

list_card_xpath = tree.xpath('//div[@class = "node-block"]/div[@class = "product"]')


for i in list_card_xpath:
    print(etree.tostring(i))
    data_code = i.xpath('//div[@class = "product"]/div/div/div/a/@href')
    print(data_code)
    for j in data_code:
        print(j)

with open('test.html', 'bw') as output_file:
    output_file.write(page.text.encode('utf-8'))




