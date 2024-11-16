import csv
import os
from dotenv import load_dotenv
import openai

# Local functions 
from datascraper import scrape

load_dotenv()

# Note: you are not suppose to include the 'API_KEY7=' part if directly using without .env
openai.api_key = os.getenv("API_KEY7")
chat_history_file = r"chat_history.csv"

messages = [{"role": "system", "content": "You are an AI specialized in financial analysis"}]

def get_response(prompt):

    # Note: role has to be reset here to user to differentiate user queries from model's response when passing as argument
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        # Note: messages list of dict param is used to structure conversation through different roles 
        # Controls behavior, i.e the system role offers concise responses
        messages = messages
    )

    reply_content = response["choices"][0]["message"]["content"]
    # Note: need to append with role assistant here to update the model with its own reponse for dynamic chat history
    messages.append({"role": "assistant", "content": reply_content})

    # Response refers to the output which is a dict
    return reply_content

def print_chat_history():
    print("\n### CONVERSATION HISTORY ###\n")
    for message in messages: 
        role = message["role"].upper()
        # Note: prints each message from the message history with respect to the role
        print(f"{role}: {message["content"]}")
    print("\n### END OF CONVERSATION HISTORY ###\n")

def save_to_csv(filename, mode, role, content):
    with open(filename, mode = mode, newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([role, content])

if __name__ == "__main__":
    print("\n### Starting chat ###\n")

    # Need to write the CSV headers
    # Returns file object
    save_to_csv(chat_history_file, "w", "Role", "Content")

    while True:
        query = input("\nEnter your query: ")
        if query == "exit":
            break
        elif query == "print history":
            print_chat_history()
        elif query.startswith("scrape "):
            stock = query.split()[1]
            link = "https://finance.yahoo.com/quote/" + stock 
            print("link", link)
            data = scrape(link)
            print(data)
            if data:
                response = get_response(f"For prompts relating to financial analysis, analyze and use the scraped data provided:\n{data}")
                save_to_csv(chat_history_file, "a", "USER", f"Analyze: {link}")
                save_to_csv(chat_history_file, "a", "ASSISTANT", response)
                print(f"\nAI Analysis:\n{response}")
        else:
            response = get_response(query)
            save_to_csv(chat_history_file, "a", "USER", query)
            save_to_csv(chat_history_file, "a", "ASSISTANT", response)
            print(f"\nAI:\n{response}")

        
