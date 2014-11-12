Bright-Lights
=============

This is an effort to build a modular system that mimics the functionality of the Philips Hue technology.
A server will run on a Raspberry Pi base station that can communicate with an array of wirelessly connected Arduino controlled lights.
The base station contains a 'known' list of connected lights and attempts to verify against each light. The base station also contains the present state.

The lights will be connected to Arduino and accept a few configuration values. The available configuration values will be: Fade Speed, Brightness, and Hue(if applicable). It is possible there will be a string of lights connected to an Arduino. If that is the case, then each addressable light will be enumerated and shown as a sublight of the overall connected 'light'.
