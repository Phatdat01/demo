from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from underthesea import sent_tokenize,word_tokenize,pos_tag,chunk,ner,classify

text="Giang Hạo xuyên qua phổ thông nhân gia, bị ép bán nhập ma môn, trở thành Ma Môn đệ tử.Vốn định an tâm tu luyện một chút mạnh lên, tốt tại tu chân giới sinh tồn được, nhưng lại bị một vị nữ ma đầu 'Đủ kiểu nhục nhã' . Thực lực chênh lệch cách xa, hắn chỉ có thể nhẫn nhục sống tạm bợ, hi vọng không cần gặp được đối phương. Không có có chỗ dựa hắn đạt được Ma Môn chưởng giáo ưu ái, có thể an tâm tu luyện, khi hắn thành vi thủ tịch đệ tử gặp mặt chưởng giáo lúc, lại sững sờ tại tại chỗ. Nhìn đối phương tuyệt mỹ khuôn mặt, hắn có chút cười không nổi, đây không phải lúc trước cái kia nữ ma đầu sao?"

# divide into sentences
print(sent_tokenize(text))
#divide into word clusters
print(word_tokenize(text))
# determined role of words
print(pos_tag(text))
# define setences, which
print(chunk(text))
#define stop word
print(ner(text))
#define type of subtite 
print(classify(text))
# print(word_tokenize(text))

# le = LabelEncoder()
# words = ['anh', 'chị','em', 'cha', 'mẹ']
# le.fit(words)

# print('Class of words: ', le.classes_)
# # Convert to num
# x = le.transform(words)
# print('Convert to number: ', x)
# # Convert to class
# print('Invert into classes: ', le.inverse_transform(x))

# #Onehot Processing
# oh = OneHotEncoder()
# classes_indices = list(zip(le.classes_, np.arange(len(le.classes_))))
# print('Classes_indices: ', classes_indices)
# oh.fit(classes_indices)
# print('One-hot categories and indices:', oh.categories_)
# # Biến đổi list words sang dạng one-hot
# words_indices = list(zip(words, x))
# print('Words and corresponding indices: ', words_indices)
# one_hot = oh.transform(words_indices).toarray()
# print('Transform words into one-hot matrices: \n', one_hot)
# print('Inverse transform to categories from one-hot matrices: \n', oh.inverse_transform(one_hot))
