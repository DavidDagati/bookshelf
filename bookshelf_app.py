import urllib.request
import json
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from functools import partial
# from get_info import getIsbnInfo

def getIsbnInfo(ISBN: str):

	key_file = open('api_key.txt', 'r')
	key = key_file.readline()

	base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

	with urllib.request.urlopen(f"{base_api_link}{ISBN}&key={key}") as f:
		text = f.read()

	decoded_text = text.decode("utf-8")
	obj = json.loads(decoded_text)
	try:
		volume_info = obj["items"][0]
	except:
		return {
			"Authors": None,
			"Title": None,
			"Subtitle": None,
			"Publisher": None,
			"Date Published": None,
			"Description": None,
			"ISBN-10": None,
			"ISBN-13": ISBN,
			"Page Count": None,
			"Print Type": None,
			"Genres": None,
			"Average Rating": None,
			"Ratings Count": None,
			"Image Link": None,
			"Language": None,
			"Preview Link": None,
			"Sale Country": None,
			"Saleability": None,
			"E-Book": None,
			"Summary": None
		}

	response_counter = 0

	search_list = [
		'volume_info["volumeInfo"]["authors"]', # array of strings
		'volume_info["volumeInfo"]["title"]', # str
		'volume_info["volumeInfo"]["subtitle"]', # str
		'volume_info["volumeInfo"]["publisher"]', # str
		'volume_info["volumeInfo"]["publishedDate"]', # str
		'volume_info["volumeInfo"]["description"]', # str,
		'volume_info["volumeInfo"]["industryIdentifiers"][0]["identifier"]', # str
		'volume_info["volumeInfo"]["industryIdentifiers"][1]["identifier"]', # str
		'volume_info["volumeInfo"]["pageCount"]', # int
		'volume_info["volumeInfo"]["printType"]', # str
		'volume_info["volumeInfo"]["categories"]', # array of strings
		'volume_info["volumeInfo"]["averageRating"]', # int
		'volume_info["volumeInfo"]["ratingsCount"]', # int
		'volume_info["volumeInfo"]["imageLinks"]["smallThumbnail"]', # str
		# volume_info["volumeInfo"]["imageLinks"]["thumbnail"], # str (same as above?)
		'volume_info["volumeInfo"]["language"]', # str
		'volume_info["volumeInfo"]["previewLink"]', # str (google books search "isbn: isbn13")
		# volume_info["volumeInfo"]["infoLink"], # str (same as above?)
		'volume_info["saleInfo"]["country"]', # str
		'volume_info["saleInfo"]["saleability"]', # str
		'volume_info["saleInfo"]["isEbook"]', # bool
		'volume_info["searchInfo"]["textSnippet"]' # str
	]

	keys_list = [
			"Authors",
			"Title",
			"Subtitle",
			"Publisher",
			"Date Published",
			"Description",
			"ISBN-10",
			"ISBN-13",
			"Page Count",
			"Print Type",
			"Genres",
			"Average Rating",
			"Ratings Count",
			"Image Link",
			"Language",
			"Preview Link",
			"Sale Country",
			"Saleability",
			"E-Book",
			"Summary"
	]

	for item in range(len(search_list)):
		try:
			if eval(search_list[item]) is not None:
				globals()[keys_list[response_counter]] = eval(search_list[item])
				response_counter += 1
			else:
				response_counter += 1
		except:
			globals()[keys_list[response_counter]] = None
			response_counter += 1

	return {
			"Authors": globals()[keys_list[0]],
			"Title": globals()[keys_list[1]],
			"Subtitle": globals()[keys_list[2]],
			"Publisher": globals()[keys_list[3]],
			"Date Published": globals()[keys_list[4]],
			"Description": globals()[keys_list[5]],
			"ISBN-10": globals()[keys_list[6]],
			"ISBN-13": ISBN,
			"Page Count": globals()[keys_list[8]],
			"Print Type": globals()[keys_list[9]],
			"Genres": globals()[keys_list[10]],
			"Average Rating": globals()[keys_list[11]],
			"Ratings Count": globals()[keys_list[12]],
			"Image Link": globals()[keys_list[13]],
			"Language": globals()[keys_list[14]],
			"Preview Link": globals()[keys_list[15]],
			"Sale Country": globals()[keys_list[16]],
			"Saleability": globals()[keys_list[17]],
			"E-Book": globals()[keys_list[18]],
			"Summary": globals()[keys_list[19]]
	}
class Main(MDApp):
    def build(self):
        screen = MDScreen()
        # scan = ZBarCam()
        isbn_input = MDTextField(hint_text='ISBN', max_text_length=13,ids='isbn_id')
        search = MDRectangleFlatButton(text="Search ISBN",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.20}
                                    )
        search.bind(on_press=partial(getIsbnInfo, self.ids.isbn_id.text))
        # search.bind(on_press=getIsbnInfo(isbn_input.text))
        screen.add_widget(search) 
        screen.add_widget(isbn_input)
        return screen


Main().run()