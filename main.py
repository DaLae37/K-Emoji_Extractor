from src.emoji_extractor import emoji_extractor
from src.emoji_parser import emoji_parser

if __name__ == "__main__" :
    extractor = emoji_extractor()
    parser = emoji_parser()
    
    while True :
        query = input("Input an Emoji Name : ")
        data = extractor.search_emoji_data(query)
        
        emoji_list = parser.select_emoji_title(data)
        if len(emoji_list) == 0 :
            print("Find 0 Result, Try Again")
            continue
        else :
            index = 1
            for emo in emoji_list :
                print(str(index) + " : " + emo.title + " - " + emo.artist)
                index += 1
            input_index = int(input("Input an Emoji Index (Input '0' is Exit) : "))
            
            if input_index == 0 :
                break
            elif len(emoji_list) <= input_index - 1 or input_index < input_index - 1 :
                print("Input Correct Index, Try Again")
                continue
            else :              
                title = emoji_list[input_index - 1].title
                data = extractor.get_emoji_urls(emoji_list[input_index - 1].titleUrl)
                
                url_list = parser.get_download_url(data)
                
                input_width = int(input("Input an Emoji Width (Input '0' is Origin) : "))
                input_height = int(input("Input an Emoji Height (Input '0' is Origin) : "))
                success = extractor.download_emoji(url_list, title, input_width, input_height)
                print("Download Success : " + str(success) + "/" + str(len(url_list)))