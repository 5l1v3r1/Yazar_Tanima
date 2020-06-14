import pandas as pd
from keras.utils import np_utils

dataset = pd.read_csv("clear_data.csv")


dataset.rename(columns = {'10' : 'Cümle Sayısı', '187' : 'Kelime Sayısı',
                       '149' : 'Farklı Kelime Sayısı', '1' : 'Ünlem Sayısı',
                       '10.1' : 'Nokta Sayısı', '5' : 'Virgül Sayısı',
                       '0' : 'Soru İşareti', '0.1' : 'İki Nokta',
                       '94' : 'İsim Sayısı', '44' : 'Fiil Sayısı',
                       '11' : 'Sıfat Sayısı', '3' : 'Zamir Sayısı',
                       '0.2' : 'Zarf Sayısı', '0.3' : 'Bağlaç Sayısı',
                       '1.1' : 'Edat Sayısı', '2' : 'Zaman Belirten Kelime Sayısı',
                       '7' : 'Sayı İçeren Kelime Sayısı', '7.1' : 'Özel Kelime Sayısı',
                       '0.4' : 'Kısaltma Sayısı', '0.5' : 'Soru Sayısı',
                       'adnandincer' : 'Yazar İsmi'}, inplace = True)
x = dataset.drop(columns = ['Yazar İsmi'])
y = dataset[['Yazar İsmi']]

#Çıktıyı kategorik veriye dönüştür
from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)
y = np_utils.to_categorical(y)

#Eğitim ve veri testi ayrıldı
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 2)

#Z-Score Normalizasyon işlemini gerçekleştir
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


from keras import layers
from keras import models
import keras as keras

model = models.Sequential()


model.add(layers.Dense(128, activation = 'relu', input_shape = (20,)))
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dense(8, activation = 'softmax'))
from keras import optimizers
model.compile(optimizer = optimizers.Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])



x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = y_train[:1000]
partial_y_train = y_train[1000:]

history = model.fit(partial_x_train, partial_y_train, epochs=20, batch_size = 25, validation_data=(x_val, y_val))




print(model.evaluate(x_test,y_test))

import numpy as np
#Yazının veri seti içerisindeki özelliklerini dizi olarak vererek tahmin sonucunu görebiliriz.
prediction = sc.transform(np.array([31,428,353,3,35,25,2,5,221,98,17,15,0,1,4,9,7,12,4,2]).reshape(1,20))
predict = model.predict(prediction)
predict_class = model.predict_classes(prediction)[0]
print(predict_class)

#Author's IDs:
#0 >>> Adnan Dinçer
#1 >>> Ahmet Tan
#2 >>> Ali Sirmen
#3 >>> Emre Kongar-
#4 >>> Erol Manisalı
#5 >>> Hilmi Türkay
#6 >>> Mustafa Balbay
#7 >>> Orhan Bursalı

import matplotlib.pyplot as plt
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'b', label = 'Eğitim Kaybı')
plt.plot(epochs, val_loss, 'r', label = 'Doğrulama Kaybı')
plt.title('Eğitim ve Doğrulama Kaybı')
plt.xlabel('Epoklar')
plt.ylabel('Kayıp')
plt.legend()
plt.show()

plt.clf()

acc = history.history['acc']
val_acc = history.history['val_acc']
plt.plot(epochs, acc, 'b', label = 'Eğitim Başarımı')
plt.plot(epochs, val_acc, 'r', label = 'Doğrulama Başarımı')
plt.title('Eğitim Başarımı')
plt.xlabel('Epoklar')
plt.ylabel('Başarım')
plt.legend()
plt.show()



