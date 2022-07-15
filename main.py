



import pandas as pd
import numpy as np
from jupyter_dash import JupyterDash
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import requests as r
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import dash
from dash.dependencies import Input,Output,State
from dash import Dash,html, dcc
import jupyter_dash
import dash_bootstrap_components as dbc
from wordcloud import WordCloud,ImageColorGenerator
from skimage.io import imread
import plotly.express as px
from skimage.io import imread
import base64
import dash_core_components as dcc
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import arabic_reshaper
import arabic_reshaper
from bidi.algorithm import get_display
import requests as r
from bs4 import BeautifulSoup
import dash_html_components as html
import plotly.graph_objs as go
from PIL import Image
# from dash import dash_table
import matplotlib.pyplot as plt
from dash.dependencies import Input,Output,State
import jupyter_dash
#import dash_bootstrap_components as dbc
from wordcloud import WordCloud,ImageColorGenerator
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
df=pd.read_csv("en.yusufali.csv",index_col=None)
dff = pd.read_csv("Quran-clean-without-aarab.csv",usecols=['SurahNum','AyahNum','Ayah'])
eng_corpus = []
for num in range(1,115):
    full_surah = ""
    for aya in df[df.Surah==num].Text:
        full_surah +=  aya + " "
    eng_corpus.append(full_surah)
eng_corpus=str(eng_corpus)


arabic_corpus = []
for num in range(1,115):
    full_surah = ""
    for aya in dff[dff.SurahNum==num].Ayah:
        full_surah +=  aya + " "
    arabic_corpus.append(full_surah)

arabic_corpus = str(arabic_corpus)




#fetched from https://en.wikipedia.org/wiki/Meccan_surah
mec_surah_list = [96, 68, 73, 74, 1, 111, 81, 87, 92, 89,
                    93, 94, 103, 100, 108, 102, 107, 109, 105, 113,
                    114, 112, 53, 80, 97, 91, 85, 95, 106, 101,
                    75, 104, 77, 50, 90, 86, 54, 38, 7, 72,
                    36, 25, 35, 19, 20, 56, 26, 27, 28, 17,
                    10, 11, 12, 15, 6, 37, 31, 34, 39, 40,
                    41, 42, 43, 44, 45, 46, 51, 88, 18, 16,
                    71, 14, 21, 23, 32, 52, 67, 69, 70, 78,
                    79, 82, 84, 30, 29, 83]

eng_meccan_corp, eng_medinan_corp = "", ""
arabic_meccan_corp, arabic_medinan_corp = "", ""

for i in range(114):
        if i+1 in mec_surah_list:
            eng_meccan_corp += eng_corpus[i]
            arabic_meccan_corp += arabic_corpus[i]
        else:
            eng_medinan_corp += eng_corpus[i]
            arabic_medinan_corp += arabic_corpus[i]
# ### to obtain redundant words based on their frequency from the quran itself in ENGLISH

def get_uns(corpus):
    uniques = {}
    for s in corpus:
        for w in s.split(' '):
            if w not in uniques.keys():
                uniques[w] = 1
            else:
                uniques[w] += 1
    uniques = {k: v for k, v in sorted(uniques.items(), key=lambda item: item[1], reverse=True)}
    return uniques

get_uns(eng_corpus)
get_uns(arabic_corpus)

#### all the surahs names fetched from iternet

