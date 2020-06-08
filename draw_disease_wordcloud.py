#! /usr/bin/env python
# --coding: utf-8 -*-

from wordcloud import WordCloud
import random
import sys


def top_10_color(word):
    #color_hash = {
    #    "TP53": "crimson",
    #    "NRAS": "coral",
    #    "FLT3": "blue",
    #    "TET2": "cornflowerblue",
    #    "U2AF1": "darkgreen",
    #    "RUNX1": "mediumturquoise",
    #    "CDKN2A": "brown",
    #    "ASXL1": "blueviolet",
    #    "WT1": "lightsalmon",
    #    "IDH1": "royalblue",
    #    "BCOR": "seagreen",
    #    "DNMT3A": "mediumorchid",
    #    "ETV6": "violet"
    #}
    #if color_hash.has_key(word):
    #    return color_hash[word]
    #else:
    #    return "black"

    return "black"


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    #print word,font_size
    word_color = top_10_color(word)

    return word_color

    #if font_size >= 30:
    #    return "red"
    #else:
    #    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)



count_dict = {}
all_count = 0
with open("./6000_result_count.txt", "r") as f:
    lines = f.read().rstrip("\n").split("\n")
    for line in lines:
        data = line.split(",")
        disease = data[0]
        count = int(data[1])
        count_dict[disease] = count
        all_count += int(count)


print count_dict

#fpath = "/Library/Fonts/ヒラギノ角ゴ Pro W3.otf"

#wordcloud_y = WordCloud(background_color="white",font_path=fpath,
#    width=800,height=600).generate(y_text)



minfontsize = 10
margin_size = 8

#y_dict["FLT3"] = 5


wordcloud_d = WordCloud(background_color="white",
    mode="RGBA",
    font_path="/Library/Fonts/Arial.ttf",
    #margin=margin_size,
    width=600,
    height=800,
    relative_scaling=0.5,
    #prefer_horizontal=1,
    max_words=50
    #min_font_size=minfontsize,
    #max_font_size=round(300*magni_y,0),
    #color_func=grey_color_func
    ).generate_from_frequencies(count_dict)

wordcloud_d.to_file("./kynurenine_disease.png")


