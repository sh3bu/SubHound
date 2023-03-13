import requests

target_url = "https://example.com"

wordlist_file = input("Enter the path of the wordlist file: ")
with open(wordlist_file) as f:
    subdomains_list = [line.strip() for line in f]

for subdomain in subdomains_list:
    url = f"http://{subdomain}.{target_url}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
