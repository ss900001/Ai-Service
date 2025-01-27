import requests

# Replace with your API credentials
API_ENDPOINT = "https://api.tiktok.com/real-report-endpoint"
API_TOKEN = "your_api_token"

def report_account(username, reason="Spam"):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Your-App-Name/Version"
    }

    payload = {
        "username": username,
        "reason": reason
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Report successfully submitted for @{username}.")
        else:
            print(f"Failed to report @{username}. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the username to report: ").strip()
    reason = input("Enter the reason for reporting (e.g., Spam, Fake account): ").strip()
    report_account(username, reason)
s

# Example usage
if __name__ == "__main__":
    target_username = input("Enter the username to report: ")
    for _ in range(100):  # Send 100 reports
        send_report(target_username)

