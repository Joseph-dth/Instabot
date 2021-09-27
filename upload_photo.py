from instabot import Bot
import sys
import random

class upload_photo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
     
    def upload_init(self):


        bot = Bot()

        bot.login( username=self.username, password=self.password )
        print('Login success')

        travel_caption= ['Best experience ever!', 'Cant wait!!', 'Wanna have fun?','Hey fellows!!']
        black_caption= ['Black life metter.', 'God bless America.', 'Peace']
        path = '/Users/user/desktop/python_project/ver2/img/Posts/travel/{rn}.jpeg'.format(rn = str(random.randint(0,15)))
        bot.upload_photo( path, caption=travel_caption[random.randint(0,3)])
        print('Travel uploaded')
        path = '/Users/dog/desktop/ver2/img/Posts/black/{rn}.jpeg'.format(rn = str(random.randint(0,14)))

        #path = '/Users/user/desktop/python_project/ver2/img/Posts/black/{rn}.jpeg'.format(rn = str(random.randint(0,14)))

        bot.upload_photo(path, caption=black_caption[random.randint(0,2)])
        print('Black uploaded')

    def auto_init(self):
    
        bot = Bot()

        bot.login( username=self.username, password=self.password )
        print('Login success')

        travel_caption= ['Best experience ever!', 'Cant wait!!', 'Wanna have fun?','Hey fellows!!']
        black_caption= ['Black life metter.', 'God bless America.', 'Peace']
        path = '/Users/dog/desktop/ver2/img/Posts/travel/{rn}.jpeg'.format(rn = str(random.randint(0,15)))
        bot.upload_photo( path, caption=travel_caption[random.randint(0,3)])
        print('Travel uploaded')
        path = '/Users/dog/desktop/ver2/img/Posts/black/{rn}.jpeg'.format(rn = str(random.randint(0,14)))

        bot.upload_photo(path, caption=black_caption[random.randint(0,2)])
        print('Black uploaded')

        



