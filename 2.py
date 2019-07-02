def merge_link(str1, str2):
    full_link = ""
    while (str2.find("../") + 1):
        str1 = str1[0:str1.rfind("/")]
        str2 = str2[3:]
        full_link = str1 + "/" + str2

    return full_link


str2 = "../../index-cn.html"
str1 = "http://www.1001tvs.com/faq/cn"

full_link = merge_link(str1, str2)
print(full_link)