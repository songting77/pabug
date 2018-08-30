import urllib
from urllib import request, parse
import json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'CONNECTION': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'UM_distinctid=164e8ae6d01136-00875663a887d9-47e1039-ff000-164e8ae6d02b2; __gads=ID=5a88c84944b521a8:T=1532912101:S=ALNI_MZslljqqUpoLP74vLLGTWTCk3dB_w; vjuids=-56c2e65dd.164e8ae747b.0.74b916e8b116f; vjlast=1532912105.1532912105.30; _ntes_nnid=4e8d1a49ca3ff5edcdf6cb65ebec5e74,1532912104645; _ntes_nuid=4e8d1a49ca3ff5edcdf6cb65ebec5e74; vinfo_n_f_l_n3=45296e86dcedd6f4.1.0.1532912104654.0.1532912131824; _iuqxldmzr_=32; __utma=94650624.1023808705.1534147091.1534147091.1534147091.1; __utmc=94650624; __utmz=94650624.1534147091.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=FN8%2BsApINa7BuPXJF7VHjKPIqOqR2Dvi; WM_NI=xzqxwXXhd9GGSFlJIQuo1cPIbifTcIjqlgfo4sZcOWZoVZ8d%2B9holuQsbANJTlFPuNlm28D24yLeFc90vT393JbhevpnM%2BXKcQVphSPW%2F3XEo%2B3TiLHuRxoi2%2Byqpn6AeXI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7c74e869f81d9e441879fa68fcf47b2a7aa99c86fa39999b9e43daa959fa8c12af0fea7c3b92abca6bf99f6549cb8acdac64d919aa4abcc5bb7b1ff84d343a2b7aab5e243aaafa488e565f8ad9684ce5d9ab19abbbb70e9e7a890ef7f93adaea2cd4298b48ab1f846b0b3fed9c73af8a78486c569fbf0bab5b233f196ae89e87eb4b283ccdb41a18f9a91eb599489e1d4db4fadf5fdb5ec488cab9e99ee63f2f5b792f366f69fabb9cc37e2a3; JSESSIONID-WYYY=GXI6%2B9beP0YvwfV27xDDxlJYCyjYX%5C%5CkRaVsQ%5C552JbjC98uo%5C5Brw3iNB64ZBffB5gvldCeYM%5CixfZG2kOlNAvwX5BccW58zw%5Cynxa3sj8oc8XYY5ehGf%2FHPrwyUzlFTO4i%5CHTRl%5CbPGCCkbGYs%2Bva2aekzA9sB2Q%2B6NxvcKh178zZ0%3A1534152370882',
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='

'''
需要找对网址，正确的网易云音乐地址在XHR中的倒数‘url?csrf_token=’ 文件中
在Preview 选项卡中的data数据下有个url，这是正确的音乐链接地址
而我们所需要的是请求头中的RequsetURL中的地址
'''
url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
'''
在头文件信息中的最底部可以看到form Data数据，这是Resquset中必要的加密data
'''
data = {
    'params': 'ru6buYFFFC1npTRUMYlVCtTYAbCSTfrmlNMl0YcCctylnNmx5IcI6eUeaTgpcvugTa1snTjKifvDVIEUaupzwqMVW4y84atxDxdJsbGi2pDlWOZ38Bj1gEFLh9GwHK5H',
    'encSecKey': '3ce0af42809838a67d5c12fac94cec35ff09c5880cb8cf3ef51497274eb7a91ae1bd913814afe7b19fcde558830b1cd23f5bdbedd6d9709f452c3a92c98035f44193d990947852a0f42cb3952d2cf212f725426b71be46448d7a4c1fe107622a1116582f2e56f2af709460193c7a7b688951c4207a1d3675e5aba481b655c832',
}
# url方式加密
data = urllib.parse.urlencode(data).encode('utf-8')
# 对Resquest方法传参 请求头是为了模拟浏览器访问服务器
req = urllib.request.Request(url, data, headers)
# 打开请求的访问网址，得到一个文本文件，使用read方法读取文件内容，通过网页的编码格式读取到正确的信息
response = urllib.request.urlopen(req).read().decode('gb2312', 'ignore')
# 打印得到的响应，就可以得到网页中Preview 中的格式化的json 数据
# print(response)
# 得到data中的url网址  json.loads加载json
'''
['data']  单纯加载json的响应数据并显示data数据是大data中的列表对象
['data'][0]  打印歌曲id和地址{'id': 531655610, 'url': 'http://m10.music.126.net/20180813211452/dc8b85b57f922ff9af3ecf3cd7c6bc2f/ymusic/3773/700a/c820/a139e5a35466639cebdfa7ad3030af3b.mp3',
['data'][0]['url'] 提取其中的url
最后得到的是一个歌曲的地址
'''
musicUrl = json.loads(response)['data'][0]['url']
print(musicUrl)
'''
打开一个文件，命名为你想要的文件名和后缀，使用wb写方法二进制写入并重名为f
使用urlopen打开音乐的地址，并读取出来
read（）的方法显示的就是十六进制
再把读出的数据写进文件就是下载文件了
'''
with open('dura.mp3', 'wb')as f:
    res = urllib.request.urlopen(musicUrl).read()
    f.write(res)
