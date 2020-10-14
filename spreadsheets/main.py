import gspread, requests
from oauth2client.service_account import ServiceAccountCredentials
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

def token_stopwords(data):
    words = word_tokenize(data)
    words = [word.lower() for word in words if word.isalpha()]
    filtered_words = [word for word in words if word not in stopwords.words('portuguese')]
    return filtered_words

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("spreadsheets/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("[IA] - Ementa").sheet1
data = sheet.get_all_records()

url = 'https://brasilescola.uol.com.br/informatica/inteligencia-artificial.htm'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
table = soup.find('div', {'class' : 'conteudo-materia'})
paragraph = table.find('p', {'style': 'text-align: justify;'}).text
paragraph = paragraph.replace('\n', ' ')

for i in data:
    menu = i['EMENTA']

    words_menu = token_stopwords(menu)
    words_site = token_stopwords(paragraph)

    print("FuzzyWuzzy WRatio: {}".format(fuzz.WRatio(words_menu, words_site)))
    