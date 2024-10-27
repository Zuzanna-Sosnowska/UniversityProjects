import tkinter as tk
from tkinter import *
import tkinter.messagebox


root = tk.Tk()
root.title("Kalkulator przeliczający kursy walut")

Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Kalkulator przeliczający kursy walut ',bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("waluta")
variable2.set("waluta")


# Function To For Real Time Currency Conversion
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error !!", "Nie podano kwoty.\n Podaj prawidłowo kwotę.")

    elif from_currency == "waluta" or to_currency == "waluta":
        tkinter.messagebox.showinfo("Error !!", "Nie wybrano waluty.\n Wybierz walutę z listy.")

    else:
        try:
            new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.insert(0, str(new_amount))

            savableRates: str = ""
            for cr in CurrencyCode_list:
                savableRates += f'{cr}:{c.get_rate("USD", cr)};'

            safeCurrentRates(safeRatesFile, savableRates)

        except:
            ratedict = getSavedRates(safeRatesFile)
            newAmount = getAmount(ratedict, from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(newAmount))
            Amount2_field.insert(0, str(new_amount))


def safeCurrentRates(filename: str, savableRates: str):
    text_file = open(filename, "w")
    text_file.write(savableRates)
    text_file.close()


def getSavedRates(filename: str):
    text_file = open(filename, "r")
    offline_rates = text_file.read()
    text_file.close()

    global rateDict
    rateDict = {}
    rateMap = offline_rates.split(";")
    rateMap.pop()
    for data in rateMap:
        s = data.split(":")
        rateDict[s[0]] = float(s[1])
    return rateDict


def getAmount(rate_dict: dict, from_currency: str, to_currency: str, amount: float):
    from_curr_in_USD = amount * rate_dict[from_currency]
    finalAmount = from_curr_in_USD/rate_dict[to_currency]
    return finalAmount


# clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


safeRatesFile = 'rates.txt'
CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "PLN", "CZK", ]

root.configure(background='#e6e5e5')
root.geometry("700x400")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Kwota : ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Przelicznik z : ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Przelicznik na : ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Wynik : ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Oblicz ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Wyczyść ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)

root.mainloop()