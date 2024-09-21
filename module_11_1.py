# Обзор сторонних библиотек Python
import requests
import pandas
import numpy
import matplotlib.pyplot
from PIL import Image

'requests'
r = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
print(1, r.encoding)
print(2, r.content)
print(3, r.text)
print(4, r.json())
print(5, r.raw)
print(6, r.status_code)
print(10, r.headers)
print(11, r.history)

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(7, r)
print(8, r.text)
print(9, r.json())
print(10, r.headers)
print(11, r.history)

'pandas'
dict_ = {'a': 1, 'b': 2, 'c': 3}
s = pandas.Series(data=dict_, index=['a', 'b', 'c'])
print(s)
c = pandas.Series(data=dict_, index=['q', 'w', 'e'])
print(c)
print(c.empty) # проверка на пустоту
print(c.hasnans) # проверка на NaN
file = 'for_pandas.xlsx'
new_file='new_file_pandas.xlsx'
xl = pandas.read_excel(file) # чтение файла
print(xl.head(3))
xl_new = pandas.DataFrame(xl.sum().round(1)) # сохранение вычислений в новый файл
print(xl_new.head(3))
xl_new.to_excel(new_file)

'numpy'
a = numpy.array([1, 2, 3, 4, 5, 6])
print(1, a)
a[0] = 7
print(2, a)
a[0:] = 8
print(3, a)
print(4, a.ndim) # проверка количества измерений
b = numpy.array([[5, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(5, b)
print(6, b.ndim)
c = numpy.array([[[1, 2, 3]*3],[[4, 5, 6]*3] ])
print(7, c)
print(8, c.ndim)
d = numpy.arange(6)
print(9, d)
print(10, d.ndim)
e = numpy.sort(b)
print(11, e)
q = numpy.concatenate((a,d))
print(12, q)
print(13, (i:=(a + d)))
print(14, b.sum())
print(15, q*2)
print(16, c.max())
print(17, a.reshape(3,2))
print(18, b.transpose())
print(19, numpy.flip(b))

'matplotlib'
# странная парабола
a = b = c = 1
x_list = list(range(-100, 100))
y_list = []

for i in x_list:
    int_x = x_list[i]
    y = a * (int_x ** 2) + b * int_x + c
    y_list.append(y)

matplotlib.pyplot.plot(x_list, y_list)
matplotlib.pyplot.show()

'PIL'
img_file_1 = 'kosmonavt.jpg'
img_file_2 = 'nature.jpg'

im_1 = Image.open(img_file_1)
im_2 = Image.open(img_file_2)

#создаём пустую картинку
new_image = Image.new('RGB',(2*im_1.size[0], im_1.size[1]), (250,250,250))

#вставляем изображения
new_image.paste(im_1,(0,0))
new_image.paste(im_2,(im_1.size[0],0))

new_image.save("image.bmp","BMP")

new_image.show()