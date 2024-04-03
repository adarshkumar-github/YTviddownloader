#(Run this code to download video from the title)
#Fetching link part
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

video_title = input("Enter the video title: ")
search_query = '+'.join(video_title.split())
url = f"https://www.youtube.com/results?search_query={search_query}"

driver.get(url)

driver.implicitly_wait(10)

first_video_link = driver.execute_script('''
    return document.querySelector('#contents ytd-video-renderer a#video-title').href;
''')

driver.quit()


#Download Part

from pytube import YouTube
link=first_video_link
url = YouTube(link)

#Please give the location at which you want your file to be saved instead of this location.

save_location = r"C:\Users\adars\OneDrive\Documents\Experiment"

# showing video details
print("Video title: ", url.title)
print("Number of views on the video: ",url.views)
print("Length of the video ", url.length, "seconds")
print("Description:", url.description)

try:
    url = YouTube(link)
    video = url.streams.get_highest_resolution()
    print("Downloading.............")
    video.download(save_location)
    print("Video downloaded successfully!!!")

except:
    print("Something went wrong!!")