import urllib.request
import re
import os
import urllib

def getHtml(url):#该函数获得网页源代码
    page=urllib.request.urlopen(url)
    html=page.read()
    return html.decode('UTF-8','ignore')

def getImg(html):#该函数实现从源代码中找到要爬中的视频链接或者图片地址等等关键信息，然后保存到本地
    reg = r'src="(.+?x-oss-process=style/240h)"  />'
    imgre = re.compile(reg,re.M)
    imglist = imgre.findall(html)

    #urlList=map(lambda x:'http:'+x,imglist)#如果源代码中的视频或者图片链接没有http:等请求头，请打开此项
    
    x = 0
    path = 'D:\\《Python程序文件》\\爬取到的图片'#内容存放在本地的文件夹路径
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
print (getHtml("https://www.quanjing.com/creative/topic/31"))#为了解决可能出现的一些问题，这里显示爬取到源代码，以此来比对开发者工具查看到的源码是否和真正爬取到的一致，修改正则表达式的时候以此为主
print("请打开文件夹查看视频或图片！")
