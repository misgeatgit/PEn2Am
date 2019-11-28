# encoding=utf8
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

KEY_MAP={
        'ha':['ሀ', 'ሐ', 'ሓ', 'ሗ', 'ሃ', 'ኸ'], 'hu':['ሁ', 'ኹ', 'ሑ', 'ሗ'],
        'hi':['ሂ', 'ሒ', 'ኺ'], 'haa':['ሃ', 'ሀ', 'ሓ', 'ሐ', 'ኸ', 'ኻ'],
        'he':['ሄ', 'ሔ', 'ኼ'], 'h':['ህ', 'ሕ'], 'ho':['ሆ', 'ሖ', 'ኾ'],
        'la':['ለ'], 'lu':['ሉ'], 'li':['ሊ', 'ል'], 'laa':['ላ'], 'le':['ሌ'], 'l':['ል'],
        'lo':['ሎ'], 'lua':['ሏ'],
        'ma':['መ'], 'mu':['ሙ'], 'mi':['ሚ', 'ም'], 'ma':['ማ'], 'me':['ሜ'],
        'm':['ሚ', 'ም'], 'mo':['ሞ'], 'mua':['ሟ'],
        'sa':['ሰ','ሠ'], 'su':['ሱ', 'ሡ'], 'si':['ሲ', 'ሢ'], 'saa':['ሳ', 'ሣ'],
        'se':['ሴ', 'ሤ'], 's':['ስ', 'ሥ'], 'so':['ሶ', 'ሦ'], 'sua':['ሷ'],
        'ra': ['ረ'], 'ru':['ሩ'], 'ri':['ሪ'], 'raa': ['ራ'], 're': ['ሬ'],
        'r':['ር'], 'ro':['ሮ'], 'rua': ['ሯ'],
        'sha': ['ሸ'], 'shu':['ሹ'], 'shi':['ሺ'], 'shaa': ['ሻ'], 'she':['ሼ'],
        'sh':['ሽ'], 'sho':['ሾ'], 'shua':['ሿ'],
        'qa':['ቀ','ቐ'], 'qu':['ቁ', 'ቑ'], 'qi':['ቂ', 'ቒ'], 'qaa':['ቃ', 'ቓ', 'ቕ'],
        'qe':['ቄ', 'ቔ'], 'q':['ቅ'], 'qo':['ቆ', 'ቖ'], 'qua':['ቇ'],
        'ka':['ከ', 'ቀ'], 'ku':['ኩ', 'ቁ'], 'ki':['ኪ', 'ቂ'], 'kaa':['ካ', 'ቃ'],
        'ke':['ኬ', 'ቄ'], 'k':['ክ', 'ቅ'], 'ko':['ኮ', 'ቆ'], 'kua':['ኯ'],
        'va':['ቨ'], 'vu':['ቩ'], 'vi':['ቪ'], 'vaa':['ቫ'], 've':['ቬ'], 'v':['ቭ'],
        'vo':['ቮ'], 'vua':['ቯ'],
        'ba':['በ'], 'bu':['ቡ'], 'bi':['ቢ'], 'baa':['ባ'], 'be':['ቤ'],  'b':['ብ'],
        'bo':['ቦ'], 'bua':['ቧ'],
        'ta':['ተ', 'ጠ'], 'tu':['ቱ', 'ጡ'], 'ti':['ቲ', 'ጢ'], 'taa':['ታ', 'ጣ'],
        'te':['ቴ', 'ጤ'],
        't':['ት', 'ጥ'], 'to':['ቶ', 'ጦ'], 'tua':['ቷ', 'ጧ'],
        'cha':['ቸ', 'ጨ'], 'chu':['ቹ', 'ጩ'], 'chi':['ቺ', 'ጪ'], 'chaa':['ቻ', 'ጫ'],
        'che':['ቼ', 'ጬ'],
        'ch':['ች', 'ጭ'], 'cho':['ቾ', 'ጮ'], 'chua':['ቿ', 'ጯ'],
        'ca':['ጨ'], 'cu':['ጩ'], 'ci':['ጪ'], 'caa':['ጫ'], 'ce':['ጬ'], 'c':['ጭ'],
        'co':['ጮ'], 'cua':['ጯ'],
        'na':['ነ', 'ና'], 'nu':['ኑ'], 'ni':['ን','ኒ'], 'ne':['ነ','ኔ'], 'n':['ን'],
        'no':['ኖ'], 'nua':['ኗ'],
        'gna':['ኘ', 'ኛ'], 'gnu': ['ኙ'], 'gni':['ኚ'], 'gne':['ኜ'], 'gn':['ኝ'],
        'gno':['ኞ'], 'gno':['ኟ'],
        'a':['አ', 'ኣ', 'ዐ', 'ዓ'], 'u':['ኡ', 'ዑ'], 'i':['ኢ', 'ዒ'],
        'e':['ኤ', 'እ', 'ኧ', 'ዔ', 'ዕ'], 'o':['ኦ', 'ዖ'],
        'wa':['ወ'], 'wu':['ዉ'], 'wi':['ዊ'], 'wa':['ዋ'], 'we':['ዌ'], 'w':['ው'],
        'wo':['ዎ'],
        'za':['ዘ'], 'zu':['ዙ'], 'zi':['ዚ'], 'za':['ዛ'], 'ze':['ዜ'], 'z':['ዝ'],
        'zo':['ዞ'], 'zua':['ዟ'],
        'zha':['ዠ'], 'zhu':['ዡ'], 'zhi':['ዢ'], 'zhaa':['ዣ'], 'zhe':['ዤ'],
        'zh':['ዥ'], 'zho':['ዦ'], 'zhua':['ዧ'],
        'ya':['የ'], 'yu':['ዩ'], 'yi':['ዪ'], 'yaa':['ያ'], 'ye':['ዬ'], 'y':['ይ'],
        'yo':['ዮ'], 'yua':['ዯ'],
        'da':['ደ', 'ዳ'], 'du':['ዱ'], 'di':['ዲ',],'de':['ዴ'], 'd':['ድ'],
        'do':['ዶ'], 'dua':['ዷ'],
        #{''da','ዸ'},{''du','ዹ'},{''di',},{''daa','ዻ'},{''de',},{''d','ዽ'},
        #{''do','ዾ'},{''dua','ዿ'},
        'pa':['ጰ', 'ፐ', 'ጳ'], 'pu':['ጱ', 'ፑ'], 'pi':['ጲ', 'ፒ'], 'pa':['ፓ'],
        'pe':['ጴ', 'ፔ'], 'p':['ጵ', 'ፕ'], 'pua':['ጷ', 'ፗ'], 'po':['ጶ', 'ፖ'],
        'tsa':['ፀ', 'ጸ'], 'tsu':['ፁ', 'ጹ'], 'tsi':['ፂ', 'ጺ'], 'tsa':['ፃ', 'ጻ'],
        'tse':['ፄ', 'ጼ'],
        'ts':['ፅ', 'ጽ'], 'tso':['ፆ', 'ጾ'], 'tsua':['ፇ', 'ጿ'],
        'ja':['ጀ'], 'ju':['ጁ'], 'ji':['ጂ'], 'jaa':['ጃ'], 'je':['ጄ'], 'j':['ጅ'],
        'jo':['ጆ'], 'jua':['ጇ'],
        'ga':['ገ'], 'gu':['ጉ'], 'gi':['ጊ'], 'gaa':['ጋ'], 'ge':['ጌ'], 'g':['ግ'],
        'go':['ጎ'], 'gua':['ጏ'],
        #{''ga','ጘ'},{''gu','ጙ'},{''gi','ጚ'},{''gaa','ጛ'},{''ge','ጜ'},{''g','ጝ'}
        #,{''go','ጞ'},{''gua','ጟ'},
        'fa':['ፈ'], 'fu':['ፉ'], 'fi':['ፊ'], 'faa':['ፋ'], 'fe':['ፌ'], 'f':['ፍ'],
        'fo':['ፎ'], 'fua':['ፏ'],
        #NUMERALS
        '1':'፩', '2':'፪', '3':'፫', '4':'፬', '5':'፭', '6':'፮', '7':'፯', '8':'፰',
        '9':'፱', '10':'፲',
        '20':'፳', '30':'፴', '40':'፵', '50':'፶', '60':'፷', '70':'፸', '80':'፹',
        '90':'፺', '100':'፻',
        '10000':'፼'
        }
