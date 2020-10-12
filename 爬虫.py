import urllib.request,os,re


def 获得html(url):
    源码=urllib.request.urlopen(url)
    html源码=源码.read()
    return html源码.decode('utf-8')

def 获取图片(html源码):
    正则 = 'src="(.+)\?x-oss-process=style/240h"'
    list = re.compile(正则,re.M)
    图片列表 = list.findall(html源码)
    路径 = r'D:\《Python程序文件》\爬取到的图片'
    路径1 = 路径+'\\'
    if not os.path.isdir(路径):
        os.makedir(路径)
    print(图片列表)
    x = 0
    for 图片url in 图片列表:
        urllib.request.urlretrieve(图片url,'{}{}.jpg'.format(路径1,x))
        x=x+1
    #return 图片列表
获取图片(获得html("https://www.quanjing.com/creative/topic/31"))
print('请打开文件夹查看！！！')
