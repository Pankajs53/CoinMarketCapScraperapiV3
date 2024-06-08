import pandas as pd

def create_excel_file(scraped_data):
    try:
        # Extract relevant information
        coin_data = scraped_data['output']
        coin_name = scraped_data['coin']
        price = coin_data['price']
        price_change = coin_data['price_change']
        market_cap = coin_data.get('market_cap', None)
        volume = coin_data.get('volume', None)
        volume_change = coin_data.get('volume_change', None)
        circulating_supply = coin_data.get('circulating_supply', None)
        total_supply = coin_data.get('total_supply', None)
        diluted_market_cap = coin_data.get('diluted_market_cap', None)
        # contracts = coin_data.get('contracts', [])
        # official_links = coin_data.get('official_links', [])
        # socials = coin_data.get('socials', {})

        # Create a DataFrame from the extracted data
        data = {
            'Coin Name': [coin_name],
            'Price': [price],
            'Price Change': [price_change],
            'Market Cap': [market_cap],
            'Volume': [volume],
            'Volume Change': [volume_change],
            'Circulating Supply': [circulating_supply],
            'Total Supply': [total_supply],
            'Diluted Market Cap': [diluted_market_cap]
        }
        df = pd.DataFrame(data)

        # Read existing Excel file (if exists)
        excel_file_path = "scraped_data.xlsx"
        try:
            existing_df = pd.read_excel(excel_file_path)
            # Append new data to existing DataFrame
            df = pd.concat([existing_df, df], ignore_index=True)
            print("Added new entry in excel file")
        except FileNotFoundError:
            pass  # Continue if the file doesn't exist

        # Write data to Excel
        df.to_excel(excel_file_path, index=False)
        print("Data saved to Excel file successfully")
    except KeyError as e:
        print(f"Error accessing dictionary key: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
