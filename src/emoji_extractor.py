import requests
import os
from src.emoji_modifier import emoji_modifier

class emoji_extractor() :
    def __init__(self) :
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
    
    def search_emoji_data(self, query) :
        url = "https://e.kakao.com/api/v1/search?query=" + query
        try :
            response = requests.get(url, timeout=2, headers=self.headers, verify=True)
        except requests.exceptions.Timeout as e :
            print("Timeout Error : ", e)
            return 0
            
        if response.status_code == 200 :
            data = response.json()
            return data
        else :
            print("Search Error : ", response.status_code)
    
    def get_emoji_urls(self, titleUrl) :
        url = "https://e.kakao.com/api/v1/items/t/" + titleUrl
        try :
            response = requests.get(url, timeout=2, headers=self.headers, verify=True)
        except requests.exceptions.Timeout as e :
            print("Timeout Error : ", e)
            return 0
        
        if response.status_code == 200 :
            data = response.json()
            return data
        else :
            print("Find Error : ", response.status_code)
            
    def download_emoji(self, url_list, title, width, height) :
        download_success = 0
        
        directory = "emoji/" + title + "/"
        os.makedirs(directory, exist_ok=True)
        
        for url in url_list :
            try :
                response = requests.get(url, timeout=5, headers=self.headers, verify=True)
            except requests.exceptions.Timeout as e :
                break
            
            content_type = response.headers.get("Content-Type")
            extension = "." + content_type.split('/')[-1]
            file_name = str(url).split('/')[-1]
            path = os.path.join(directory, file_name + extension)
            if response.status_code == 200 :
                with open(path, "wb") as file:
                    file.write(response.content)
                if extension == ".gif" :
                    emoji_modifier.resize_animation(path, width, height, extension)
                else :
                    emoji_modifier.resize_image(path, width, height, extension)
                download_success += 1
            else :
                print("Download Error : ", response.status_code)
                
        return download_success