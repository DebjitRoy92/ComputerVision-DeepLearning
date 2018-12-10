from google_images_download import google_images_download   #importing the library
import sys
response = google_images_download.googleimagesdownload()   #class instantiation

title = sys.argv[1]
arguments = {"keywords":title,"limit":300,"print_urls":True,"chromedriver":"C:/Users/debji/ml_src/cricket/dataset/chromedriver.exe"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)
