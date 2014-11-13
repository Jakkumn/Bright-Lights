#Core.py will be used as the main thread that handles taking the information
# from the http server and handing it to the translator to send to the lights

#imports
import argparse
#import logging

#Multiprocess off the input server and watch for updates to the shared 'light' file
#if change, add work request to light_changer with the changes


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
