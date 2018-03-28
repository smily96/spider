import requests
from lxml import etree


url_img = 'https://www.zhihu.com/question/47252185/answer/300534139'

headers_base = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

response = requests.get(url=url_img,headers=headers_base)

html = etree.HTML(response.text)

url_img_list = html.xpath("//div[@class='RichContent-inner']//figure//img/@src")

# for one_img in url_img_list:
#     print(url_img_list[6])
    # response = requests.get(url=one_img,headers=headers_base)
    #
    # file_name = one_img.split("-")[-1]
    #
    # with open(file_name,'wb') as f:
    #     f.write(response.content)


for i in range(275):
    print("第%d次："%i,url_img_list[i])