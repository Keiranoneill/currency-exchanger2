import tkinter as tk

currency_exchange = {
    'US dollar': 0.81,
    'Canadian dollar': 0.60,
    'Danish Krone': 0.12,
    'euro': 0.86,
    'Japanese Yen ': 0.57
}


def convert_currency():
    amount = float(amount_entry.get())
    currency = currency_var.get()

    if currency in currency_exchange:
        conversion_rate = currency_exchange[currency]
        converted_amount = amount * conversion_rate
        result_label.config(text=f"{amount} {currency.upper()} is equal to {converted_amount:.2f} GBP.")
    else:
        result_label.config(text="Invalid currency.")


window = tk.Tk()
window.title("Currency Converter")


name_label = tk.Label(window, text="Welcome ")
name_label.pack()


currency_label = tk.Label(window, text="What currency would you like to convert?")
currency_label.pack()

currency_var = tk.StringVar(window)
currency_var.set("US dollar")

currency_option = tk.OptionMenu(window, currency_var, *currency_exchange.keys())
currency_option.pack()

amount_label = tk.Label(window, text="Enter the amount to convert:")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
