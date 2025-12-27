import requests

response = requests.get("https://api.exchangeratesapi.io/v1/latest?access_key=1fe97a02457d80b80af9a893750e3cdc")

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print("base: " + base)
    print("date: " + date)

    # print(rates)

    for key in rates:
        print(key + ": ", rates[key])