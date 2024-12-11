import requests

def chat_with_baseer():
    url = "https://basser-api.vercel.app/chat"
    print("Baseer Chat Terminal (type 'exit' to quit)")
    print("-----------------------------------------")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        try:
            response = requests.post(
                url,
                json={"message": user_input}
            )
            response.raise_for_status()
            data = response.json()
            print("\nBaseer:", data['response'])
            
        except requests.exceptions.RequestException as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    chat_with_baseer()