surah_name = """1. Al-Fatihah (the Opening)
2. Al-Baqarah (the Cow)
3. Aali Imran (the Family of Imran)
4. An-Nisa’ (the Women)
5. Al-Ma’idah (the Table)
6. Al-An’am (the Cattle)
7. Al-A’raf (the Heights)
8. Al-Anfal (the Spoils of War)
9. At-Taubah (the Repentance)
10. Yunus (Yunus)
11. Hud (Hud)
12. Yusuf (Yusuf)
13. Ar-Ra’d (the Thunder)
14. Ibrahim (Ibrahim)
15. Al-Hijr (the Rocky Tract)
16. An-Nahl (the Bees)
17. Al-Isra’ (the Night Journey)
18. Al-Kahf (the Cave)
19. Maryam (Maryam)
20. Ta-Ha (Ta-Ha)
21. Al-Anbiya’ (the Prophets)
22. Al-Haj (the Pilgrimage)
23. Al-Mu’minun (the Believers)
24. An-Nur (the Light)
25. Al-Furqan (the Criterion)
26. Ash-Shu’ara’ (the Poets)
27. An-Naml (the Ants)
28. Al-Qasas (the Stories)
29. Al-Ankabut (the Spider)
30. Ar-Rum (the Romans)
31. Luqman (Luqman)
32. As-Sajdah (the Prostration)
33. Al-Ahzab (the Combined Forces)
34. Saba’ (the Sabeans)
35. Al-Fatir (the Originator)
36. Ya-Sin (Ya-Sin)
37. As-Saffah (Those Ranges in Ranks)
38. Sad (Sad)
39. Az-Zumar (the Groups)
40. Ghafar (the Forgiver)
41. Fusilat (Distinguished)
42. Ash-Shura (the Consultation)
43. Az-Zukhruf (the Gold)
44. Ad-Dukhan (the Smoke)
45. Al-Jathiyah (the Kneeling)
46. Al-Ahqaf (the Valley)
47. Muhammad (Muhammad)
48. Al-Fat’h (the Victory)
49. Al-Hujurat (the Dwellings)
50. Qaf (Qaf)
51. Adz-Dzariyah (the Scatterers)
52. At-Tur (the Mount)
53. An-Najm (the Star)
54. Al-Qamar (the Moon)
55. Ar-Rahman (the Most Gracious)
56. Al-Waqi’ah (the Event)
57. Al-Hadid (the Iron)
58. Al-Mujadilah (the Reasoning)
59. Al-Hashr (the Gathering)
60. Al-Mumtahanah (the Tested)
61. As-Saf (the Row)
62. Al-Jum’ah (Friday)
63. Al-Munafiqun (the Hypocrites)
64. At-Taghabun (the Loss & Gain)
65. At-Talaq (the Divorce)
66. At-Tahrim (the Prohibition)
67. Al-Mulk – (the Kingdom)
68. Al-Qalam (the Pen)
69. Al-Haqqah (the Inevitable)
70. Al-Ma’arij (the Elevated Passages)
71. Nuh (Nuh)
72. Al-Jinn (the Jinn)
73. Al-Muzammil (the Wrapped)
74. Al-Mudaththir (the Cloaked)
75. Al-Qiyamah (the Resurrection)
76. Al-Insan (the Human)
77. Al-Mursalat (Those Sent Forth)
78. An-Naba’ (the Great News)
79. An-Nazi’at (Those Who Pull Out)
80. ‘Abasa (He Frowned)
81. At-Takwir (the Overthrowing)
82. Al-Infitar (the Cleaving)
83. Al-Mutaffifin (Those Who Deal in Fraud)
84. Al-Inshiqaq (the Splitting Asunder)
85. Al-Buruj (the Stars)
86. At-Tariq (the Nightcomer)
87. Al-A’la (the Most High)
88. Al-Ghashiyah (the Overwhelming)
89. Al-Fajr (the Dawn)
90. Al-Balad (the City)
91. Ash-Shams (the Sun)
92. Al-Layl (the Night)
93. Adh-Dhuha (the Forenoon)
94. Al-Inshirah (the Opening Forth)
95. At-Tin (the Fig)
96. Al-‘Alaq (the Clot)
97. Al-Qadar (the Night of Decree)
98. Al-Bayinah (the Proof)
99. Az-Zalzalah (the Earthquake)
100. Al-‘Adiyah (the Runners)
101. Al-Qari’ah (the Striking Hour)
102. At-Takathur (the Piling Up)
103. Al-‘Asr (the Time)
104. Al-Humazah (the Slanderer)
105. Al-Fil (the Elephant)
106. Quraish (Quraish)
107. Al-Ma’un (the Assistance)
108. Al-Kauthar (the River of Abundance)
109. Al-Kafirun (the Disbelievers)
110. An-Nasr (the Help)
111. Al-Masad (the Palm Fiber)
112. Al-Ikhlas (the Sincerity)
113. Al-Falaq (the Daybreak)
114. An-Nas (Mankind)"""

surah_name = list(map(lambda x: x.split(' ')[1], (surah_name.split('\n'))))

#Scrab surahs names in arabic from Internet

site =  r.get('https://gpsarab.com/shop11/en/content/11-list-of-surahs-in-the-holy-quran').content
soup = BeautifulSoup(site, "html.parser")
surah_name_arabic = [s.text for s in soup.findAll('td')]
surah_name_arabic = [surah_name_arabic[x] for x in range(1, len(surah_name_arabic),5)]
### to get redundant words(pronouns etc) so we can omit them later on
SW = list(STOPWORDS) + ['ye', 'verily', 'will', 'said', 'say', 'us', 'thy', 'thee', 'thou',
                        'the', 'and', 'of', 'to', 'is', 'in', 'they', 'a', 'that', 'for',
                        'ye', 'who', 'their', 'not', 'them', 'He', 'be',
                        'We', 'those', 'with', 'have', 'are', 'And', 'from', 'it', 'but',
                        'on', 'you', 'your', 'all', 'as', 'he', 'shall', 'if', 'thou', 'no',
                        'which', 'But', 'do', 'his', 'what', 'I', 'or', 'when', 'we', 'by',
                        'His', 'said:', 'thy', 'has', 'this', 'They', 'there',
                        'then', 'one', 'my', 'him', 'were', 'was', 'thee', 'them,', 'may', 'any',
                        'had', 'sent', 'before', 'nor', 'among', 'whom', 'Day', 'hath', 'made',
                        'did', '(of', 'Who', 'would', '(in', 'out', 'Say:', 'our', 'indeed',
                        'so', 'If', '(to', '(the', 'against', 'been', 'an', 'For', 'you,',
                        'us', 'The', 'Then', 'fear', 'than', 'give', '-', 'should', 'such', 'Most',
                        'down', 'men', 'So', 'say:', '"O', 'Our', 'It', 'come', 'can', 'after', 'O',
                        'me', 'some', 'turn', '', 'over', 'up', 'things', 'make', 'know',
                        'reject', 'When', 'unto', 'into', 'its', 'see', 'Those', 'only',
                        'them:','good', 'own', 'doth', 'of)', 'most', 'other',
                        'except', '(for', 'Thou', 'at', '(and', 'between', 'take', 'away',
                        'given', 'every', 'back', 'say,', 'verily', 'never', 'That', 'said'
                       'whose', 'where', 'which', 'how', 'when']

