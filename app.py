from flask import Flask
#from redis import Redis
import bprints
import inspect

#from bprint import blueprint
app = Flask(__name__)

for bpname in dir(bprints):
    obj = getattr(bprints,bpname)
    if obj.__name__ != 'storenames' and inspect.ismodule(obj):
        app.register_blueprint(obj.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
