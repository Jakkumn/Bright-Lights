#This will be used to handle incoming http requests
#Uses the bottle python library

import argparse
import logging
import logging.config
#import time
import json
from bottle import run, get, post


light_info = None  #this will be the process object handled by the multiprocess manager to allow syncing of dictionaries across modules. The dictionary will contain the light information.

@get('/tacos')
def tacos_are_great():
    #for the lolz
    return "Tacos are great"

@get('/info/lights')
def display_lights_info():
    #displays all lights and what they are bound to
    logging.info("*->Request to show all lights")
    try:
        return light_info["Lights"]["0"]
    except KeyError:
        return "No Lights currently connected"
    except:
        return "Unknown failure"


@get('/info/lights/<id:float>')
def display_light_info(id):
    #needs access to the previous state database
    #note: all items in Lights.json should be of float type. So light 1 is actually 1.0, allows for handling sub lights
    logging.info("*->Request to light: "+str(id))
    logging.info("*--->Returned: "+str(light_info))
    try:
        return light_info["Lights"][str(id)]
    except KeyError:
        return "No light with connection number: "+str(id)

#Use http/POST for updating lights to new values
    #need to investigate if just appending info to the url is the best way to set light info

@post('/set/lights/<id:float>')
def update_light_info(id):
    #updates database? should communicate with something to notify requested change
    logging.info("*->Request to change light: "+str(id))
    return "Not implemented yet"
    #modify spot in light info, manager will handle updating
    #if success return true
    #else false

#thoughts on being able to configure onboard the lights sensors (like a light with a motion detector, enable/disable that?)
#there is a field allowing onboard sensors, not sure what else for that

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Runs the server locally with debug")
    args = parser.parse_args()
    if args.debug:
        #runs server in debug mode and stores a debug file documenting what happened during the test
        #need to setup a logging setup file
        with open("logging_config.json", 'rt') as configurator:
            config = json.load(configurator)
        logging.config.dictConfig(config)
        logging.info("HTTP server running in debug mode. Using: localhost:8080")
        global light_info
        light_info = json.load(open("Lights.json", 'r')) #loads a dummy Lights.json file, no writing capabilities yet
        run(host="localhost", port=8080, debug=True)
    else:
        print("HTTP server running in normal mode\n")