s = ['من', 'في', 'ما',
       'إن', 'لا', 'على', 'إلا', 'ولا', 'وما', 'أن', 'قال', 'إلى', 'لهم', 'يا', 'ومن', 'ثم', 'لكم', 'به', 'كان', 'بما'
       , 'قل', 'ذلك', 'أو', 'له', 'الذي', 'هو',  'هم', 'وإن', 'قالوا', 'كل', 'فيها', 'كانوا', 'عن', 'الذين','إذا',  'عليهم',
       'شيء', 'هذا', 'كنتم',  'لم', 'وهو', 'فإن', 'إذ',  'عليكم',  'إنا', 'فلا', 'منهم',  'أيها', 'إنه','بعد', 'عليه',
       'حتى', 'وهم', 'وإذا', 'بسم الله' 'أولئك', 'أم', 'إني', 'ولقد', 'فيه', 'بل', 'قد', 'عند', 'إنما', 'ولكن', 'ولو',
       'مما',  'منكم', 'فلما', 'ألا', 'لمن',  'دون', 'فمن', 'منه', 'فإذا', 'فما', 'منها', 'كذلك', 'وقال', 'وكان']
ASW1 = [get_display(arabic_reshaper.reshape(x)) for x in s]

surah_name=pd.DataFrame(surah_name)


####  This is the main function which will be used to generate various kinds of wordclouds

def generateWordCloud(corpus=None, title=None, isArabic=False):
    plt.figure(figsize=(15, 8))

    if not isArabic:
        my_wordcloud = WordCloud(min_font_size=50, stopwords=SW, max_words=100, collocations=False, width=4000,
                                 height=2000, background_color='white', contour_width=0.0000001)

        my_wordcloud.generate(corpus)
        fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2', title="<b>The Most Frequent Words In Quran</b>")
        fig_wordcloud.update_layout(title_x=0.5, title_font_color="#4B9071")
        fig_wordcloud.update_xaxes(visible=False)
        fig_wordcloud.update_yaxes(visible=False)

    if isArabic:
        word_cloud = WordCloud(font_path='arial', width=4000, height=2000, min_font_size=50, collocations=False,
                               stopwords=ASW1, max_words=100, background_color='white')
        fig_wordcloud = word_cloud.generate_from_text(get_display(arabic_reshaper.reshape(corpus)))
        fig_wordcloud = px.imshow(word_cloud, template='ggplot2')
        fig_wordcloud.update_xaxes(visible=False)
        fig_wordcloud.update_yaxes(visible=False)
        fig_wordcloud.update_layout(title_text="<b>الكلمات الأكثر انتشارًا في القرءان</b>", title_x=0.5,
                                    title_font_color="#4B9071")

    return fig_wordcloud

Arab_words=arabic_meccan_corp.split()

NAMES = {'آدم': 12, 'إبليس': 11, 'فرعون': 66, 'موسى': 139, 'عيسى': 32, 'جبريل': 3, 'سليمان': 16, 'هاروت': 1, 'وماروت': 1, 'إبراهيم': 64, 'رب': 500, 'إسماعيل': 9, 'يعقوب': 16, 'إسحاق': 17, 'حنيفا': 2, 'الأسباط': 4, 'الرحمن': 64,'الله': 2261, 'طالوت': 2, 'هارون': 19, 'جالوت': 3, 'داوود': 18, 'عمران': 3, 'مريم': 34, 'زكريا': 7, 'المسيح': 10, 'محمد': 4, 'نوح': 39, 'يونس': 4, 'اليسع': 2, 'صالح': 8, 'شعيب': 10, 'عزير': 1, 'عاد': 21, 'ثمود': 25, 'يونس': 4, 'هود': 7, 'لوط': 17, 'يوسف': 26, 'البشير': 1, 'إسماعيل': 3, 'يحيى': 4, 'إدريس': 2, 'إسرائيل': 43, 'السامري': 3, 'الهدهد': 1, 'كريم': 1, 'هامان': 5, 'قارون': 2, 'لقمان': 2, 'الملائكة': 68, 'ياسين': 1, 'أيوب': 4, 'مالك': 1, 'مأجوج': 2, 'يأجوج': 2, 'يهود': 9, 'نصارى': 16, 'أحمد': 1, 'إلياس': 2, 'أبي لهب': 1}
LOC = { 'الواد': 4, 'البيت': 1, 'نهر': 5, 'المدينة': 14, 'مصر': 4, 'جنات': 67, 'الكهف': 4, 'البحرين': 4, 'جهنم': 35, 'مدين': 9, 'سيناء': 1, 'النار': 10, 'القرى': 4, 'يثرب': 1, 'الجنة': 50, 'مكة': 1, 'ببابل': 1, 'بكة': 1, 'عدن': 11, 'المغرب': 7, 'الأقصى': 1, 'مسجد': 21, 'مكة': 1}
LOC_map = { 'الواد المقدس': 2, 'مصر': 4, 'مدين': 9, 'سيناء': 1, 'يثرب': 1, 'مكة': 1, 'بابل': 1, 'بكة': 1, 'المسجد الأقصى': 1, 'مكة': 1}

data = {'City':['الواد المقدس', 'مصر', 'مدين', 'سيناء', 'يثرب', 'مكة', 'بابل', 'المسجد الأقصى'],'frequency':[2, 4, 9, 1, 1, 2, 1, 1],'iso_alpha':['EGY','EGY','JOR','EGY','SAU','SAU','IRQ','PSE']}

df_LOC_map = pd.DataFrame(data)
import plotly.express as px
fig1 = px.scatter_geo(df_LOC_map,   # locations="iso_alpha",
                     color="City", # which column to use to set the color of markers
                     hover_name="City", # column added to hover information
                     size="frequency", # size of markers
                     projection="natural earth",
                   lat=[28.239069,27.488781,29.878755,28.883160,24.706915,21.186973,32.569963,31.872893],
                    lon=[33.656254,29.824681,38.181730,33.871252,39.437466,41.592705,44.544741,35.025873])

fig1.update_layout(
        title = 'Cities in Quran' )
