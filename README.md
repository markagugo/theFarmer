# THE_FARMER
<p align="center">
  <img width="600" height="400" src="https://user-images.githubusercontent.com/73078814/169968797-8e91e83d-0322-44df-b5e9-23e17cc2c55c.png">
</p>


# Project Description
<h4>
 <p><b>THE_FARMER</b> is a sophisticated tool developed for web crawling and data extraction purposes. As a programmer, you can leverage this tool to automate the process of searching for specific data, such as URLs, on the internet. Let's consider a practical scenario where you want to download a movie, but manually scouring the web for the direct download link in formats like .mp4 or .mkv seems laborious. With <b>THE_FARMER</b>, all you need to do is provide a search keyword and try to be more specfic(e.g., "Vince Carter Legacy 2021 movie download"), specify the type of data you are interested in crawling for (e.g., .mp4, .mkv, .pdf, @gmail.com, /mp4, .png, etc.), provide the path to your Chrome Driver executable file (e.g., "C:\WebDriver\chromedriver.exe"), and specify the file where the discovered data or URLs should be stored (e.g., "urls.txt").
</p>
  <br />
  <p><b>Please note that executing this code may take a considerable amount of time to complete. As the program runs, the discovered data will be promptly updated and written to the designated file. If necessary, you can interrupt the program at any time by pressing <b>CTRL + C</b>. It's worth mentioning that this program is compatible with both Windows and Linux operating systems.
</p>
  <br />
    <i>
      It is important to maximize the screen size of your Chrome browser once the program and the browser open to ensure optimal performance and usability.
    </i>
  <br />
  <h4>
    Please bear in mind that <b>THE_FARMER</b> is a dynamic tool, and additional features and updates will be introduced in future versions to enhance its capabilities.
  </h4>  
</h4>

# Installation
```bash
git clone https://github.com/markagugo/theFarmer.git
```


# Usage
```bash
//navigate to the the_farmer directory you cloned
cd the_farmer

//install the neceassary requirements
pip install requirements.txt

//for program help
python theFarmer.py --h

#run the program and parse neceassary parameters
python .\theFarmer.py -k 'vince carter legacy movie download' -u '.mp4, .mkv, .jpg', -e 'C:\WebDriver\chromedriver.exe' -o 'vid_links.txt'
```
