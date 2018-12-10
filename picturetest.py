from PIL import Image
import json

with open("weatherDisplay.json", "r") as jsonWeather:
    weatherDict = json.load(jsonWeather)



i = 1
while i < 48:
    print(weatherDict["images"][str(i)])
    tempImagePath = "MirrorFiles/1x/" + weatherDict["images"][str(i)] + ".png"
    tempImage = Image.open(tempImagePath)
    i = i + 1