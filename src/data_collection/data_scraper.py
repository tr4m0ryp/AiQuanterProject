import requests

def collect_data(url):
    """Function to collect data from a URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # assuming the API returns JSON data
    else:
        return None

if __name__ == "__main__":
    url = "https://api.example.com/data"  # replace with real URL
    data = collect_data(url)
    if data:
        print("Data collected successfully:", data)
    else:
        print("Failed to collect data.")
