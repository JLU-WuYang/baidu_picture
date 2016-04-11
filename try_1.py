# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:34:27 2016

@author: Albert
"""

import urllib2
import re
import urllib
import os
def cbk(a, b, c): 
    '''回调函数
04
    @a: 已经下载的数据块
05
    @b: 数据块的大小
06
    @c: 远程文件的大小
07
    ''' 
    per = 100.0 * a * b / c 
    if per > 100: 
        per = 100 
    print '%.2f%%' % per
name=raw_input(u'输入贴吧名: ')
begin=int(raw_input(u'输入起始页: '))
end=int(raw_input(u'输入结束页: '))
os.mkdir('d://picture//'+name)
for a in xrange(begin,end+1):
    url=r'http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'%(name,50*(a-1))
    html=urllib2.urlopen(url)
    page=html.read()
    patten=re.findall('original="(.*?).jpg',page,re.S)
    i=1
    for line in patten:
        line=line+'.jpg'
        
        local = 'd://picture//%s//%d-%d.jpg'%(name,a,i)
        print "第%d页第%d张"%(a,i)   
        i=i+1
        urllib.urlretrieve(line, local, cbk)
   
