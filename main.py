import tkinter as tk
import requests
import threading

url = 'https://api.quotable.io/random'
quotes = []
quote_number = 0

window = tk.Tk()
window.geometry("900x260")
window.title("Quote generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="grey")


def preload_quotes():
    global quotes

    print("***Loading***")

    for x in range(10):
        r = requests.get(url)
        random_quote = r.json()
        quote = random_quote['content']
        author = random_quote['author']
        content = quote + "\n\n" + "- " + author
        print(quote)

        quotes.append(content)

    print("***Finished***")


preload_quotes()


def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1

    if quotes[quote_number] == quotes[-3]:
        thread = threading.Thread(target=preload_quotes)
        thread.start()


#   UI

quote_label = tk.Label(window,
                       text="Click on the button to generate a random number!",
                       height=6,
                       pady=10,
                       wraplength=800,
                       font=("Helvetica", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Generate",
                   command=get_random_quote,
                   bg="#0052cc",
                   fg="#FFFFFF",
                   activebackground="grey",
                   font=("Helvetica", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)

#   Program execution

if __name__ == "__main__":
    window.mainloop()