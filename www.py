import requests,json
def res():
 # url='https://www.baidu.com'
 response=requests.get(url=url)
#     # print(response.text)
#     # return response
#     '''post方案'''
#     data={"name":"liu","password":"123456"}
#     reponse=requests.post(url=url,data=data)
#     a=json.dumps(data)
#     print(type(a))
#     return a
# res()
# sys.setdefaultencoding('utf-8')

# import urllib.request
# #
# #
# # url = 'http://www.baidu.com/'
# # res = urllib.request.urlopen(url=url)
# # print(res.status)
# import requests,json
# url="http://www.baidu.com"
# res=requests.get(url)
# res.encoding="utf-8"
# # print(res.text)
# js_str = json.dumps(res.text)
# print(js_str)
# import urllib,urllib3