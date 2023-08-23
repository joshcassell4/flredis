from flask import Blueprint
#from redis import Redis
#from storenames import storenames
from bprints import stores

blueprint1 = Blueprint('blueprint1', __name__)
portnum = 6379
#storesn = ['redis']
# stores = []
# for store in storenames:
#     stores.append(Redis(host=store, port=portnum))

@blueprint1.route('/')
def index():
    
    stores[0].incr('hits')
    x = stores[0].command_count()

    counter = str(stores[0].get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s). Count returned "+ str(x)
    #return "This is an example app"
