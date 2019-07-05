import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_html(url):
    #获取网址内容
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    loge = url.find(".apk") + url.find(".exe") + url.find("itunes.") + url.find("play.google") + url.find("taobao.com") + url.find("nero") + url.find("umeng.")
    null = ""
    if loge == -7:
        r = requests.get(url)
        r.encoding = 'utf-8'
        data = r.text
        #print(data)
        return data
    else:
        return null


def find_link_list(url):
    # 利用正则查找所有超连接
    link_lists = []
    href_link_list = re.findall(r"href=\"[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\"", url)
    for urls in href_link_list:
        #print(urls)
        link_lists.append(urls[6:-1])
    return link_lists


def merge_link(str1, str2):
    full_link = ""
    while (str2.find("../") + 1):
        str1 = str1[0:str1.rfind("/")]
        str2 = str2[3:]
        full_link = str1 + "/" + str2
        #print(full_link)
    return full_link

def check_link_list(urls):
    #检查并补全url
    full_link_list = []
    for url in urls:
        link_lists = find_link_list(get_html(url))

        for link in link_lists:
            if link.find(".css") == -1:
                if "http" in link:
                    #print(link)
                    full_link_list.append(link)
                    pass
                else:
                    print(url)
                    print(link)
                    if link.find("../") == -1:
                        link = url[0:url.rfind("/") + 1] + link
                        #print(link)
                        full_link_list.append(link)
                    else:
                        link = merge_link(url, link)
                        #print(link)
                        full_link_list.append(link)
            else:
                pass
        else:
            pass

    return full_link_list


url = ["https://taobao.swiftlink.mobi/index.html"]
i = 3

while i > 0:

    url = check_link_list(url)
    url = list(set(url))
    print("不要着急，正在工作")
    i = i - 1

num = 0
for list in url:
    #print(list)
    num += 1
print(num)


'''
for url in final_link_list:
    url = [url]
    length = len(url)
    url_result_success = []
    url_result_failed = []
    for i in range(0, length):
        try:
            response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
            if response.status_code != 200:
                raise requests.RequestException(u"Status code error: {}".format(response.status_code))#引出请求时出现歧义异常
        except requests.RequestException as e:
            url_result_failed.append(url[i])
            result_failed_len = len(url_result_failed)
            for i in range(0,result_failed_len):
                print('URL-->  %s' % url_result_failed[i].strip()+' -->死链接')
            continue
        url_result_success.append(url[i])
    
    result_success_len = len(url_result_success)
        
    for i in range(0, result_success_len):
        print('URL-->  %s' % url_result_success[i].strip()+' -->活链接')
'''

