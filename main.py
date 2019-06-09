# import urllib.request
import os
import requests # for requesting to url
from bs4 import BeautifulSoup # to go through various elements of webpage


find_name = input('What do you want to find?\n') # get input from user

URL_PEXELS = "https://www.pexels.com/search/"
URL_UNSPLASH = "https://unsplash.com/search/photos/"

req = requests.get(URL_PEXELS + find_name + "/")

soup = BeautifulSoup(req.content, 'html.parser')
image = soup.find_all('img', class_ = 'photo-item__img') # find picture element

for i in image:
    if not os.path.exists(find_name):
        os.makedirs(find_name) # create directory of find name if not exists
    image_url = str(i['data-big-src']) # get 'data-big-src'  attribute value
    image_name = str(i['alt']).replace(' ','_').replace('-','_')
    img_data = requests.get(image_url).content # get image data from url
    with open(find_name + '/' + image_name + '.jpg', 'wb') as handler:
        handler.write(img_data) # wrting data to file?

req = requests.get(URL_UNSPLASH + find_name + "/")

soup = BeautifulSoup(req.content, 'html.parser')
div = soup.find_all('div', class_ = 'IEpfq')
for i in div:
	image = i.find_all('img', class_ = '_2zEKz') # find picture element

	for i in image:
		try:
			if not os.path.exists(find_name):
				os.makedirs(find_name) # create directory of find name if not exists
			image_url = str(i['src']) # get 'data-big-src'  attribute value
			image_name = str(i['alt']).replace(' ','_').replace('-','_')
			img_data = requests.get(image_url).content # get image data from url
			with open(find_name + '/' + image_name + '.jpg', 'wb') as handler:
				handler.write(img_data) # wrting data to file
		except Exception as e:
			print(e)