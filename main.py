from src.StockExchangeChatBot import StockExchangeChatbot
import json


def main():

    # Used for error handling - in this case mostly in case of missing file or for the json integrity
    try:
        with open('info/Chatbot - stock data.json.', "r") as file:
            data = json.load(file)
            # Checks if the json file is empty
            if not data:
                print('Json file is empty')
                return 0
        app = StockExchangeChatbot(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()
