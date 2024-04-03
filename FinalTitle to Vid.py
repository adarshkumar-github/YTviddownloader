from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome service and Chrome WebDriver using ChromeDriverManager
chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

# Construct the YouTube search query URL
video_title = input("Enter the video title: ")
search_query = '+'.join(video_title.split())
url = f"https://www.youtube.com/results?search_query={search_query}"

# Navigate to the search query URL
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Execute JavaScript to get the link of the first video
first_video_link = driver.execute_script('''
    return document.querySelector('#contents ytd-video-renderer a#video-title').href;
''')

# Print the link of the first video
# print("Link to the first video:", first_video_link)

# Close the browser
driver.quit()


#Download Part

from pytube import YouTube

# link = input("Enter the link of the video which you want to download:")
link=first_video_link
url = YouTube(link)
save_location = r"C:\Users\adars\OneDrive\Documents\Experiment"

# showing video details
print("Video title: ", url.title)
print("Number of views on the video: ",url.views)
print("Length of the video ", url.length, "seconds")
print("Description:", url.description)

# process
try:
    url = YouTube(link)
    video = url.streams.get_highest_resolution()
    print("Downloading.............")
    video.download(save_location)
    print("Video downloaded successfully!!!")

except:
    print("Something went wrong!!")