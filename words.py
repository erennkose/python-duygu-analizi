from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak", "âciz", "acımak", "ağrımak", "asla",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk", "bozmak",
            "cimri", 
            "çatışma", "çirkin",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz", "değillemek", "düşmek",
            "eksilmek", "ezmek",
            "fena", "felç", "fahiş",
            "gergin", "göçmek", 
            "hüzün", "hata", "hasta", "hiçbir", "hiç",
            "intihar", "iğrenç", "istifa", "itici",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza", "küflenmek", "kesmek", "kaçırmak", "korku",
            "mikrop", "mutsuz", "mızmız", "maalesef", "mahrum",
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü", "ölüm", 
            "sinir", "solmak", "sorun", "sinirlenmek", "sıkmak", "sıkıcı", "saldırı",
            "tartışma", "tehlike", "ters", "tiksinmek", "tartışmak", "tatsız",
            "unutmak",
            "üzgün", "üzülmek", "üzmek", 
            "vazgeçmek", "vefat", "veda",
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", "yanmak", "yormak", "yalanmış", "yıkmak", "yakmak", "yangın",
            "zehir"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz", "dolayı"}

negDoubleWords = {"ne", "ya"}

reduplications = {"kalkar kalkmaz", "gelir gelmez", "gider gitmez", "yapar yapmaz", "paha biçilmez", "fena değil"}