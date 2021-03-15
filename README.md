# captioningVideos
This repository contains a program that makes captions from a text file for a video based on timestamps from keypresses on the keyboard.

<h1>Installing:</h1>
<p>This will use python. Click <a href = 'https://www.python.org/downloads/'>this link</a> and download the most recent version of python. After it downloads install the program and continue on. You do not need to open python.</p>

<p>Go to the top of the page and click the green code button then press download zip. After it downloads open the folder and extract the files to your computer by clicking on the downloaded folder then on the top bar of File Explorer there is a "compressed folder tools". Click on that option, there should be an option to extract all.<p>

<h1>Usage</h1>
<h2>Preparing for the captioning:</h2>
<p>For an example of these directions see the file named "example.txt". This is the file the the program will use to make the captions. The file will need to be saved in the same folder ad runMe.py. This will need to have all of the text you want displayed for the captioning. The way that you make this file is that every time a person changes speaking you press enter. Every time you press enter will be a different caption set. For example the first line will be one caption and the second line will be another. Don't worry if your line is really long, the program will automatically space out the captions to not be too long for the screen.</p>

<h2>Running the program</h2>
<p>In the folder where you extracted the files and after installing python double click on the runMe.py file then it will open up and give you instructions to run the program. If you mess up at any time you can press 'r' and it will go back to the start and you can try to caption the video again. You can also enter 'a' to access the advanced menu from the opening menu.</p>

<h1>Extra features and information</h1>

<p>This is all you need if you only want to generate the captions. You can upload the .srt file to facebook if you want. To burn them into your video which is recommended for social media you will also need to download and install <a href = 'https://handbrake.fr/downloads.php'>handbrake</a> which can add your captions without losing too much video quality. Every time you edit your video it wil lose some quality but for me the quality change was not noticeable and it does a very good job at burning in the captions.</p>

<h1>To do:</h1>
<ul>
  <li>Make the video play in the python window using opencv. You can also capture keypresses in this way so you would not need the pynput library any more.
  <li>Make the program burn in the captions if you want them too. Eliminate the need for handbrake
</ul>
