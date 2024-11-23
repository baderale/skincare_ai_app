from pyairtable import Api
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("configs/.env")
AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = "Products"  # Replace with the exact name of your table

def get_products():
    try:
        # Initialize the Airtable API
        api = Api(AIRTABLE_PAT)
        table = api.table(BASE_ID, TABLE_NAME)

        # Fetch all records from the table
        records = table.all()
        products = [record["fields"] for record in records]
        return products
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []

if __name__ == "__main__":
    products = get_products()
    if products:
        print("Products fetched successfully:")
        for product in products:
            print(f"Name: {product.get('Product Name', 'N/A')}")
            print(f"Price: ${product.get('Price', 'N/A')}")
            print(f"Category: {product.get('Category', 'N/A')}")
            print(f"Affiliate Link: {product.get('Affiliate Link', 'N/A')}")
            print()
    else:
        print("No products found or an error occurred.")
