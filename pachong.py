import requests
import re
from bs4 import BeautifulStoneSoup,BeautifulSoup
import time


url ='https://www.hqu.edu.cn/index/hdxw.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.36;'
    }


def get_news():
    
    #get网页 不知道为什么.content再decode就可,直接content = requests.get(url,headers=headers).text反而乱码？
    content = requests.get(url,headers=headers)
    content.enconding = 'utf-8'

    content_new = content.content
    text = content_new.decode("utf-8")

    #解析
    soup =BeautifulSoup(text,features='html5lib')
    all_news = soup.findAll('ul',attrs={'class':'list_box_wz_list'})

    for all_new in all_news:
        with open("output.html", "w", encoding="utf-8") as f:
            f.write(str(all_new))
    # 使用正则表达式去除<span>标签
    with open('output.html', 'r', encoding='utf-8') as file:
        html = file.read()
    html = re.sub(r'<\s*span\s*[^>]*>.*?<\s*/\s*span\s*>', '', html)
    # 生成新的HTML文件
    with open('/root/myproject/templates/hdxw.html', 'w', encoding='utf-8') as file:
        file.write(html)


def get_news2():
    
    interval = 5
    while True:
        get_news()
        print('爬取网页%s' % url)
        time.sleep(interval)
get_news2()