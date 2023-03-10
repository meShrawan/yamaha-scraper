import pandas as pd
from paths import urls, save_paths
import os
import Required


class Url_scraper:
    def __init__(self, url, path):
        self.path = path
        self.url = url

    def return_df(lists):
        df = pd.DataFrame(lists)
        df['price'] = df['price'].str.replace(',', '').astype(int)
        return df
    
    def main(self):
        soup = Required.return_soup(self.url)
        lists = list()

    
        content = soup.find(id = 'content')
        lis = content.find_all('li')
        
        for i in lis:

            link_tag = i.find('a')
            link = link_tag['href']
            name = i.find('h5').text
            price = i.find('bdi').text.replace('₨', '')
            
            lists.append(
                {
                    'link':link,
                    'name':name,
                    'price':price
                }
            )
        
        df = Url_scraper.return_df(lists)
        
        save_file = self.url.split('/')[-2]
        save_path = os.path.join(self.path, save_file+'.csv')
        
        
        df.to_csv(save_path, index=False)
        
def main():
    motercycle_obj = Url_scraper(urls['motorcycle'], save_paths['url_save_path'])
    motercycle_obj.main()
    
    scooter_obj = Url_scraper(urls['scooter'],save_paths['url_save_path'])
    scooter_obj.main()

if __name__ == '__main__':
    main()
