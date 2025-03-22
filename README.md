#############################################################################

Pick-a-Fit App

## Authors:
- Portia Li & Mariana Ma
- Northwestern University, CS 310
 
The Pick-a-Fit application is an online outfit recommendation system. 
The application interacts with AWS Lambda functions through API Gateway as well
as WeatherAPI to provide users with personalized outfit recommendations based on 
images of their clothes and current weather conditions. Users upload their clothing images
and related metadata, which is stored in S3 and RDS. Then, users can ask for a
personalized outfit based on the weather, as well as get weekly clothing item
recommendations based on the weekly forecast.

#############################################################################

OVERVIEW OF THE APPLICATION

#############################################################################

MAIN CLIENT-SIDE FUNCTIONS:
1. upload(): upload an image of a clothing item and provide some basic information. 
2. outfit(): get an outfit recommendation based on the current weather conditions. The
outfit images will be downloaded from S3 and returned to the user as a folder of images.
3. forecast(): get the weekly forecast (average weather, precipitation, etc.) and a weekly
clothing recommendation based on the week's predicted weather.

#############################################################################

LAMBDA FUNCTIONS:
1. /item/userid: takes the image posted by the client. First, we run Rekognition on the image
to check if it is in fact a clothing item. If it's not, return an error to the client. Otherwise,
proceed and upload clothing item's information to RDS and the image to S3.
2. /outfit/userid: interacts with WeatherAPI to get the current weather. Based on that, it selects
suitable clothing items from the client's digital wardrobe and returns an outfit consisting of a 
top, bottoms, and shoes. Returns the outfit as a folder with the clothing images inside.
3. /forecast/userid: interacts with WeatherAPI to get the full weekly forecast. Based on this,
recommend specific clothing items to the user that align with the weather predictions and also 
advise the client on what items to add to their wardrobe.

#############################################################################

NON-TRIVIAL OPERATIONS:
1. Rekognition for clothing image detection and validation
2. Interacting with WeatherAPI to build a custom outfit
3. Interacting with WeatherAPI to create a weekly forecast and use
the collected stats to make clothing item recommendations.

#############################################################################
SETUP: The only client-side setup required is docker.
INSTRUCTIONS:

Linux users (and Windows users running WSL), open a terminal window,
navigate to the folder containing this 'readme.txt' file, and run the 
following command from a terminal window:

  ./_setup-linux.bash

Then build the Docker image by executing this command:

  ./docker/build

Finally, to run the image do the following:

  ./docker/run

If all is well you should see the "docker>" prompt. You only need to do
the setup and build commands once. 

#############################################################################

Mac users: open a terminal window and navigate to the folder containing
this 'readme.txt' file. A nice trick is to open Finder, "View" menu, 
"Show Path Bar", right-click on the folder name, "Open in Terminal". Then
run these commands:

  chmod 755 *.bash

  ./_setup-mac.bash

Now build the Docker image by executing this command:

  ./docker/build

Finally, to run the image do the following:

  ./docker/run

If all is well you should see the "docker>" prompt. You only need to do
the setup and build commands once. 

#############################################################################

Windows users: open a Powershell window and navigate to the folder 
containing this 'readme.txt' file. A nice trick is to view the folder
and right-click on the background and select "Open in Terminal" (if 
Powershell doesn't open, you can change the default profile to Powershell,
save, and try again). Then run this command:

  .\_setup-windows.ps1

If you get an error message along the lines of "script is not digitally 
signed. You cannot run this script on the current system", then run 
as follows:

  powershell.exe -executionpolicy bypass .\_setup-windows.ps1

Now build the Docker image by executing this command:

  ./docker/build

If you get an error message along the lines of "script blocked by system's
execution policy", then do the following and try again:

  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Finally, to run the image do the following:

  ./docker/run

If all is well you should see the "docker>" prompt. You only need to do
the setup and build commands once. 

#############################################################################


#############################################################################
#############################################################################