# fig1.update_layout( margin={"r":0,"t":0,"l":0,"b":0})
fig1.update_layout(title_text="<b>Cities Mentioned In The Quran</b>", title_x=0.5,title_font_color="#4B9071",height=500 , width = 1090)

#fig1.show();

# ترتيب السور على حسب النزول
arrangement = ['العلق','القلم','المزمل','المدثر','الفاتحة',' المسد','التكوير','الأعلى','الليل','الفجر','الضحى','الشرح','العصر','العاديات','الكوثر','التكاثر','الماعون','الكافرون','الفيل','الفلق','الناس','الإخلاص','النجم','عبس','القدر','الشمس','البروج','التين','قريش','القارعة','القيامة','الهمزة','المرسلات','ق','البلد','الطارق','القمر','ص','الأعراف','الجن','يس','الفرقان','فاطر','مريم','طه','الواقعة','الشعراء','النمل','القصص','الإسراء','يونس','هود','يوسف','الحجر','الأنعام','الصافات','لقمان','سبأ','الزمر','غافر','فصلت','الشورى','الزخرف','الدخان','الجاثية','الأحقاف','الذاريات','الغاشية','الكهف','النحل','نوح','إبراهيم','الأنبياء','المؤمنون','السجدة','الطور','الملك','الحاقة','المعارج','النبأ','النازعات','الانفطار','الانشقاق','الروم','العنكبوت','المطففين','البقرة','الأنفال','آل عمران','الأحزاب','الممتحنة','النساء','الزلزلة','الحديد','محمد','الرعد','الرحمن','الإنسان','الطلاق','البينة','الحشر','النور','الحج','المنافقون','المجادلة','الحجرات','التحريم','التغابن','الصف','الجمعة','الفتح','المائدة','التوبة','النصر']


chapter = [30,29,29,29,1,30,30,30,30,30,
           30,30,30,30,30,30,30,30,30,30,
           30,30,27,30,30,30,30,30,30,30,
           29,30,29,26,30,30,27,23,8,29,
           22,18,22,16,16,27,19,19,20,15,
           11,11,12,14,7,23,21,22,23,24,
           24,25,25,25,25,26,26,30,15,14,
           29,13,17,18,21,27,29,29,29,30,
           30,30,30,21,20,30,
           1,9,3,21,28,4,30,27,26,13,
           27,29,28,30,28,18,17,28,28,26,
           28,28,28,28,26,6,10,30]

num_Ayah = [19,52,20,56,7,5,29,19,21,30,
            11,8,3,11,3,8,7,6,5,5,
            6,4,62,42,5,15,22,8,4,11,
            40,9,50,45,20,17,55,88,206,28,
            83,77,45,98,135,96,227,93,88,111,
            109,123,111,99,165,182,34,54,75,85,
            54,53,89,59,37,35,60,26,110,128,
            28,52,112,118,30,49,30,52,44,40,
            46,19,25,60,69,36,
            286,75,200,73,13,176,8,29,38,43,
            78,31,12,8,24,64,78,11,22,18,
            12,18,14,11,29,120,129,3]

num_pages = [0.5,2,2,2,1,0.5,1,1,1,1,
             0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
             0.5,0.5,2,1,0.5,0.5,1,0.5,0.5,0.5,
             1,0.5,2,2,1,0.5,3,5,26,2,
             6,8,6,7,10,3,10,8,11,11,
             13,14,14,5,23,7,4,6,9,10,
             6,6,7,3,3,5,3,1,12,15,
             2,7,10,8,3,3,2,2,2,2,
             2,1,1,7,8,2,
             48,10,27,10,2,29,0.5,5,4,6,
             3,2,2,0.5,4,9,10,2,3,3,
             2,2,2,2,4,22,21,0.5]
index = list(range(114))
import pandas as pd

zipped = list(zip(index, arrangement, chapter, num_Ayah, num_pages))
df = pd.DataFrame(zipped, columns=['index','Surah', 'chapter', 'num_Ayah', 'num_pages'])


# Sentiment Analysis

positive_sent = [4, 65, 50, 31, 19, 28, 23, 11, 23, 20, 21, 18, 7, 14, 17, 25, 25, 17, 30, 36, 23, 28, 19, 15, 21, 50, 19, 18, 14, 17, 14, 5, 23, 10, 16, 15, 44, 26, 15, 22, 13, 19, 17, 18, 11, 9, 12, 14, 3, 8, 15, 9, 25, 9, 18, 17, 11, 3, 6, 4, 6, 3, 1, 11, 5, 4, 11, 10, 9, 10, 7, 5, 5, 9, 13, 13, 7, 12, 13, 17, 8, 7, 7, 7, 8, 4, 6, 5, 13, 2, 7, 10, 7, 3, 4, 6, 3, 4, 3, 3, 2, 4, 2, 1, 1, 3, 0, 0, 0, 2, 2, 3, 0, 2]

negative_sent = [1, 39, 27, 25, 14, 27, 47, 18, 37, 10, 19, 28, 6, 13, 35, 19, 20, 30, 20, 32, 31, 17, 43, 13, 23, 103, 26, 16, 13, 13, 2, 7, 10, 12, 5, 30, 94, 36, 11, 16, 10, 6, 29, 26, 5, 5, 11, 4, 1, 26, 25, 25, 21, 31, 49, 56, 2, 4, 5, 2, 2, 3, 2, 1, 1, 0, 10, 29, 32, 24, 12, 6, 7, 34, 19, 8, 36, 19, 26, 21, 18, 10, 24, 12, 8, 12, 7, 16, 14, 15, 4, 7, 2, 4, 4, 11, 0, 0, 4, 7, 8, 4, 1, 8, 3, 1, 7, 2, 5, 0, 3, 0, 5, 4]


