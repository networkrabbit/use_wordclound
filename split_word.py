# -*- coding: utf-8 -*-
import jieba

stopwords = {}


# 加载停止词
def load_stopwords(filename):
    global stopwords
    for line in open(filename, 'r').readlines():
        line = line.rstrip()
        stopwords.setdefault(line, 0)
        stopwords[line] = 1


# 使用jieba包做中文分词
def split_word(content):
    seg_generator = jieba.cut(content)  # 使用结巴分词，也可以不使用
    # 去除停止词
    seg_list = [i for i in seg_generator if i not in stopwords]
    # 去除空格和换行符
    seg_list = [i for i in seg_list if i != u" " and i != u"\n"]
    return seg_list


# 统计词频
def word_count(word_list):
    word_count_dict = {}
    for i in word_list:
        if i in word_count_dict:
            value = word_count_dict[i] + 1
            word_count_dict[i] = value
        else:
            word_count_dict[i] = 1
    return word_count_dict


# 输入待分词和统计词频的文本路径
def manager_word(file_path):
    file_name = 'resources/stopwords.txt'
    load_stopwords(file_name)
    text = open(file_path, 'r').read()
    word_list = split_word(text)
    count_dict = word_count(word_list)
    # 返回值为词频的字典，键为词，值为该词出现次数
    return count_dict

if __name__ == '__main__':
    manager_word("resources/love2.txt")
