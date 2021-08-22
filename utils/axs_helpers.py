import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI

def get_axsprice(currency): # function to retrieve specifically AXS price rate
    cg = CoinGeckoAPI()
    price = cg.get_price(ids='axie-infinity', vs_currencies=currency)
    return price

def get_minutely_market_history(currency):
    cg = CoinGeckoAPI()

    market_history = cg.get_coin_market_chart_by_id(id="axie-infinity", vs_currency=currency, days=1)

    prices = market_history['prices']

    temp = []

    for volume, price in prices:
        temp.append(price)
    
    return temp

def graph_day_market_history(currency): # graphs minutely data of axs 
    temp = get_minutely_market_history(currency)
    
    x = list(range(len(temp)))

    fig, ax = plt.subplots()
    ax.plot(x, temp, label=f"AXS per Minute ({currency.upper()})")
    ax.xaxis.set_ticklabels([])
    plt.legend()
    plt.xlabel("Minute")
    plt.ylabel(f"AXS Price in {currency.upper()}")
    plt.title("AXS Price Minutely Data")
    plt.text(x[len(x)-1], temp[len(temp)-1], f"{temp[len(temp)-1]:.2f}", rotation=45)
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)

    plt.savefig("assets/images/graphs/axs/minutely.png")