# surah_name_arabic
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
site =  r.get('https://gpsarab.com/shop11/en/content/11-list-of-surahs-in-the-holy-quran').content
soup = BeautifulSoup(site, "html.parser")
surah_name_arabic = [s.text for s in soup.findAll('td')]
surah_name_arabic = [surah_name_arabic[x] for x in range(1, len(surah_name_arabic),5)]

zipped = list(zip(index, surah_name_arabic, positive_sent, negative_sent))
df_sent = pd.DataFrame(zipped, columns=['index','Surah', 'positive_sent', 'negative_sent'])

import plotly.graph_objects as go



fig = go.Figure()

fig.add_trace(go.Bar(x=df_sent['Surah'], y=df_sent['positive_sent'],
                base=0,
                marker_color='lightslategrey',
                name='Positive'))

fig.add_trace(go.Bar(x=df_sent['Surah'], y=(-1)* (df_sent['negative_sent']),
#                 base=(-1)*(df_sent['negative_sent']),
                base=0,
                marker_color='crimson',
                name='Negative'))





fig.update_layout(height = 500, width =1090)

fig.update_layout(title_text="<b>Sentiment Analysis for The Holy Quran</b>", title_x=0.5,title_font_color="#4B9071",)

#fig.show()

POS = {'part_voc': 511, 'pron': 1346, 'verb': 18846, 'pron_dem': 1041, 'part_interrog': 93, 'conj_sub': 1836, 'part': 696, 'adj': 2636, 'prep': 10397, 'conj': 1879, 'noun': 23128, 'part_verb': 409, 'adv': 550, 'adv_rel': 71, 'part_det': 8, 'part_focus': 65, 'pron_rel': 3604, 'adv_interrog': 36, 'part_neg': 2056, 'part_fut': 38, 'interj': 30, 'abbrev': 987, 'noun_quant': 40, 'pron_interrog': 45, 'verb_pseudo': 777, 'noun_prop': 7120}

import plotly.express as px
import pandas as pd

zipped = list(zip(POS.keys(),POS.values()))
pos_df = pd.DataFrame(zipped, columns=['POS','count'])
# pos_df

fig3 = px.bar(data_frame = pos_df, x = pos_df['POS'] , y = pos_df['count'])
fig3.update_layout(title_text="<b>Part Of Speech Tagging</b>", title_x=0.5,title_font_color="#4B9071")
#fig3.show();

NAMES = {'آدم': 12, 'إبليس': 11, 'فرعون': 66, 'موسى': 139, 'عيسى': 32, 'جبريل': 3, 'سليمان': 16, 'هاروت': 1, 'وماروت': 1, 'إبراهيم': 64, 'رب': 500, 'إسماعيل': 9, 'يعقوب': 16, 'إسحاق': 17, 'حنيفا': 2, 'الأسباط': 4, 'الرحمن': 64,'الله': 2261, 'طالوت': 2, 'هارون': 19, 'جالوت': 3, 'داوود': 18, 'عمران': 3, 'مريم': 34, 'زكريا': 7, 'المسيح': 10, 'محمد': 4, 'نوح': 39, 'يونس': 4, 'اليسع': 2, 'صالح': 8, 'شعيب': 10, 'عزير': 1, 'عاد': 21, 'ثمود': 25, 'يونس': 4, 'هود': 7, 'لوط': 17, 'يوسف': 26, 'البشير': 1, 'إسماعيل': 3, 'يحيى': 4, 'إدريس': 2, 'إسرائيل': 43, 'السامري': 3, 'الهدهد': 1, 'كريم': 1, 'هامان': 5, 'قارون': 2, 'لقمان': 2, 'الملائكة': 68, 'ياسين': 1, 'أيوب': 4, 'مالك': 1, 'مأجوج': 2, 'يأجوج': 2, 'يهود': 9, 'نصارى': 16, 'أحمد': 1, 'إلياس': 2, 'أبي لهب': 1}
NAMES_list = []
for key in NAMES:
    for idx in range(NAMES[key]):
        NAMES_list.append(key)
# NAMES_list
NAMES_text = ' '.join(NAMES_list)
# NAMES_text

LOC = { 'الواد': 4, 'البيت': 1, 'نهر': 5, 'المدينة': 14, 'مصر': 4, 'جنات': 67, 'الكهف': 4, 'مجمع_البحرين': 4, 'جهنم': 35, 'مدين': 9, 'سيناء': 1, 'النار': 10, 'القرى': 4, 'يثرب': 1, 'الجنة': 50, 'مكة': 1, 'ببابل': 1, 'بكة': 1, 'عدن': 11, 'المغرب': 7, 'الأقصى': 1, 'مسجد': 21, 'مكة': 1}

LOC_list = []
for key in LOC:
    for idx in range(LOC[key]):
        LOC_list.append(key)
# LOC_list
LOC_text = ' '.join(LOC_list)
# LOC_text

LOC_map = { 'الواد المقدس': 2, 'مصر': 4, 'مدين': 9, 'سيناء': 1, 'يثرب': 1, 'مكة': 1, 'بابل': 1, 'بكة': 1, 'المسجد الأقصى': 1, 'مكة': 1}

# Sentiment Analysis

