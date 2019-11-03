import requests
from bs4 import BeautifulSoup
def get_info(id=None):
 if(len(id) == 18 and not id.isdigit()):
  try:
    # Needed declarations
    url = "https://www.toxic-bot-list.ml/view/{}".format(id)
    data_returned = requests.get(url).text
    data_parsed = BeautifulSoup(data_returned, features="html.parser")
    # Return object
    return_object = {
        "avatar_url": data_parsed.select_one('body > div.deneme > center > img[src]')['src'],
        "owner": data_parsed.select_one('body > div.deneme > center > h3:nth-child(3)').text,
        "authorize_link": data_parsed.find_all('a')[11]['href'],
        "votes": data_parsed.find_all('button')[2].text,
        "long_description": data_parsed.select_one('#descrption').text,
        "short_description": data_parsed.select_one('h6').text,
        "library": data_parsed.find_all('button')[len(data_parsed.find_all('button')) - 1].text
    }
    return {
        'Success': return_object
    }
  except Exception as e:
    return {
        'Error': e
    }
 else:
    return {
        'Error' : 'Check your ID\'s type and length'
    }
    """
    @return : Returns the info about the given ID bot
    @rtype : object
    @param :
        id = The bot's unique ID
    @ptype : string
    """