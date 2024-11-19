import requests

# Define the ICP API endpoint (replace with your actual ICP API endpoint)
ICP_API_URL = "https://your-icp-api-endpoint"

# Function to get UTXOs (Unspent Transaction Outputs) for a Bitcoin address
def get_utxos(address):
    response = requests.get(f"{ICP_API_URL}/bitcoin_get_utxos", params={"address": address})
    return response.json()

# Function to get the balance of a Bitcoin address
def get_balance(address):
    response = requests.get(f"{ICP_API_URL}/bitcoin_get_balance", params={"address": address})
    return response.json()

# Function to get current fee percentiles
def get_fee_percentiles():
    response = requests.get(f"{ICP_API_URL}/bitcoin_get_current_fee_percentiles")
    return response.json()

# Function to get block headers for transaction verification
def get_block_headers(start_height, end_height=None):
    params = {"start_height": start_height}
    if end_height:
        params["end_height"] = end_height
    response = requests.get(f"{ICP_API_URL}/bitcoin_get_block_headers", params=params)
    return response.json()

# Example: Use the functions to interact with the API
if __name__ == "__main__":
    address = "your-bitcoin-address"  # Replace with your actual Bitcoin address
    
    # Fetch UTXOs and Balance
    utxos = get_utxos(address)
    balance = get_balance(address)
    
    # Fetch current fee percentiles
    fee_percentiles = get_fee_percentiles()

    # Print out the results
    print("UTXOs:", utxos)
    print("Balance:", balance)
    print("Fee Percentiles:", fee_percentiles)

    # Example: Get block headers for a range of heights
    start_height = 1000000
    block_headers = get_block_headers(start_height)
    print("Block Headers:", block_headers)