positive_sent = [4, 65, 50, 31, 19, 28, 23, 11, 23, 20, 21, 18, 7, 14, 17, 25, 25, 17, 30, 36, 23, 28, 19, 15, 21, 50, 19, 18, 14, 17, 14, 5, 23, 10, 16, 15, 44, 26, 15, 22, 13, 19, 17, 18, 11, 9, 12, 14, 3, 8, 15, 9, 25, 9, 18, 17, 11, 3, 6, 4, 6, 3, 1, 11, 5, 4, 11, 10, 9, 10, 7, 5, 5, 9, 13, 13, 7, 12, 13, 17, 8, 7, 7, 7, 8, 4, 6, 5, 13, 2, 7, 10, 7, 3, 4, 6, 3, 4, 3, 3, 2, 4, 2, 1, 1, 3, 0, 0, 0, 2, 2, 3, 0, 2]

negative_sent = [1, 39, 27, 25, 14, 27, 47, 18, 37, 10, 19, 28, 6, 13, 35, 19, 20, 30, 20, 32, 31, 17, 43, 13, 23, 103, 26, 16, 13, 13, 2, 7, 10, 12, 5, 30, 94, 36, 11, 16, 10, 6, 29, 26, 5, 5, 11, 4, 1, 26, 25, 25, 21, 31, 49, 56, 2, 4, 5, 2, 2, 3, 2, 1, 1, 0, 10, 29, 32, 24, 12, 6, 7, 34, 19, 8, 36, 19, 26, 21, 18, 10, 24, 12, 8, 12, 7, 16, 14, 15, 4, 7, 2, 4, 4, 11, 0, 0, 4, 7, 8, 4, 1, 8, 3, 1, 7, 2, 5, 0, 3, 0, 5, 4]


# surah_name_arabic
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
site =  r.get('https://gpsarab.com/shop11/en/content/11-list-of-surahs-in-the-holy-quran').content
soup = BeautifulSoup(site, "html.parser")
surah_name_arabic = [s.text for s in soup.findAll('td')]
surah_name_arabic = [surah_name_arabic[x] for x in range(1, len(surah_name_arabic),5)]

zipped = list(zip(index, surah_name_arabic, positive_sent, negative_sent))
df_sent = pd.DataFrame(zipped, columns=['index','Surah', 'positive_sent', 'negative_sent'])

NAMES = {'آدم': 12, 'إبليس': 11, 'فرعون': 66, 'موسى': 139, 'عيسى': 32, 'جبريل': 3, 'سليمان': 16, 'هاروت': 1, 'وماروت': 1, 'إبراهيم': 64, 'رب': 500, 'إسماعيل': 9, 'يعقوب': 16, 'إسحاق': 17, 'حنيفا': 2, 'الأسباط': 4, 'الرحمن': 64,'الله': 2261, 'طالوت': 2, 'هارون': 19, 'جالوت': 3, 'داوود': 18, 'عمران': 3, 'مريم': 34, 'زكريا': 7, 'المسيح': 10, 'محمد': 4, 'نوح': 39, 'يونس': 4, 'اليسع': 2, 'صالح': 8, 'شعيب': 10, 'عزير': 1, 'عاد': 21, 'ثمود': 25, 'يونس': 4, 'هود': 7, 'لوط': 17, 'يوسف': 26, 'البشير': 1, 'إسماعيل': 3, 'يحيى': 4, 'إدريس': 2, 'إسرائيل': 43, 'السامري': 3, 'الهدهد': 1, 'كريم': 1, 'هامان': 5, 'قارون': 2, 'لقمان': 2, 'الملائكة': 68, 'ياسين': 1, 'أيوب': 4, 'مالك': 1, 'مأجوج': 2, 'يأجوج': 2, 'يهود': 9, 'نصارى': 16, 'أحمد': 1, 'إلياس': 2, 'أبي لهب': 1}
NAMES_list = []
for key in NAMES:
    for idx in range(NAMES[key]):
        NAMES_list.append(key)
# NAMES_list
NAMES_text = ' '.join(NAMES_list)
#NAMES_text

word_cloud = WordCloud(font_path='arial',width=2050,height=1000, stopwords=ASW1,max_words=160,background_color='white',collocations = False)
fig_wordcloud1  = word_cloud.generate_from_text(get_display(arabic_reshaper.reshape(NAMES_text)))
fig_wordcloud1 = px.imshow(word_cloud, template='ggplot2')
fig_wordcloud1.update_xaxes(visible=False)
fig_wordcloud1.update_yaxes(visible=False)
fig_wordcloud1.update_layout(title_text="Names", title_x=0.5,title_font_color="#4B9071",font_size=15)

#fig_wordcloud1.show();


word_cloud1 = WordCloud(font_path='arial',width=2050,height=1000, stopwords=ASW1,max_words=160,background_color='white',collocations = False)
wordcloud1  = word_cloud.generate_from_text(get_display(arabic_reshaper.reshape(LOC_text)))
wordcloud1 = px.imshow(word_cloud, template='ggplot2')
wordcloud1.update_xaxes(visible=False)
wordcloud1.update_yaxes(visible=False)
wordcloud1.update_layout( title_x=0.5,title_text="places",title_font_color="#4B9071",font_size=15)
#wordcloud1.show();
LOC = { 'الواد': 4, 'البيت': 1, 'نهر': 5, 'المدينة': 14, 'مصر': 4, 'جنات': 67, 'الكهف': 4, 'البحرين': 4, 'جهنم': 35, 'مدين': 9, 'سيناء': 1, 'النار': 10, 'القرى': 4, 'يثرب': 1, 'الجنة': 50, 'مكة': 1, 'ببابل': 1, 'بكة': 1, 'عدن': 11, 'المغرب': 7, 'الأقصى': 1, 'مسجد': 21, 'مكة': 1}

