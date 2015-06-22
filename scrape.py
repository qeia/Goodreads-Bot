__author__ = 'Sid'
key='DFVpTYLt67bVxlSdd8KfQ'
import urllib2
from xml.dom import minidom
def parser(url):
    dic={}
    new=url+'?key='+key
    obj=urllib2.urlopen(new)
    doc=minidom.parse(obj)
    dic["id"]=doc.getElementsByTagName("id")[0].firstChild.data
    dic["isbn"]=doc.getElementsByTagName("isbn")[0].firstChild.data
    dic["title"]=doc.getElementsByTagName("title")[0].firstChild.data
    dic["author"]=doc.getElementsByTagName("name")[0].firstChild.data
    return dic


