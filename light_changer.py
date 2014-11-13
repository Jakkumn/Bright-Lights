#This will contain the light change system along with the output serializer

#import
import argparse
#import logging

#will need to serialize data
    #create start bit:
    #create light identifier (multiple lights on 'network')
    #create light intensity
    #create light hue

#thoughts on being able to configure onboard the lights sensors (like a light with a motion detector, enable/disable that?)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Run Light modifier in a debug mode")
    args = parser.parser_args()
    if args.debug:
        print("Running in debug mode")
        #setup logging
    else:
        print("Lights\n")