LOC_list = []
for key in LOC:
    for idx in range(LOC[key]):
        LOC_list.append(key)
# LOC_list
LOC_text = ' '.join(LOC_list)



arrangement = ['العلق','القلم','المزمل','المدثر','الفاتحة',' المسد','التكوير','الأعلى','الليل','الفجر','الضحى','الشرح','العصر','العاديات','الكوثر','التكاثر','الماعون','الكافرون','الفيل','الفلق','الناس','الإخلاص','النجم','عبس','القدر','الشمس','البروج','التين','قريش','القارعة','القيامة','الهمزة','المرسلات','ق','البلد','الطارق','القمر','ص','الأعراف','الجن','يس','الفرقان','فاطر','مريم','طه','الواقعة','الشعراء','النمل','القصص','الإسراء','يونس','هود','يوسف','الحجر','الأنعام','الصافات','لقمان','سبأ','الزمر','غافر','فصلت','الشورى','الزخرف','الدخان','الجاثية','الأحقاف','الذاريات','الغاشية','الكهف','النحل','نوح','إبراهيم','الأنبياء','المؤمنون','السجدة','الطور','الملك','الحاقة','المعارج','النبأ','النازعات','الانفطار','الانشقاق','الروم','العنكبوت','المطففين','البقرة','الأنفال','آل عمران','الأحزاب','الممتحنة','النساء','الزلزلة','الحديد','محمد','الرعد','الرحمن','الإنسان','الطلاق','البينة','الحشر','النور','الحج','المنافقون','المجادلة','الحجرات','التحريم','التغابن','الصف','الجمعة','الفتح','المائدة','التوبة','النصر']
chapter = [30,29,29,29,1,30,30,30,30,30,
           30,30,30,30,30,30,30,30,30,30,
           30,30,27,30,30,30,30,30,30,30,
           29,30,29,26,30,30,27,23,8,29,
           22,18,22,16,16,27,19,19,20,15,
           11,11,12,14,7,23,21,22,23,24,
           24,25,25,25,25,26,26,30,15,14,
           29,13,17,18,21,27,29,29,29,30,
           30,30,30,21,20,30,
           1,9,3,21,28,4,30,27,26,13,
           27,29,28,30,28,18,17,28,28,26,
           28,28,28,28,26,6,10,30]

num_of_ayahs = [19,52,20,56,7,5,29,19,21,30,
            11,8,3,11,3,8,7,6,5,5,
            6,4,62,42,5,15,22,8,4,11,
            40,9,50,45,20,17,55,88,206,28,
            83,77,45,98,135,96,227,93,88,111,
            109,123,111,99,165,182,34,54,75,85,
            54,53,89,59,37,35,60,26,110,128,
            28,52,112,118,30,49,30,52,44,40,
            46,19,25,60,69,36,
            286,75,200,73,13,176,8,29,38,43,
            78,31,12,8,24,64,78,11,22,18,
            12,18,14,11,29,120,129,3]


index = list(range(114))
# import pandas as pd

zipped = list(zip(index, arrangement, chapter, num_of_ayahs ))
df = pd.DataFrame(zipped, columns=['index','Surah', 'chapter', 'num_of_ayahs'])






marks={ index: {"label": str(index), "style": {"writing-mode": "vertical-rl"}}
                for index in index }

app = dash.Dash(__name__)
server=app.server #to make heroku recognize
#and connect the server

