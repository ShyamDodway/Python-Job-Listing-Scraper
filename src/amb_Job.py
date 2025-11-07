import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

cwd = os.getcwd()
first = True
csv_file = os.path.join(cwd, 'data/ambition_box_job.csv')


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': '"3c149-zduGkjRayUmO8QeUYGfzdxO+BbU"',
    'priority': 'u=0, i',
    'referer': 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': '_t_ds=152955421762415851-5815295542-015295542; _gcl_au=1.1.544378753.1762415862; _ga=GA1.1.832264765.1762415862; _fbp=fb.1.1762415866451.88968096035809698; _clck=143dcoi%5E2%5Eg0s%5E0%5E2136; showChatbot=y; _clsk=1c5k7aa%5E1762451738631%5E1%5E0%5Ee.clarity.ms%2Fcollect; bm_mi=4FBA5F77BC966AB0B72FA3B2B929B27C~YAAQvwVaaGITsCaaAQAAVSfsXh1wFWn1baPDHRZuJZA1WXs53fgCFGgjAOmH4keJZRV4BR0CflCXFRvnSUnAsBbNnscOe8vZfjoIn0JAbaQcWTfm/1rFa8DPYvxOx2+qv6jDKVAB7C7NrTGFr1T2xio0VST6yKieJGz37J+IPpArHUPmk0WF3QiWdBWJqnMWpYPzcufnY/Mb39LNqBc6Sr6sd/XQ7WI7JKKIkKPFsMANYQ071E/e79LI1jV5b9TGuhL054s+RsUaxZag5nNiO/SFMLbHsIg5/xY7lqI4FwPHFY0aJb1m8wPR0GTQuRkhMlBjUU6cX3i2418T4+6TUlQPrrAo2gV4TSCflA==~1; ak_bmsc=F7EAAE3E9501DEAB0071F26F38E89B99~000000000000000000000000000000~YAAQvwVaaNYTsCaaAQAABUPsXh1aS5msc7jmF0nZlRQ1j2hmMP5QW63PopEpdRlnykCVTo/D6cUNtjVRvBK3oOK8pIPTmS1oOQEYRb0wGKsE3v0Dt+Bs1h588t71btiEeIoXggouBiMFU2a0zPVInW+fBye4cz/ogpVhOuVCQKAzl3+xoqWOs4Os1sDC5QeB17Toj7o5gvgu6cf6QXmOyKCRNTTHq+idk9+wVN2uHeKnE08nHSpbBTTQqMIDR3SsIuhtg1fTsIdIXbihgXw2g+YxsqsuoLfetOx6Lq5dSNWZkeopHXB7+qNEzq642PmzJLV1MUI30tjsp7LIveqT7LHNMvYSd+kdz24XP1pGspNOEXLWu/b6FXa4OE6YDWnVn7IoJrzvpXaI8ewD6j0oUx3TMHMnVEstAsc7/9RDGLQH5dUsSlzUiDKoVQzXIU3DyXOlAtsrlpdorxl6nefXgeOrxpHNBstEKSTMT1zZYWVt/mRmdc1dKt7UrBMdeQWEXBytFJ18egHMyp51nzXHO95VodBUzwfib/kRfcA57cABVqSqY6Ms2dE=; _ga_HV7DJVVBCW=GS2.1.s1762529134$o8$g1$t1762529389$j8$l0$h0; g_state={"i_l":0,"i_ll":1762529393192,"i_b":"4Mzitw2lBKXN3nshpbTiLcJGpQPFO+7HFK64+orA5hQ"}; bm_sv=80B64B079041FC943E9D6FE7CB5DC626~YAAQvwVaaIgqsCaaAQAAMqjwXh3sPaNVOVmlcDmQjbIHOpm8u7GHKPnhTmDjZ33iqRRMi75XB7K6O/66iShLeikchOz5668Sy4CqIBMKuG+hT7/kLABrEFzzTiMe1Q7RageWfsmXG1TjXnJu1v12RWgS+JYAGdFCx20Bcsr5nFBclndT6L3JKY+XY8AsnFZmArx+aVrOrrRtNCDSZzXEIktpRrtq7xbprDSDYXfRFYA8MXlXzYQsqFR1IN2abG5Bk6PxTFm7~1; HOWTORT=ul=1762529428596&r=https%3A%2F%2Fwww.ambitionbox.com%2Fjobs%3Fcampaign%3Ddesktop_nav&hd=1762529387419&cl=1762529386992&nu=https%3A%2F%2Fwww.ambitionbox.com%2Fjobs',
}


current_page = 1
x = True
while x is True:
    params = {
        'campaign': 'desktop_nav',
        'page': current_page,
    }

    response = requests.get('https://www.ambitionbox.com/jobs', params=params,  headers=headers,verify = False)
    if response.status_code == 200:
        X = True
        soup = BeautifulSoup(response.text, 'html.parser')
        blocks = soup.find_all('div', class_ = "jobInfoCard")

        for block in blocks:
            div_tag = block.find('a',class_ = "title noclick")
            designation = div_tag.text.strip() if div_tag else None

            div_tag_2 = block.find('div',class_ = "company-info")
            company_name = div_tag_2.find('p',class_ = "company body-medium").text.strip() if div_tag_2 else None

            div_tag_3 = block.find('i', class_='icon icon-work')
            experience = div_tag_3.find_next('p').text.strip() if div_tag_3 else None


            div_tag_4 = block.find('div',class_ = "entity loc")
            location = div_tag_4.find('p',class_="body-small-l").text.strip() if div_tag_4 else None

            div_tag_5 = block.find('div',class_ = "entity")
            skills = div_tag_5.find('p',class_ ="body-small-l").text.strip() if div_tag_5 else None

            div_tag_6 = block.find('i',class_ = "icon icon-wallet")
            salary = div_tag_6.find_next('p').text.strip() if div_tag_6 else None 

            record = {
                "Desiganation" : designation,
                "Company Name" : company_name,
                "Experience" : experience,
                "Location"  : location,
                "Skills" : skills,
                "Salaary" : salary 

            }

            pd.DataFrame([record]).to_csv(csv_file, mode='a', index=False, header = first)
            first = False

            print(company_name)
        print(f"Current Page: {current_page}") 

    else:
        X = False

    current_page += 1





            


