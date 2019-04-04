'''
准备工作
安装request
安装lxml
安装命令：pip install xxx
'''

# 导入一些工具包
import requests
from lxml import etree
from pandas import DataFrame

# 确定一个对象，网址,关键词：数据分析
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
res = requests.get(url)
res.encoding = 'gbk'
# 定义节点树的根
root = etree.HTML(res.text)
# 利用xpath查找网页信息
position = root.xpath('//div[@class="el"]/p/span/a/@title')
company = root.xpath('//div[@class="el"]/span/a/@title')
place = root.xpath('//div[@class="el"]/span[@class="t3"]/text()')
salary = root.xpath('//div[@class="el"]/span[@class="t4"]/text()')
# 隶属于Pandas，数据框，类似于Excel
jobInfo = DataFrame([position, company, place, salary]).T
jobInfo.columns = ['职位名', '公司名', '工作地点', '薪资']
jobInfo.head(10)
print(jobInfo)
