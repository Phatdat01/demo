from pyvi import ViTokenizer, ViPosTagger

print(ViTokenizer.tokenize(u"Trường đại học bách khoa hà nội"))

print(ViPosTagger.postagging(ViTokenizer.tokenize(u"Trường đại học Bách Khoa Hà Nội")))

from pyvi import ViUtils
print(ViUtils.remove_accents(u"Trường đại học bách khoa hà nội"))

from pyvi import ViUtils
print(ViUtils.add_accents('truong dai hoc bach khoa ha noi'))