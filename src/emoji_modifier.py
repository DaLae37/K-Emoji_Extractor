import cv2
import numpy as np
from PIL import Image, ImageSequence

class emoji_modifier() :
    def __init__(self) :
        pass
    
    @staticmethod
    def resize_image(path, width, height, extension) :
        emoji_byte_array = np.fromfile(path, np.uint8)
        emoji = cv2.imdecode(emoji_byte_array, cv2.IMREAD_UNCHANGED)
        
        if emoji is None :
            print("Resize Image Load Failed!")
            return
        
        if width != emoji.shape[1] and width != 0:
            if width < emoji.shape[1] :
                inter_method = cv2.INTER_AREA
            else :
                inter_method = cv2.INTER_LINEAR
            emoji = cv2.resize(emoji, (width, emoji.shape[0]), interpolation=inter_method)
            
        if height != emoji.shape[0] and height != 0:
            if height < emoji.shape[0] :
                inter_method = cv2.INTER_AREA
            else :
                inter_method = cv2.INTER_LINEAR
            emoji = cv2.resize(emoji, (emoji.shape[1], height), interpolation=inter_method)
        
        result, encoded_emoji = cv2.imencode(extension, emoji)
        if result:
            encoded_emoji.tofile(path)
    
    @staticmethod
    def resize_animation(path, width, height, extension) :
        emoji = Image.open(path)
        
        duration = emoji.info.get("duration", 100)
        loop = emoji.info.get("loop", 0)
        
        frames = list()
        for frame in ImageSequence.Iterator(emoji):
            image = frame.convert("RGBA")
            image_array = np.array(image)
            
            if width != image_array.shape[1] and width != 0:
                if width < image_array.shape[1] :
                    inter_method = cv2.INTER_AREA
                else :
                    inter_method = cv2.INTER_LINEAR
                image_array = cv2.resize(image_array, (width, image_array.shape[0]), interpolation=inter_method)
            
            if height != image_array.shape[0] and height != 0:
                if height < image_array.shape[0] :
                    inter_method = cv2.INTER_AREA
                else :
                    inter_method = cv2.INTER_LINEAR
                image_array = cv2.resize(image_array, (image_array.shape[1], height), interpolation=inter_method)
                
            frames.append(Image.fromarray(image_array))
            
        frames[0].save(path, save_all=True, append_images=frames[1:], duration=duration, loop=loop, optimize=False, disposal=2)