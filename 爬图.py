import urllib.request
import re
import os
import urllib

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html.decode('UTF-8','ignore')

def getImg(html):
    reg = r'src="(.+?x-oss-process=style/240h)"  />'
    imgre = re.compile(reg,re.M)
    imglist = imgre.findall(html)

    #urlList=map(lambda x:'http:'+x,imglist)
    
    x = 0
    path = 'D:\\《Python程序文件》\\爬取到的图片'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path+'\\'

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{0}{1}.jpg'.format(paths,x))
        x = x + 1
    #return urlList
    return imglist
html = getHtml("https://www.quanjing.com/creative/topic/31")
print (getImg(html))
print (getHtml("https://www.quanjing.com/creative/topic/31"))
print("请打开文件夹查看视频或图片！")
