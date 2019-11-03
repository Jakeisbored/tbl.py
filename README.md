##Welcome to toxic bot list api python wrapper docs!
###Docs
####There are too instances of this package are:
###Bots
**=> Methods**
##### 1-get_info()
````python

    @return : Returns the info about the given ID bot
    @rtype : object
    @param :
        id = The bot's unique ID

````
#####Example:
````python
from tbl import bots # importing the bots instance from the package
print(bots.get_info('593000879876079611')) # printing the result of the method with the id passed
````