app.layout = html.Div(

    [

        #         html.Div([html.Img(src=app.get_asset_url('logo.png'),style={'height':'100px',
        #                      'width':'20%','align':'left',"margin-left":"500px","float":"left"})]),
        html.A(
            dbc.Row(
                [

                    dbc.Col(html.Img(src=app.get_asset_url('lgo.png'), style={'height': '98px',
                                                                              'width': '95px', 'align': 'left',
                                                                              "margin-left": "590px",
                                                                              "float": "left"})),

                    dbc.Col(html.H1(children='The Holy Quran',
                                    style={
                                        'text-align': 'center',
                                        'color': '##EDEFEB',
                                        "margin-left": "-18px"
                                    }
                                    )),
                    dbc.Col(html.H6(
                        style={
                            'text-align': 'right',
                            'color': 'white'
                        })),
                ],
                style={
                    'height': 'auto',
                    'width': 'auto',
                    'text-align': 'left',
                    'background-color': '#4b9072a7',
                    'align-items': 'center'
                }
            ),
        ),

        html.Div(
            [
                html.H1(children="Getting Insights From Quran Using NLP"),
                html.Label(
                    "We Are Interested In Investigating The Holy Qur'an To Come Up With Some Insights Such As Qur'an Contains of 6666 Ayahs,There is 85 Makki Surah and 25 Madani Surah,We Also Came Up With the places, People Mentioned In Qur'an Using Camel Tool.",
                    style={"color": "rgb(33 36 35)"},
                ),


            ],
            className="side_bar",
        ),

        html.Div(
            [
                html.Div(
                    [

                        html.Div(
                            [
                                html.Div(
                                    [dcc.Dropdown(
                                        id='dropdown',
                                        options=[
                                            {'label': 'Whole Quran', 'value': 'eng_corpus'},
                                            {'label': 'Makki', 'value': 'eng_meccan_corp'},
                                            {'label': 'Madani', 'value': 'eng_medinan_corp'}, ],

                                        placeholder='Choose .....', multi=False,
                                        className='form-dropdown',
                                        style={'width': "100%", "color": "secondary"},
                                        persistence='string',
                                        persistence_type='memory'
                                    ),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Col(
                                                    [
                                                        dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph',
                                                                 children=[
                                                                     dcc.Tab(label='En', value='tab-1-example-graph'),
                                                                     dcc.Tab(label='Ar', value='tab-2-example-graph'),
                                                                 ], style={"padding-bottom": "0px",
                                                                           "margin-bottom": "15px"}, ),
                                                        dcc.Graph(id='wordcloud'),
                                                    ],

                                                ),

                                            ], style={})], width={'size': 12, "offset": 0, 'order': 1},
                                            style={'padding-left': "25px", 'padding-right': "25px",
                                                   "padding-bottom": "15px"}),

                                        html.Div([
                                            dcc.Graph(id='environ-graph', figure=fig),
                                        ], style={'padding-left': "25px", 'padding-right': "10px",
                                                  "padding-bottom": "15px"}),

                                        html.Div([
                                            dcc.Graph(id='graph2', figure=fig1),

                                        ], style={"padding-bottom": "15px", "width": "100%", 'padding-left': "25px",
                                                  'padding-right': "25px"}),

                                    ],
                                    style={"width": "1095"

                                           },
                                ),
                                html.Div(
                                    [
                                        #

                                        html.Div(
                                            [

                                            ]
                                        ),
                                    ],
                                    style={"width": "100%"},
                                ),
                            ],
                            className="row",
                        ),

                        html.Div([
                            dcc.Graph(id='environ-graph1', figure=fig3),
                        ], style={"width": "1150", 'padding-left': "25px", 'padding-right': "25px"
                            , "height": " 500px",
                                  "padding-bottom": "10px"

                                  }, ),

                        html.Div([
                            html.H2(children="Named entity recognition (NER)",
                                    style={"text-align": "center", "font-size": "100%", "color": "#4B9071",
                                           "font-weight": "bold", "padding-bottom": "50px",
                                           "padding-bottom": "50px",
                                           "margin-top": "-10px", "margin-bottom": "-10px"})
                        ]),

                        html.Div([

                            html.Div([

                                dcc.Graph(figure=wordcloud1)],
                                style={'width': '47%', 'display': 'inline-block', "padding-bottom": "15px",
                                       'padding-left': "25px",
                                       'padding-right': "20px"}),

                            html.Div([
                                dcc.Graph(figure=fig_wordcloud1)],
                                style={'width': '47%', 'align': 'right', 'display': 'inline-block',
                                       "padding-bottom": "15px",
                                       'padding-right': "10px"})
                        ]),

                        #
                        #         html.Div([
                        #             html.Pre(children= "The order of the Quran",
                        #             style={"text-align": "center", "font-size":"100%", "color":"black"})
                        #         ]),

                        html.Div([
                            dcc.Graph(id='the_graph')
                        ], style={'padding-left': "25px", 'padding-right': "25px"}),

                        html.Div([
                            dcc.RangeSlider(id='the_index',
                                            min=0,
                                            max=113,
                                            value=[0, 5],
                                            marks=marks,
                                            step=None)
                        ], style={"padding-left": "15px"}),

                    ],
                    className="main",
                ),
            ], style={"width": "100%px"}
        ),

        html.Div(
            [
                html.Div(
                    [

                    ],
                    style={"width": "100%"},
                ),
                html.Div(
                    [
                        html.P(
                            [

                                html.Br(),

                            ],
                            style={"font-size": "12px"},
                        )
                    ],
                    style={"width": "100%"},
                ),
            ],
            className="footer",
            style={"display": "flex"},
        ),
    ]
)


# ------------------------------------------------------ Callbacks ------------------------------------------------------


@app.callback(Output('wordcloud', 'figure'),
              Input('tabs-example-graph', 'value'),
              Input('dropdown', 'value'),
              )
def render_content(tab, dropdown):
    if tab == 'tab-1-example-graph':
        return generateWordCloud(corpus=eng_corpus, isArabic=False)

    elif tab == 'tab-2-example-graph':
        return generateWordCloud(corpus=arabic_corpus, isArabic=True)


# @app.callback(Output('wordcloud1', 'figure'),
#               Input('tabs-example-graph1', 'value'),
#               Input('dropdown', 'value'),
# )
# def render(tabb,dropdown1):
#     if tab == 'tab-1-example-graph1':
#         return generateWordCloud(corpus=NAMES_text,isArabic=True)
#     elif tab == 'tab-2-example-graph1':
#         return generateWordCloud(corpus=LOC_text,isArabic=true)

# @app.callback(Output('live-update-text', 'children'),
#               [Input('interval-component', 'n_intervals')])
# def update_date(n):
#       return [html.P('Last updated ' +str(datetime.datetime.now()))]


@app.callback(
    Output('the_graph', 'figure'),
    [Input('the_index', 'value')]
)
def update_graph(index_chosen):
    dff = df[(df['index'] >= index_chosen[0]) & (df['index'] <= index_chosen[1])]

    scatterplot = px.scatter(
        data_frame=dff,
        x="chapter",
        y="num_of_ayahs",
        hover_data=['Surah'],
        hover_name=dff['Surah'],
        # size="num_pages",
        size="num_of_ayahs",
        color="chapter",
        text="Surah",
        height=400,
        width=1095,
        log_y=True,
        size_max=35
        , color_continuous_scale='Viridis'
        # # ,range_x=,
        # # range_y=
    )

    scatterplot.update_traces(textposition=['top center', "bottom center"], textfont_size=10, textfont=dict(
        family="Arial",
        size=10,
        color="darkslategray"))
    scatterplot.update_layout(title_text="<b>the order of revelation of the quran </b>", title_x=0.5,
                              title_font_color="#4B9071")

    return (scatterplot)


app.run_server(port=8540)
