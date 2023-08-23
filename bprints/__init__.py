from redis import Redis
from bprints.storenames import storenames
#storenames = ['redis']
stores = []
for store in storenames.keys():
    stores.append(Redis(host=store, port=storenames[store]))