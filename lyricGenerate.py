from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.callbacks import LambdaCallback
import numpy as np
import random
import sys
import pickle


# 加载数据 整理字和id之间的映射
sentences = []
with open('lyrics.txt', 'r', encoding='utf8') as fr:
    lines = fr.readlines()
    for line in lines:
        line = line.strip()
        count = 0
        # 取出英文过多的歌词
        for c in line:    # 统计一周歌中英文字母占得个数
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                count += 1
        if count / len(line) < 0.1:   # 若占比小于0.1则 说明英文少，这首歌就加入到我们的列表中
            sentences.append(line)
print('共%d首歌' % len(sentences))


# 整理汉字和数字的映射
chars = {}
for sentence in sentences:
    for c in sentence:
        chars[c] = chars.get(c, 0) + 1   # 这里是字典的一个基础知识，不懂百度
chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)  # 按词频进行排序
chars = [char[0] for char in chars]
vocab_size = len(chars)    # 总共的汉字数
print('共%d个字' % vocab_size, chars[:20])
 
char2id = {c: i for i, c in enumerate(chars)}
id2char = {i: c for i, c in enumerate(chars)}
 
with open('dictionary.pkl', 'wb') as fw:
    pickle.dump([char2id, id2char], fw)   # 把这两个字典扔进pkl中去



maxlen = 10   # 每隔10取一个词
step = 3   # 取一段序列，然后往后面移动三格，再进行取
vocab_size = len(chars)   # 总共含有的汉字个数
 
X_data = []
Y_data = []
for sentence in sentences:
    for i in range(0, len(sentence) - maxlen, step):
        # 取前10个字
        X_data.append([char2id[c] for c in sentence[i: i + maxlen]])
        # 预测第11个字  预测的词用one_hot编码来表示
        y = np.zeros(vocab_size, dtype=np.bool)
 
        # 这里就是去除第11个词 然后找出对应的id  在id那个位置标记为1,表示这个词的存在
        y[char2id[sentence[i + maxlen]]] = 1   # 用one_hot编码表示一个词的存在
        Y_data.append(y)
 
X_data = np.array(X_data)  # X_data中每条数据的长度都是10
Y_data = np.array(Y_data)  # Y_data中每条数据是一个稀疏向量。几万维，只是在对应位置取1
print(X_data[:2])
print(X_data.shape, Y_data.shape)   # 输出数据的形状




# 模型中所需要的一些参数
embed_size = 128
hidden_size = 128
batch_size = 64
epochs = 20
 
# 定义模型   
# input_dim：大或等于0的整数，字典长度，即输入数据最大下标+1   是embedding层的一些参数  embed_size就是要将最后的一个汉字映射到多少维的向量
# output_dim：大于0的整数，代表全连接嵌入的维度
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embed_size, input_length=maxlen))
model.add(LSTM(hidden_size, input_shape=(maxlen, embed_size)))  # 经过embedding  我们的输入数据变为（max_len, embed_size）
model.add(Dense(vocab_size, activation='softmax'))    # 经过上面的LSTM  我们再连接个Dense  预测的是下一个是所有词的概率。
model.compile(loss='categorical_crossentropy', optimizer='adam')



def sample(preds, diversity=1.0):
    preds = np.asarray(preds).astype('float64')    # 得到当前预测的概率，我们不能单纯认为下一个词是概率最大的那个，要加个多样性    
    preds = np.log(preds + 1e-10) / diversity     # 怎样实现多样性，它就是把概率稍加变动，再加个diversity
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)   # 每一个单词期望的概率 / 总的期望概率   才代表当前词的概率
    probas = np.random.multinomial(1, preds, 1)    # 
    return np.argmax(probas)     # 经过一系列处理后 找出概率大的



# 定义每次训练结束后的回调函数，也就是根据当前训练 试着去生成一段文本
def on_epoch_end(epoch, logs):
    print('-' * 30)
    print('Epoch', epoch)
 
    index = random.randint(0, len(sentences))    # 从我们的句子中随机选取一个字
    for diversity in [0.2, 0.5, 1.0]:    # 给几种不同的多样性权重。。越小可能对概率高的汉字越不利
        print('----- diversity:', diversity)
        sentence = sentences[index][:maxlen]   #  选出某个句子的前十个字  也就是给了起始文本
        print('----- Generating with seed: ' + sentence)  
        sys.stdout.write(sentence)  
 
        for i in range(400):  
            x_pred = np.zeros((1, maxlen))
            for t, char in enumerate(sentence):
                x_pred[0, t] = char2id[char]   # 将我们刚才生成的种子转换为对应的id
 
            preds = model.predict(x_pred, verbose=0)[0]  # 预测概率  这里面还有损失，因为我们只需要概率，所以这里最后加了个[0]
            next_index = sample(preds, diversity)   # 讲概率传进我们的函数中，得到下一个汉字
            next_char = id2char[next_index]   # 将预测的id转为它对应的汉字
 
            sentence = sentence[1:] + next_char  # 构造下一个输入 
 
            sys.stdout.write(next_char)  # 后面逐个词进行写入
            sys.stdout.flush()



# 训练并保存模型
model.fit(X_data, Y_data, batch_size=batch_size, epochs=epochs, callbacks=[LambdaCallback(on_epoch_end=on_epoch_end)])
model.save('song_keras.h5')




from keras.models import load_model
import numpy as np
import pickle
import sys
 
maxlen = 10
model = load_model('song_keras.h5')
 
with open('dictionary.pkl', 'rb') as fr:
    [char2id, id2char] = pickle.load(fr)
 
def sample(preds, diversity=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-10) / diversity
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
 
sentence = '只剩下钢琴被我弹了一天'
sentence = sentence[:maxlen]
 
diversity = 1.0
print('----- Generating with seed: ' + sentence)
print('----- diversity:', diversity)
sys.stdout.write(sentence)
 
for i in range(400):
    x_pred = np.zeros((1, maxlen))
    for t, char in enumerate(sentence):
        x_pred[0, t] = char2id[char]
 
    preds = model.predict(x_pred, verbose=0)[0]
    next_index = sample(preds, diversity)
    next_char = id2char[next_index]
 
    sentence = sentence[1:] + next_char
 
    sys.stdout.write(next_char)
    sys.stdout.flush()