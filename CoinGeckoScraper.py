from bs4 import BeautifulSoup
import requests
import pandas as pd

name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for i in range (1,131):

    url = 'https://www.coingecko.com/?page=' + str(i)

    response = requests.get(url)
    print(str(i), " Connection ", response.status_code)

    soup =soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')
    print("Page ", str(i)," - Total results ", len(results))

    for result in results:

        try: #name
            name.append(result.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            name.append('N/A')

        try: #price
            price.append(result.find('td',{'class':'td-price'}).get_text().strip())
        except:
            price.append('N/A')

        try: #change_1h
            change_1h.append(result.find('td',{'class':'td-change1h'}).get_text().strip())
        except:
            change_1h.append('N/A')

        try: #change_24h
            change_24h.append(result.find('td',{'class':'td-change24h'}).get_text().strip())
        except:
            change_24h.append('N/A')

        try: #change_7d
            change_7d.append(result.find('td',{'class':'td-change7d'}).get_text().strip())
        except:
            change_7d.append('N/A')

        try: #volume_24h
            volume_24h.append(result.find('td',{'class':'td-liquidity_score'}).get_text().strip())
        except:
            volume_24h.append('N/A')

        try: #market_cap
            market_cap.append(result.find('td',{'class':'td-market_cap'}).get_text().strip())
        except:
            market_cap.append('N/A')

# Dataframe
crypto_df = pd.DataFrame({'Coin': name, 'Price': price, '1hr Change': change_1h, '24hr Change': change_24h, '7d Change': change_7d, '24hr Volume':volume_24h, 'Market Cap': market_cap})
crypto_df.to_excel('CryptocurrencyDataset.xlsx', index=False)
print("Scraping Complete >>> Dataset Generated")