from openai import OpenAI
import time
import os
import urllib.request as req
import csv
from PIL import Image
from datetime import datetime

class ProductImageGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.list_product = ["Laptop", "Desktop", "Smartphone"]

    def generate_images(self, product, prompt, output_dir, num_images=15):
        output_dir = output_dir.replace(" ", "_")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        for i in range(num_images):
            url_image = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            ).data[0].url

            image_name = f"{product}_{current_time}_{i}.png"
            image_name = image_name.replace(" ", "_")
            image_path = os.path.join(output_dir, image_name)

            req.urlretrieve(url_image, filename=image_path)
            time.sleep(3)

            self.resize_image(image_path)

        print(f"Added {num_images} images to folder {output_dir}")

    def resize_image(self, image_path, new_size=(512, 512)):
        img = Image.open(image_path)
        img_resized = img.resize(new_size, Image.ANTIALIAS)
        img_resized.save(image_path)

def main():
    api_key = "" # OpenAI API key
    product_list_file = "list_product.csv"
    output_base_dir = "./"

    generator = ProductImageGenerator(api_key)

    with open(product_list_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=':')
        for row in reader:
            product = row["product"]
            prompt = row["prompt"]
            output_dir = os.path.join(output_base_dir, product)

            generator.generate_images(product, prompt, output_dir)

if __name__ == "__main__":
    main()
