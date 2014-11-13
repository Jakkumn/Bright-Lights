#Core.py will be used as the main thread that handles taking the information
# from the http server and handing it to the translator to send to the lights

#imports
import argparse
#import logging

#wait for request to pop in from http handler
#operate depending on that request
#request should contain: light(?), intensity, hue


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Runs Light Base in a verbose mode")
    parser.add_argument("-d", "--debug", action="store_true",help="Runs Light Base in a debug mode")
    args = parser.parse_args()
    if args.debug:
        print("Running in debug mode")
        #set logging level
    elif args.verbose:
        print("Running in verbose mode")
        #set logging level
    else:
        print("Out\n")
