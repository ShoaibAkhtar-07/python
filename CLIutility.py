import argparse
import requests

def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Image downloaded and saved as '{filename}'")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
        
parser = argparse.ArgumentParser()

parser.add_argument("url",help="give the url of the image")
parser.add_argument("output",help="give the name of the image")

args = parser.parse_args()

print(args.url)
print(args.output)
download_image(args.url,args.output)
