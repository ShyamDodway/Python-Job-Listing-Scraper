import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

cwd = os.getcwd()
first = True
csv_file = os.path.join(cwd, 'data/company_listings.csv')


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
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': '_t_ds=152955421762415851-5815295542-015295542; _gcl_au=1.1.544378753.1762415862; _ga=GA1.1.832264765.1762415862; _fbp=fb.1.1762415866451.88968096035809698; _clck=143dcoi%5E2%5Eg0s%5E0%5E2136; showChatbot=y; bm_mi=F618941BAB471B5C9350FEB22B5ED151~YAAQz/UwF9KkISaaAQAA3ajtWR1Lsia+vc+yV9RjQEHp6o05e2ZzuXVCPpzIotQNyX32+G+hihtS8QDctbADqiuHlxmCMJTqeAOTEcETcmAau2pKxP8uYFZILlnJ66MoqgfM0yd3kiir0gpyI0JRnq9GLBch5W2e3EAkc2hSicSHDeUw90Utm4LY0YQMKzVWFvMdI9FIlAUpifn5iYWlMOjPqcKg/DB533DJcRh4BB5GBamUImpKgaXOUA96l1HWUdXj4JQeFAbzUTRCQu9/keshYDKsHHNAje8036tvxlPj6D4D0TaNOHbit2vBYeQRuMpIiU22yz1UrMNwQdUK471gQlDC2jt0CcT8~1; _clsk=tjip8p%5E1762445354681%5E1%5E1%5Ee.clarity.ms%2Fcollect; ak_bmsc=6113861008D1D9C404622D4E496A4FA7~000000000000000000000000000000~YAAQz/UwF9WxISaaAQAAKhjuWR0KMQtUqegZ/9Kj3E3qSuTQZfTWdh+bza6Gf6/DhYPu8hIO9HzRtqXHNPAcnlRQqScmadD4Gs6rf8VFLvCp6SAGbvgvL86uyiYuhAAsXWZXZpVnUc+A3ClJxmWruQ9wNV76csJY6BtRRNCS95qu8/0doZ+UmN6YbUqtwv16978PyRqXhzGYN9VGJ26QylcloVZtS89SLGGWKptN64J0iyDvxnOuVsXZfK9zoeXm+X1WZvpoTQioU9az4Domb9RTOsg70dGYJI+JD4iOMnubrntA1cafaeQQrvFppWGtqeDUZcgjitmVt9f2Vep8QxHEUjIYXQ5FXa5D7FK4tV1d7MtcPW9ho6Q21IvQawqyx2YasiB5HxndWAcGqBRouQnlxv95hqQwhVr9tf6Mo8t7dmlUdkRTHDFdtuzEHXMdceTAAZKjy7zi0Re2ICXP7OWGRzhyeciIHzUljGFPddSAiKYqIKvo1fnIU7FrMFGrdsAhkQ==; g_state={"i_l":0,"i_ll":1762446849117,"i_b":"mp3mqG5kb3ZTCVcYIC8JjQqizzBFn0E/+sCy/eYu7ok"}; _ga_HV7DJVVBCW=GS2.1.s1762445345$o4$g1$t1762447015$j56$l0$h0; bm_sv=DDD2404DBB510BE38BC43CC2D0DBF8F4~YAAQzbYRYI65bxGaAQAAgz0HWh3oA0bgN9cdhQI18APdJbK+64UvK3I/qK69LbsbZLpT/GXvW1OIvwTc7USvFi22pi9RrT4VvhJWwqo668qWIxmm5WGNiD+ekWygZvrunanwr8YJMaqIVy0Lv6ovi7CA7u2/SYNT4ZugEE7lhjM3tpPJwHpSTPHIMY+ciO3+VvoPricC+nYkkSy0/AEpStyZxodm45Otf8JZsF70dmqFdU1deKTZ2guyIxBwOKoiqiBgqdsy~1; HOWTORT=cl=1762447014132&r=https%3A%2F%2Fwww.ambitionbox.com%2Flist-of-companies%3Fcampaign%3Dhomepage_companies_widget%26page%3D2&nu=https%3A%2F%2Fwww.ambitionbox.com%2Flist-of-companies%3Fcampaign%3Dhomepage_companies_widget%26page%3D2&ul=1762447025786',
}



current_page = 1
x = True
while x is True:
    params = {
        'campaign': 'homepage_companies_widget',
        'page': current_page,
    }

    response = requests.get('https://www.ambitionbox.com/list-of-companies', params=params, headers=headers,verify=False)
    if response.status_code == 200:
        x = True
        soup = BeautifulSoup(response.text, 'html.parser')

        blocks = soup.find_all('div', class_ = "companyCardWrapper__primaryInformation")
        for block in blocks:
            h2_tag = soup.find('h2', class_ = "companyCardWrapper__companyName")
            company_name = h2_tag.text.strip()
            span_tag = soup.find('span', class_ = "companyCardWrapper__interLinking")
            job_tittle = span_tag.text.strip()
            good_thing = soup.find('span', class_ = "companyCardWrapper__ratingValues")
            rating = good_thing.text.strip()

            record = {
                'Company Name': company_name,
                'Job Title': job_tittle,
                'Rating': rating
            }

            pd.DataFrame([record]).to_csv(csv_file, mode='a', index=False, header= first)
            first = False


            print(company_name)
        print(f"Current Page: {current_page}")
    else:
        x = False

    
    
    current_page += 1

