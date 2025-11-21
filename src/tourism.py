import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


cwd = os.getcwd()
first = True
csv_file = os.path.join(cwd,'data/tourism_destination.csv')

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1611933933.1763664051; _gcl_au=1.1.940625819.1763664051; userCountry=IN; G_ENABLED_IDPS=google; _fbp=fb.1.1763664053672.923157403748907914; _ctpuid=6ad2cced-1823-48a8-a6da-e86a3f36d351; timeoutPopupShown=true; JSESSIONID=46744147D6B35C02FFBCA176977C093F; _ga_2EYTXREWVK=GS2.1.s1763749363$o2$g1$t1763750646$j60$l0$h1899049190; userCookie={"pageviews":13}; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%223314be9e-e2d4-41d6-ac57-4b3e3edd443b%5C%22%2C%5B1763664053%2C302000000%5D%5D%22%5D%5D%5D; __gads=ID=1d592c99f779d96b:T=1763664078:RT=1763750647:S=ALNI_MYuntZCrDp5dLTjEbKbH17GGewidg; __gpi=UID=000011b9d1b92ce0:T=1763664078:RT=1763750647:S=ALNI_MaENTdpGJXgd9koF6OSqO-cZV87XA; __eoi=ID=8922ebd3a122a32f:T=1763664078:RT=1763750647:S=AA-AfjagN5QDxZxs0wHjH--egxre; FCNEC=%5B%5B%22AKsRol8DFHQZXJy66X99HE0jzkXfaOVq54CXA0z0Xn_vb9HO331GA-RF09PpyKP3rhAEY-jfjEmi9hezQsJpEBL-Q-UvZX5S64D0-7IgGZAd3VVYNT9tzzYMEyIZPJUs2LJeBiYSIWzJjYLO9SNl27xF_rYnAYTYKQ%3D%3D%22%5D%5D',
}

current_page = 0
X = True
while X is True:
    params = {
    'pageNum': current_page,
}


    response = requests.get(
    'https://www.holidify.com/country/india/places-to-visit.html',
    params=params,
    headers=headers,
)
    if response.status_code == 200:
        X = True
        soup = BeautifulSoup(response.text, 'html.parser')
        blocks = soup.find_all('div',class_ = 'card content-card')
        for block in blocks:
            h3_tag = block.find('h3', class_ = 'card-heading')
            place_name = h3_tag.text.strip() if h3_tag else None

            p_tag = block.find('p', class_ = 'mb-2')
            place_location = p_tag.text.strip() if p_tag else None

            pp_tag = block.find('p', class_ = 'mb-3')
            known_for  = pp_tag.text.strip() if pp_tag else None

            record = {
                'place_name' : place_name,
                'place_location' : place_location,
                'known_for' : known_for
            }

            df = pd.DataFrame([record])
            df.to_csv(csv_file ,mode = 'a',index = False, header = first)

            first = False
            print("place_name")
        
        print(f"Completed page {current_page}")

    else:
           X = False
    
    current_page += 1