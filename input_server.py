#This will be used to handle incoming http requests
#Uses the bottle python library

import argparse
import logging
import time
from bottle import run, get, post

@get('/tacos')
def hello():
    #for the lolz
    return "Tacos are great"

@get('/info/lights')
def display_lights_info():
    #displays all lights and what they are bound to
    logging.info("*->Request to show all lights")
    logging.info("*--->Returned: "+str("something here"))
    return "Success"

@get('/info/lights/<id:float>')
def display_light_info(id):
    #needs access to the previous state database
    logging.info("*->Request to light: "+str(id))
    logging.info("*--->Returned: "+str("something here"))
    return "Success"

#Use http/POST for updating lights to new values
    #need to investigate if just appending info to the url is the best way to set light info

@post('/set/lights/<id:float>')
def update_light_info(id):
    #updates database? should communicate with something to notify requested change
    logging.info("*->Request to change light: "+str(id))
    #if success return true
    #else false

#thoughts on being able to configure onboard the lights sensors (like a light with a motion detector, enable/disable that?)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Runs the server locally with debug")
    args = parser.parse_args()
    if args.debug:
        #runs server in debug mode and stores a debug file documenting what happened during the test
        #need to setup a logging setup file
        logging.basicConfig(filename='./Logs/HTTP_Server.'+str(time.clock())+'.log', level=logging.DEBUG)
        logging.info("HTTP server running in debug mode. Using: localhost:8080")
        run(host="localhost", port=8080, debug=True)
    else:
        print("HTTP server running in normal mode\n")
