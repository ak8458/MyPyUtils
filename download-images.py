import csv
import os
import requests
import urllib.parse

# Specify the path to the CSV file
csv_path = '/Users/akshaypatil/Documents/work/projects/RH/temp/all-rte-images-en-us.csv'
#csv_path = '/Users/akshaypatil/Documents/work/projects/RH/temp/all-blog-feature-images-en-us.csv'

# Specify the path to the folder where the images will be saved
save_folder = '/Users/akshaypatil/Documents/work/projects/RH/temp/test-download'
#save_folder = '/Users/akshaypatil/Documents/work/projects/RH/temp/all-blog-feature-images-en-us'

# Specify the path to the log file
log_file = '/Users/akshaypatil/Documents/work/projects/RH/temp/file.log'

# Open the CSV file and read the contents
with open(csv_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    # Skip the header row (if there is one)
    next(reader)
    # Iterate through each row in the CSV file
    for row in reader:
        # Get the URL of the image from the 4th column
        image_url = row[0]
        #domain = "https://www.roberthalf.com"
        # Get the name of the image (assumes it's the last part of the URL)
        image_name = os.path.basename( image_url)
        print(image_url)
        # decode image_name and modify
        decoded_image_url = urllib.parse.unquote(image_name)
        #image_url = domain + image_url;
        # Download the image
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save the image to the specified folder with the same name
            with open(os.path.join(save_folder, decoded_image_url), 'wb') as f:
                f.write(response.content)
        else:
            # Log the row to the log file
            with open(log_file, 'a') as f:
                f.write('Error downloading image from row {}: {}\n'.format(reader.line_num, image_url))

