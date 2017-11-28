# coding:utf-8

from scipy.misc import imread
import matplotlib.pyplot as plt
import random
import split_word

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

word_feq = split_word.manager_word("resources/love2.txt")
# 设置背景图片
back_coloring = imread("image/love.jpg")

# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)


# 获取hsl类型的红色
def red_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(3, 87%%, %d%%)" % random.randint(45, 60)


# 添加特定的停止词，因为中文分词已经处理所以不配置
# stopwords = set(STOPWORDS)
# stopwords.add("int")
# stopwords.add("ext")

wc = WordCloud(font_path=u'./font/手写pippi.ttf',
               background_color="white",
               max_words=1000,
               mask=back_coloring,
               # stopwords=stopwords,
               max_font_size=100,
               random_state=42,
               color_func=red_color_func)
# 英文直接使用generate方法录入所有文本，中文则使用分词统计词频
# wc.generate(text)
# 计算好词频后使用generate_from_frequencies函数
wc.generate_from_frequencies(word_feq)
plt.figure()
# 显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()

# 保存图片
wc.to_file(u"love.png")
