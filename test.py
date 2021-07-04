from bs4 import BeautifulSoup
import urllib.request
import csv

# 把网址 URL 存在变量里
# urlpage =  'https://www.similarweb.com/top-websites/category/e-commerce-and-shopping/'

# 获取网页内容，把 HTML 数据保存在 page 变量中
# page = urllib.request.urlopen(urlpage)
# 用 Beautiful Soup 解析 html 数据，并保存在 soup 变量里
# soup = BeautifulSoup(page, 'html.parser')


#读取本地文件
page = "./top_shopping_website.html"
# 用 Beautiful Soup 解析 html 数据，并保存在 soup 变量里
soup = BeautifulSoup(open(page, encoding='utf-8'), 'html.parser')

# print(soup)

# 在表格中查找数据
table = soup.find('table', attrs={'class': 'topRankingGrid-table'})
results = table.find_all('span', attrs={'class': 'topRankingGrid-titleName'})
print('Number of results', len(results))
# 提取标签中的文字并输出到文档中
for i in results:
    f = open("data.txt",'a')
    f.write(i.get_text())
    f.write("\n")

