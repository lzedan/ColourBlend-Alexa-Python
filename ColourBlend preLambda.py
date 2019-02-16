import turtle
import math



"""
----------------------------------------------------------------------------------
CLASS: Colour

Colour is a construction made up of three int values:
int red
int green
int blue

Each value corresponds to the the channel in an 8-bit value ranging from 0 to 255.

The following functions are provided by this library:
fromHex
fromWebColour
determineInput
convertToHSB
convertToRGB
blend
add
subtract
fuse
toString
display

Not all functions necessarily have self as an input requirement.
TODO: Implement functions for converting between RGB and CYMK
TODO: Build a function that provides more verbose output
"""
class colour():

    """
    the webColourDict is a Hash Table that contains the name of the HTML standard web colours as
    keys with their RGB values in an integer array. I'd like to include some Pantone colours down
    the line but this is a good starting point.
    """
    webColourDict = {
        "alice blue"                :   [240,248,255],
        "antique white"             :   [250,235,215],
        "aqua"                      :   [0,255,255],
        "aquamarine"                :   [127,255,212],
        "azure"                     :   [240,255,255],
        "beige"                     :   [245,245,220],
        "bisque"                    :   [255,228,196],
        "black"                     :   [0,0,0],
        "blanched almond"           :   [255,235,205],
        "blue"                      :   [0,0,255],
        "blue violet"               :   [138,43,226],
        "brown"                     :   [165,42,42],
        "burly wood"                :   [222,184,135],
        "cadet blue"                :   [95,158,160],
        "chartreuse"                :   [128,255,0],
        "chocolate"                 :   [127,255,0],
        "coral"                     :   [255,127,80],
        "cornflower blue"           :   [100,149,237],
        "corn silk"                 :   [255,248,220],
        "crimson"                   :   [220,20,60],
        "cyan"                      :   [0,255,255],
        "dark blue"                 :   [0,0,139],
        "dark cyan"                 :   [0,139,139],
        "dark golden rod"           :   [184,134,11],
        "dark gray"                 :   [169,169,169],
        "dark grey"                 :   [169,169,169],
        "dark green"                :   [0,100,0],
        "dark khaki"                :   [189,183,107],
        "dark magenta"              :   [139,0,139],
        "dark olive green"          :   [85,107,47],
        "dark orange"               :   [255,140,0],
        "dark orchid"               :   [153,50,204],
        "dark red"                  :   [139,0,0],
        "dark salmon"               :   [233,150,122],
        "dark sea green"            :   [143,188,143],
        "dark slate blue"           :   [72,61,139],
        "dark slate gray"           :   [49,79,79],
        "dark slate grey"           :   [49,79,79],
        "dark turquoise"            :   [0,206,209],
        "dark violet"               :   [148,0,211],
        "deep pink"                 :   [255,20,147],
        "deep sky blue"             :   [0,191,255],
        "dim gray"                  :   [105,105,105],
        "dim grey"                  :   [105,105,105],
        "dodger blue"               :   [30,144,255],
        "fire brick"                :   [178,34,34],
        "floral white"              :   [255,250,240],
        "forest green"              :   [34,139,34],
        "fuchsia"                   :   [255,0,255],
        "gainsboro"                 :   [220,220,220],
        "ghost white"               :   [248,248,255],
        "gold"                      :   [255,215,0],
        "golden rod"                :   [218,165,32],
        "gray"                      :   [128,128,128],
        "grey"                      :   [128,128,128],
        "green"                     :   [0,128,0],
        "green yellow"              :   [173,255,47],
        "honey dew"                 :   [240,255,240],
        "hot pink"                  :   [255,105,180],
        "indian red"                :   [205,92,92],
        "indigo"                    :   [75,0,130],
        "ivory"                     :   [255,255,240],
        "khaki"                     :   [240,230,140],
        "lavender"                  :   [230,230,250],
        "lavender blush"            :   [255,240,245],
        "lawn green"                :   [124,252,0],
        "lemon chiffon"             :   [255,250,205],
        "light blue"                :   [173,216,230],
        "light coral"               :   [240,128,128],
        "light cyan"                :   [224,255,255],
        "light golden rod yellow"   :   [250,250,210],
        "light gray"                :   [211,211,211],
        "light grey"                :   [211,211,211],
        "light green"               :   [144,238,144],
        "light pink"                :   [255,182,193],
        "light salmon"              :   [255,160,122],
        "light sea green"           :   [32,178,170],
        "light sky blue"            :   [135,206,250],
        "light slate gray"          :   [119,136,153],
        "light slate grey"          :   [119,136,153],
        "light steel blue"          :   [176,196,222],
        "light yellow"              :   [255,255,224],
        "lime"                      :   [0,255,0],
        "lime green"                :   [50,205,50],
        "linen"                     :   [250,240,230],
        "magenta"                   :   [255,0,255],
        "maroon"                    :   [128,0,0],
        "medium aqua marine"        :   [102,205,170],
        "medium blue"               :   [0,0,205],
        "medium orchid"             :   [186,85,211],
        "medium purple"             :   [147,112,219],
        "medium sea green"          :   [60,179,113],
        "medium slate blue"         :   [123,104,238],
        "medium spring green"       :   [0,250,154],
        "medium turquoise"          :   [72,209,204],
        "medium violet red"         :   [199,21,133],
        "midnight blue"             :   [25,25,112],
        "mint cream"                :   [245,255,250],
        "misty rose"                :   [255,228,225],
        "moccasin"                  :   [255,228,181],
        "navajo white"              :   [255,222,173],
        "navy"                      :   [0,0,128],
        "old lace"                  :   [253,245,230],
        "olive"                     :   [128,128,0],
        "olive drab"                :   [107,142,35],
        "orange"                    :   [255,165,0],
        "orange red"                :   [255,69,0],
        "orchid"                    :   [218,112,214],
        "pale golden rod"           :   [238,232,170],
        "pale green"                :   [152,251,152],
        "pale turquoise"            :   [175,238,238],
        "pale violet red"           :   [219,112,147],
        "papaya whip"               :   [255,239,213],
        "peach puff"                :   [255,218,185],
        "peru"                      :   [205,133,63],
        "pink"                      :   [255,192,203],
        "plum"                      :   [221,160,221],
        "powder blue"               :   [176,224,230],
        "purple"                    :   [128,0,128],
        "rebecca purple"            :   [102,51,153],
        "red"                       :   [255,0,0],
        "rosy brown"                :   [188,143,143],
        "royal blue"                :   [65,105,225],
        "saddle brown"              :   [139,69,19],
        "salmon"                    :   [255,128,114],
        "sandy brown"               :   [244,164,96],
        "sea green"                 :   [46,139,87],
        "sea shell"                 :   [255,245,238],
        "sienna"                    :   [160,82,45],
        "silver"                    :   [192,192,192],
        "sky blue"                  :   [135,206,235],
        "slate blue"                :   [106,90,205],
        "slate gray"                :   [112,128,144],
        "slate grey"                :   [112,128,144],
        "snow"                      :   [255,250,250],
        "spring green"              :   [0,255,127],
        "steel blue"                :   [70,130,180],
        "tan"                       :   [210,180,140],
        "teal"                      :   [0,128,128],
        "thistle"                   :   [216,191,216],
        "tomato"                    :   [255,99,71],
        "turquoise"                 :   [64,224,208],
        "violet"                    :   [238,130,238],
        "wheat"                     :   [245,222,179],
        "white"                     :   [255,255,255],
        "white smoke"               :   [245,245,245],
        "yellow"                    :   [255,255,0],
        "yellow green"              :   [154,205,50]
    }

    #The initialisation/constructor simply takes three int values and places them
    #in self. Again, only values from 0 to 255 are valid, but this is dealt with the
    #supporting functions.
    def __init__(self, red = None, green = None, blue = None):
        if(red is None):
            red = 0
        if(green is None):
            green = 0
        if(blue is None):
            blue = 0

        self.red = red
        self.green = green
        self.blue = blue

    #-----------fromHex-----------
    #The input here is a string, representing an RGB value in hex code format.
    #The function parses substrings and converts them into decimal numbers from
    #their string values.
    def fromHex(self, hexCode):
        if "#" in hexCode:
            hexCode = hexCode[1:]
        if len(hexCode) == 6:
            self.red = int(hexCode[0:2], 16)
            self.green = int(hexCode[2:4], 16)
            self.blue = int(hexCode[4:], 16)
    
    #-----------fromWebColour-----------
    #The input is a string, hopefully it's one of the HTML standard web colours
    #that are defined in our hash table.
    def fromWebColour(self, webColour):
        self.red = webColourDict[webColour][0]
        self.green = webColourDict[webColour][1]
        self.blue = webColourDict[webColour][2]

    #-----------determineInput-----------
    #The input is a string
    #Using some if statements, the function will determine if the user has entered either
    #a hexcode or a HTML web colour, and then construct a new colour object from that input.
    #If both tests fail, the function returns a false value.
    #That could probably be changed to something more pragmatic in a future version.    
    def determineInput(someColour):
    		hexCompliant = True
    		
    		if(len(someColour) <= 7):
    			for i in someColour:
    				if(i >= 'g') and (i != '#'):
    					hexCompliant = False
    		else:
    			hexCompliant = False
    			
    		newColour = colour()
    		
    		if(hexCompliant):
    			newColour.fromHex(someColour)
    		elif(hexCompliant == False):
    			if(someColour in webColourDict):
    				newColour.fromWebColour(someColour)
    			else:
    				newColour = False
    		
    		return newColour

    #-----------convertToHSB-----------
    #Taking a colour object as input, convert the values into a Hue, 
    #Saturation, and Brightness array.
    def convertToHSB(self):
        #First find the Brightness
        channelPercents = []
        rgbChannels = [self.red, self.green, self.blue]
        conversionRed = self.red/255
        conversionGreen = self.green/255
        conversionBlue = self.blue/255
        channelPercents.append(conversionRed)
        channelPercents.append(conversionGreen)
        channelPercents.append(conversionBlue)

        channelMax = max(channelPercents)
        channelMin = min(channelPercents)

        Brightness = channelMax*100

        #Now calculate the Saturation
        if (channelMax != 0):
            Saturation = (channelMax - channelMin)/channelMax
        else:
            Saturation = 0.0

        Saturation = Saturation * 100

        #Finally, the Hue value
        divisor = channelMax - channelMin
        if(max(channelPercents) == self.red/255):
            Hue = (conversionGreen - conversionBlue)/divisor
        elif(max(channelPercents) == self.green/255):
            Hue = 2.0 + (conversionBlue - conversionRed) / divisor
        elif(max(channelPercents) == self.blue/255):
            Hue = 4.0 + (conversionRed - conversionGreen) / divisor
        
        Hue = Hue * 60
        if(Hue < 0):
            Hue = Hue + 360
        
        outputHSB = [Hue, Saturation, Brightness]
        return outputHSB

    #-----------convertToRGB-----------
    #Taking in an array of Hue, Saturation, and Brightness values,
    #Calculate the conversion to an RGB colour object.
    #
    #Right now, this function is always off by 1. I know it's the way in which
    #I've casted the floats to integer values, but it's still off.
    def convertToRGB(hsbArray):
        red = 0
        green = 0
        blue = 0

        if(hsbArray[1] == 0):
            red = hsbArray[2]
            green = hsbArray[2]
            blue = hsbArray[2]

        hsbArray[0] = hsbArray[0]/360
        hsbArray[1] = hsbArray[1]/100
        hsbArray[2] = hsbArray[2]/100
        
        h = int((hsbArray[0] - math.floor(hsbArray[0]))*6.0)
        f = ((hsbArray[0] - math.floor(hsbArray[0]))*6.0) - float(math.floor(h))
        p = hsbArray[2] * (1.0 - hsbArray[1])
        q = hsbArray[2] * (1.0 - hsbArray[1] * f)
        t = hsbArray[2] * (1.0 - (hsbArray[1] * (1.0 - f)))

        if(h == 0):
            red = int(hsbArray[2] * 255 + 1)
            green = int(t * 255 + 1)
            blue = int(p * 255 + 1)
        elif(h == 1):
            red = int(q * 255 + 1)
            green = int(hsbArray[2] * 255 + 1)
            blue = int(p * 255 + 1)
        elif(h == 2):
            red = int(p * 255 + 1)
            green = int(hsbArray[2] * 255 + 1)
            blue = int(t * 255 + 1)
        elif(h == 3):
            red = int(p * 255 + 1)
            green = int(q * 255 + 1)
            blue = int(hsbArray[2] * 255 + 1)
        elif(h == 4):
            red = int(t * 255 + 1)
            green = int(p * 255 + 1)
            blue = int(hsbArray[2] * 255 + 1)
        elif(h == 5):
            red = int(hsbArray[2] * 255 + 1)
            green = int(p * 255 + 1)
            blue = int(q * 255 + 1)


        outputColour = colour(red, green, blue)
        return outputColour

    #----------blend----------
    #Okay so this function will blend any number of RGB values
    #It takes in any number of strings, determines how to make them into RGB colours,
    #and then processes them in separate channel arrays
    #Then it averages out the value of each channel,
    #And then returns a new Colour object containing these averaged channel values.
    #
    #This style of blending is useful in digital art, as a real-world analogue does not exist.
    def blend(*args):
        #These arrays will capture the individual channel values from the input Colour objects
        redChannels = []
        greenChannels = []
        blueChannels = []

        #Setting up the mean values
        redMean = 0
        greenMean = 0
        blueMean = 0

        #What's critically important here is to find out if our input is valid colour codes or not
        #And then, taking those as new Colour objects, parsing their RGB values into our separate
        #arrays.
        tempColour = colour()
        for i in args:
            tempColour = colour.determineInput(i)
            if(tempColour != False):
                redChannels.append(tempColour.red)
                greenChannels.append(tempColour.green)
                blueChannels.append(tempColour.blue)
        
        #If the number of values in any channel array is less than 1, something has failed
        #while we were processing the inputs. TODO: Return something more formal than a string.
        if((len(redChannels) <= 1) or (len(greenChannels) <=1) or (len(blueChannels) <= 1)):
            return "Lol no"
        else:
            for r in redChannels:
                redMean += r
            for g in greenChannels:
                greenMean += g
            for b in blueChannels:
                blueMean += b
            
            #Math to determine the averages for each colour value
            redMean = int(redMean/len(redChannels))
            greenMean = int(greenMean/len(greenChannels))
            blueMean = int(blueMean/len(blueChannels))

            #Return a new Colour object.
            outputColour = colour(redMean, greenMean, blueMean)
            return outputColour
                
    #----------add----------
    #This function additively blends any number of colour values, determined by input.
    #This style of blending is analagous to light. Light always "adds up" eventually to white.
    #The function returns a colour object
    def add(*args):
    		operatedColours = []
    		tempColour = colour()

            #Again, we're going through the inputs and seeing if they map out to valid representations
            #of colour. Then we add their objects to our array.
    		for i in args:
    			tempColour = colour.determineInput(i)
    			if(tempColour != False):
    				operatedColours.append(tempColour)
    		
            #If this function has failed to process the inputs as valid colours, than the input is invalid.
            #The function returns a string for now, but TODO: I'll change it to something else later.
    		if(len(operatedColours) <= 1):
    			return "Lol no"
    		else:
    			red = 0
    			blue = 0
    			green = 0
    			for j in operatedColours:
    				red += j.red
    				green += j.green
    				blue += j.blue
    			
                #Here's the only complication of this function.
                #Our RGB colour values max out at 255 because it's an 8-bit value.
                #If the channels, after adding, go above 255, they must be set back to 255.
    			if(red > 255):
    				red = 255
    			if(green > 255):
    				green = 255
    			if(blue > 255):
    				blue = 255
    				
    			outputColour = colour(red, green, blue)    			
    			return outputColour
        		
    #----------subtract----------
    #Like the add function, this will take in inputs and process them as colours.
    #Right now this function replicates the operations of Mathematica's colour subtraction.
    #Which is to say, any value that is in excess of 255 for a channel is processed as a separate
    #value. This is a really lossy and hacky implementation of subtraction blending, which is most
    #analagous to paint mixing in the real world. The problem is a lot more complicated, but for a first
    #version this will do.
    def subtract(*args):
        operatedColours = []
        tempColour = colour()

        #Again, we're going through the inputs and seeing if they map out to valid representations
        #of colour. Then we add their objects to our array.
        for i in args:
        	tempColour = colour.determineInput(i)
        	if(tempColour != False):
        		operatedColours.append(tempColour)
        
        #If this function has failed to process the inputs as valid colours, than the input is invalid.
        #The function returns a string for now, but TODO: I'll change it to something else later.
        if(len(operatedColours) <= 1):
        	return "Lol no"
        else:
        	red = operatedColours[0].red
        	green = operatedColours[0].green
        	blue = operatedColours[0].blue
        	j = 1
        	
        	while(j < len(operatedColours)):
        		red += operatedColours[j].red
        		green += operatedColours[j].green
        		blue += operatedColours[j].blue
        		
        		j += 1
        	
        	if(red > 255):
        		red = red % 255
            else:
                red = 0
        	if(green > 255):
        		green = green % 255
            else:
                green = 0
        	if(blue > 255):
        		blue = blue % 255
            else:
                blue = 0
        	
        	outputColour = colour(red, green, blue)        	
        	return outputColour

    #----------fuse----------
    #I didn't have a name for this operation as I already used "blend", so this will have to do.
    #fuse takes in strings, processes them as colour objects, then converts those objects to 
    #an array of their corresponding HSB values (Hue, Saturation, and Brightness), averages out
    #the HSB values, then converts back to an RGB Colour object.
    def fuse(*args):

        #We need to ultimately split all of our colours into their component HSB values, and then
        #iteratively add those values to a corresponding array.
        operatedHSB = []
        collectiveH = []
        collectiveS = []
        collectiveB = []
        count = 0

        tempColour = colour()
        for i in args:
            tempColour = colour.determineInput(i)
            if(tempColour != False):
                operatedHSB = (tempColour.convertToHSB())
                collectiveH.append(operatedHSB[0])
                collectiveS.append(operatedHSB[1])
                collectiveB.append(operatedHSB[2])
                count += 1
        
        #If this function has failed to process the inputs as valid colours, than the input is invalid.
        #The function returns a string for now, but TODO: I'll change it to something else later.
        if(count == 0):
            return "LOL nope"
        
        hueSum = 0
        satSum = 0
        briSum = 0
        neuH = 0
        neuS = 0
        neuB = 0

        #First find the new hue value
        #Finding a good hue is difficult here because, for example, simply averaging out the hue of red
        #and blue would mathematically give a green colour, even though in the real world we would expect
        #a purple colour.
        #The workaround I've discovered is that if you take the maximum and minimum Hue values from our inputs,
        #and calculate their distances first from within that first rotation in the Hue cylinder, and then the distance
        #if the values are allowed to wrap around, the smaller distance represents the more realistic hue calculation.
        if(abs(max(collectiveH) - min(collectiveH)) < abs(max(collectiveH) - (360 + min(collectiveH)))):
            for i in collectiveH:
                hueSum += i
        else:
            for i in collectiveH:
                hueSum += i
            hueSum += 360
        
        #Then average out the hue
        neuH = hueSum/len(collectiveH)

        for j in collectiveS:
            satSum += j
        for k in collectiveB:
            briSum += k
        
        #Saturation and brightness is easy because these are independent of colour.
        neuS = satSum/len(collectiveS)
        neuB = briSum/len(collectiveB)

        #Build a new array of our emergent HSB values.
        averageHSB = [neuH, neuS, neuB]
        #Convert that HSB value into a RGB Colour object.
        outputColour = colour.convertToRGB(averageHSB)

        return outputColour

    #----------toString----------
    #Taking a colour object as input, output its RGB values as their component numbers,
    #And additionally output a hexcode for the colour object
    def toString(self):
        firstLine = "RGB Values: "+str(self.red)+", "+str(self.green)+", "+str(self.blue)+"\n"
        secondLine = "Hex Value: #"+hex(self.red)[2:]+hex(self.green)[2:]+hex(self.blue)[2:]
        return firstLine + secondLine

    #----------display----------
    #Taking a colour object as input, make a cute little paint card like at a hardware store
    #using Turtle.
    def display(self):
        hexCode = "#"+hex(self.red)[2:]+hex(self.green)[2:]+hex(self.blue)[2:]
        bertWindow = turtle.Screen()
        bertWindow.clear()
        bertWindow.setup(260, 300, 0, 0)
        bert = turtle.Turtle()
        bert.penup()
        bert.speed(0)
        bert.setpos(-90, 120)
        bert.hideturtle()
        
        bert.color('black', hexCode)
        bert.pendown()
        bert.forward(180)
        bert.right(90)
        bert.forward(240)
        bert.right(90)
        bert.forward(180)
        bert.right(90)
        bert.forward(240)
        bert.penup()
        bert.right(90)
        bert.forward(15)
        bert.right(90)
        bert.forward(15)

        bert.pendown()
        bert.begin_fill()
        bert.forward(150)
        bert.left(90)
        bert.forward(150)
        bert.left(90)
        bert.forward(150)
        bert.left(90)
        bert.forward(150)
        bert.end_fill()
        bert.penup()

        bert.left(90)
        bert.forward(200)
        bert.pendown()
        bert.write(self.toString(), False, "left", ("Arial", 10, "normal"))
