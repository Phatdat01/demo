#text='àáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ'
import re

def Replace(text):
    text=re.sub('[àáãạảăắằẳẵặâấầẩẫậ]','a',text)
    text=re.sub('[èéẹẻẽêềếểễệ]','e',text)
    text=re.sub('[ìíĩỉị]','i',text)
    text=re.sub('[òóõọỏôốồổỗộơớờởỡợ]','o',text)
    text=re.sub('[ùúũụủưứừửữự]','u',text)
    text=re.sub('[ỳỵỷỹý]','y',text)
    text=re.sub('[đ]','d',text)
    text=re.sub('[ÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬ]','A',text)
    text=re.sub('[ÈÉẸẺẼÊỀẾỂỄỆ]','a',text)
    text=re.sub('[Đ]','D',text)
    text=re.sub('[ÌÍĨỈỊ]','I',text)
    text=re.sub('[ÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢ]','O',text)
    text=re.sub('[ÙÚŨỤỦƯỨỪỬỮỰ]','U',text)
    text=re.sub('[ỲỴỶỸÝ]','Y',text)

    return text

text="Tui là ai mà phải có mèo số nhọ hoàn mĩ Ánh mắt xịn sò"

print(Replace(text))