# Product Image Generator

This project generates product images using OpenAI's DALL-E model. It supports a variety of products and allows customization through prompts.

## Installation

Clone the repository and install the required packages:

```bash
git clone <repository_link>
cd product-image-generator
pip install -r requirements.txt
```

## Usage

1. Obtain an API key from OpenAI and set it in the script.
2. Prepare a `list_product.csv` file with the products and prompts.
3. Run the script:

```bash
python product_image_generator.py
```

## Example of `list_product.csv`

```csv
product:prompt
Laptop:Laptop image prompt
Smartphone:Smartphone image prompt
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.
