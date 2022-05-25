import shutil
from fastapi import UploadFile, HTTPException, status
from .string_manipulate import StringManipulate


class UploadFileUtils:

    def __init__(self, file:UploadFile):
        self.file = file
    
    def upload_image(self, path = './assets/img/', accepted_extensions = [], prefix='img', add_random_string = True, add_millisecond = True):
        
        # path url
        if path.endswith('/') == False:
            path = path+'/'

        # file extension check and exception handle
        file_type = self.file.content_type.split('/')
        
        # dot added before file extension
        file_extension = f'.{file_type[1]}'

        if len(file_type[0]) != 'image' and file_type[1] not in accepted_extensions:
            raise HTTPException(status_code= status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="media extension not supported")


        # random key
        random_string = '-' + StringManipulate.random_str(size=6) if add_random_string else ''
        millsecond = '-' + str(StringManipulate.current_millisecond()) if add_millisecond else ''

        # new image name
        new_image_name = f'{path}{prefix}{random_string}{millsecond}{file_extension}'
        
        # create image object
        with open(new_image_name, 'wb') as buffer:
            shutil.copyfileobj(self.file.file, buffer)
        

        return f'{prefix}{random_string}{millsecond}{file_extension}'