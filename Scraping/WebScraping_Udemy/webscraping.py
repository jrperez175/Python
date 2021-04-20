from bs4 import BeautifulSoup
import requests
import pandas as pd

def request_soup(url):
    response = requests.get(url)
    data = response.text
    return BeautifulSoup(data,'html.parser')

if __name__ == "__main__":
    url="https://www.programmableweb.com/category/all/apis"
    npo_apis = {}
    apis_no = 0
    while True:
        soup = request_soup(url)
        apis_table = soup.find('tbody')
        for tr in apis_table.select('tr'):
            name_tag = tr.find("td",{"class":"views-field views-field-pw-version-title"})
            name = name_tag.text if name_tag else "N/A"
            description = tr.find("td",{"class":"views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8"}).text
            category = tr.find("td",{"class":"views-field views-field-field-article-primary-category"}).text
            link = 'https://www.programmableweb.com' + tr.find("td",{"class":"views-field views-field-pw-version-title"}).a.get("href")

            apis_no+=1
            npo_apis[apis_no]=[name,description,category,link]

            print("Api Name: ",name, "\nDescription: ",description,"\nCategory:",category,"\nLink: ",link,"\n-----")
        url_tag = soup.find('a',{'title':'Go to next page'})
        if url_tag.get('href') and apis_no <=5:
            url = 'https://www.programmableweb.com' + url_tag.get('href')
            print(url)
            #break
        else:
            break
        
    print('Total Apis: ', apis_no)

    #DataFrame
    npo_apis_df = pd.DataFrame.from_dict(npo_apis,orient='index',columns=['Api Name','Description','Category','Link'])
    #CSV
    npo_apis_df.to_csv('npo_apis.csv',sep='|')