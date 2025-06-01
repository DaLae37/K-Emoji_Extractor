import json
from src.emoji import emoji

class emoji_parser() :
    def __init__(self) :
        pass
    
    def select_emoji_title(self, data) :
        emoji_list = list()
        
        for content in data["result"]["content"] :
            emo = emoji(content["title"], content["artist"], content["titleUrl"])
            emoji_list.append(emo)
            
        return emoji_list
    
    def get_download_url(self, data) :
        url_list = list()

        for thumbnail in data["result"]["thumbnailUrls"] :
            url_list.append(thumbnail)
        
        return url_list