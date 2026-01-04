import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock info")

topWidget = tk.Frame(window)
label = tk.Label(topWidget, text="Write stock ticker:")
label.pack(side=tk.LEFT)
entry = tk.Entry(topWidget)
entry.pack(side=tk.RIGHT)
topWidget.pack()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=10, width=70, padx=5, pady=5,
            font=("Helvetica", 12))

scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
textBox.pack(expand = True, fill=tk.BOTH)
scrollbar.config(command = textBox.yview)
textBox.config(yscrollcommand = scrollbar.set)

def downloadData(e):
    stock = str(e.widget.get())

    if not stock:
        print("No stock ticker")
        return

    stock = stock.upper().strip()
    print("download stock data: ", stock)

    stockData = yf.Ticker(stock)
    print(stockData.info)

entry.bind("<Return>", downloadData)

window.mainloop()