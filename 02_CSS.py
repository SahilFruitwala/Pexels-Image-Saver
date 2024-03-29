# using CSS selector

import os
import requests  # for requesting to url
from bs4 import BeautifulSoup  # to go through various elements of webpage


find_name = input('What do you want to find?\n')  # get input from user

URL_PEXELS = "https://www.pexels.com/search/"

req = requests.get(URL_PEXELS + find_name + "/")

soup = BeautifulSoup(req.content, 'html.parser')
image = soup.select('img[class="photo-item__img"]')  # find picture element

for i in image:
    if not os.path.exists(find_name):
        os.makedirs(find_name)  # create directory of find name if not exists
    image_url = str(i['data-big-src'])  # get'data-big-src' attribute value
    image_name = str(i['alt']).replace(' ', '_').replace('-', '_')
    img_data = requests.get(image_url).content  # get image data from url
    with open(find_name + '/' + image_name + '.jpg', 'wb') as handler:
        handler.write(img_data)  # wrting data to file?
