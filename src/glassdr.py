import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

cwd = os.getcwd()
first = True
csv_file = os.path.join(cwd,'data/glassdoor_company_data.csv')


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.glassdoor.co.in/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    # 'cookie': 'indeedCtk=1j9ec38a6h768800; gdId=0954e194-d4e4-4f7b-bbd5-a6349088e4a5; asst=1762492785.0; _cfuvid=D9FEagnTEcAE14RVoPSFlTgHOX829eiEVjhppAdKTO8-1762492785691-0.0.1.1-604800000; cf_clearance=n019TZsRwI9wgBk2IqPVAxccBGX8Gep4VE.EvNneujk-1762492786-1.2.1.1-WZKwH_KZpiVFjKWIgf.FBIiycoym1NFC.3wMrPgtYXayPTTAdk9oYeJ.n8RzAthOoZ0NBCPdu2WZBlbX8gBdVDKWCibDVdkRip7eizsEsQiXDj_PortsP9q6ZcVU8hotRfQQmrJhiwB2LTdqa9h7KGRKNtMP3hZfVcXWVMtSo0tLh_kd2eTUjVEF27o.NMfRg1o01LoS_RcHteM2vo6e2Voycb04EIRFxkg3TdHpdQ4; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; rl_anonymous_id=RS_ENC_v3_IjA5NTRlMTk0LWQ0ZTQtNGY3Yi1iYmQ1LWE2MzQ5MDg4ZTRhNSI%3D; rsSessionId=1762492787275; AWSALB=WbpdHwfHB/YMpIt6m2PtO9a0VRIVhvIohagkGei1ZRegzO5TttLBmgxx8LqE72/uYM12jwHwEd+RtlGfi6Mgg2NCgJuKqgxoU0mGuzoK+rfeWbKi4UWPsW5rAHgI; AWSALBCORS=WbpdHwfHB/YMpIt6m2PtO9a0VRIVhvIohagkGei1ZRegzO5TttLBmgxx8LqE72/uYM12jwHwEd+RtlGfi6Mgg2NCgJuKqgxoU0mGuzoK+rfeWbKi4UWPsW5rAHgI; JSESSIONID=6A7AF43DB810DE28F9FE2CC6C1B817D0; GSESSIONID=6A7AF43DB810DE28F9FE2CC6C1B817D0; cass=0; _optionalConsent=true; otGeoUS=false; ki_r=; ki_s=240461%3A0.0.0.0.0; rsReferrerData=%7B%22currentPageRollup%22%3A%22%2Fjob%2Fjobs-srch%22%2C%22previousPageRollup%22%3A%22%2Fjob%2Findex%22%2C%22currentPageAbstract%22%3A%22%2FJob%2F%5BOCC%5D-jobs-SRCH_%5BPRM%5D.htm%22%2C%22previousPageAbstract%22%3A%22%2FJob%2Findex.htm%22%2C%22currentPageFull%22%3A%22https%3A%2F%2Fwww.glassdoor.co.in%2FJob%2Findia-data-scientist-intern-jobs-SRCH_IL.0%2C5_IN115_KO6%2C27.htm%22%2C%22previousPageFull%22%3A%22https%3A%2F%2Fwww.glassdoor.co.in%2FJob%2Findex.htm%22%7D; cdArr=; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Nov+07+2025+10%3A51%3A46+GMT%2B0530+(India+Standard+Time)&version=202407.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=262730b5-71b3-427f-a5f5-b9838a0dcca6&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0017%3A1&AwaitingReconsent=false; ki_t=1762492790806%3B1762492790806%3B1762492907941%3B1%3B9; g_state={"i_l":0,"i_ll":1762492908838,"i_b":"ieuby65w1NL/3+9LCkq1RCHMXqO+Dk5MOXxOYRBxSec"}; rl_session=RS_ENC_v3_eyJhdXRvVHJhY2siOnRydWUsInRpbWVvdXQiOjE4MDAwMDAsImV4cGlyZXNBdCI6MTc2MjQ5NDcxMzE1OSwiaWQiOjE3NjI0OTI3ODcyNzUsInNlc3Npb25TdGFydCI6ZmFsc2V9; gdsid=1762492785112:1762494386734:C49654D21B77DA7EA4E2DAF5FC020CF1; bs=ozIRLt-A8_3VL3RiLnwGdQ:bfqHblMrXQ5ch1-U3vsNg-Ojz8gb-uQdlhdmYnBuuZjWrc51L7Kq6uvMNx0rqSQEazC-5L_Rc61xw_XYwKxDR7i0D7MK0edlpCjL0xD4vv4:PpXYc6zo0ZzA9SVNTvxuB9P3x9Sa7kxWk-_m04v04zw; __cf_bm=xt_TdNmXGvfWRtpppepc8ENYeJtzlyQnOolk5.4cKiU-1762494387-1.0.1.1-sI0wxsIdeblfI9McQY_L3E1W9EI8QF3eVWt9k9xuWqSLpZ5Ow7T4ODawnKaoWW9VU3UF7NN8zw._0ame5YZPRn72dx2mDRfAfdJ4rnrdT2U; _dd_s=rum=0&expire=1762495318460',
}


current_page = 1
X = True

while X is True:
    params = {
     'campaign': 'homepage_parameter_campaign',
     'page': current_page,
    }
    
    response = requests.get('https://www.glassdoor.co.in/Job/india-data-scientist-intern-jobs-SRCH_IL.0,5_IN115_KO6,27.htm',headers=headers)
    if response.status_code == 200:
       X = True
       soup = BeautifulSoup(response.text, 'html.parser')

       blocks = soup.find_all('li',class_ = "JobsList_jobListItem__wjTHv JobsList_dividerWithSelected__nlvH7")
       for block in blocks:
           h1_tag = soup.find('h1', class_ = "heading_Heading__aomVx heading_Level1__w42c9")
           job_tittle = h1_tag.text.strip() if h1_tag else None
   
           h4_tag = soup.find('h4', class_ = "heading_Heading__aomVx heading_Subhead__jiUbT")
           comapany_name = h4_tag.text.strip() if h4_tag else None
   
           div_tag = soup.find('div', class_ = "JobDetails_locationAndPay__XGFmY")
           job_type = div_tag.text.strip() if div_tag else None
       
           record = {
               'job_tittle' : job_tittle,
               'company_name' : comapany_name,
               'job_type' : job_type
           }
           
           pd.DataFrame([record]).to_csv(csv_file ,mode = 'a',index = False,header= first)
           
           first = False
           
           print(comapany_name)
       print(f"Current Page: {current_page}")

    else:
       X = False

    current_page += 1

    