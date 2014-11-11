#This will be used to handle incoming http requests
#Uses the bottle python library

import argparse
import logging
import time
from bottle import route, run

@route('/tacos')
def hello():
    return "Tacos are great"

@route('/info/lights')
def display_lights_info()
    #displays all lights and what they are bound to
    logging.info("*->Request to show all lights")
    logging.info("*--->Returned: "+str("something here"))
    return "Success"

@route('/info/lights/<id:int>')
def display_light_info(id):
    #needs access to the previous state database
    logging.info("*->Request to light: "+str(id))
    logging.info("*--->Returned: "+str("something here"))
    return "Success"





if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Runs the server locally with debug")
    args = parser.parse_args()
    if args.debug:
        #runs server in debug mode and stores a debug file documenting what happend during the test
        logging.basicConfig(filename='HTTP_Server.'+str(time.clock()), level=logging.DEBUG)
        logging.info("HTTP server running in debug mode. Using: localhost:8080")
        run(host="localhost", port=8080, debug=True)
    else:
        print("HTTP server running in normal mode\n")
