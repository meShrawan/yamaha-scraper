import pandas as pd
import os
from paths import save_paths, urls
import Required

class Spec_scraper:
    def main(self, url):
        soup = Required.return_soup(url)
        print(soup)
        exit()
    
    
def main():
    files = [x for x in os.listdir(save_paths['url_save_path'])]
    spec_obj = Spec_scraper()
    
    for file_ in files:
        df = pd.read_csv(os.path.join(save_paths['url_save_path'], file_))
        
        for i, row in df.iterrows():
            link = row['link']
            specification = spec_obj.main(link)
            
            
            
if __name__ == '__main__':
    main()