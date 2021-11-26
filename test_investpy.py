import investpy, json
import pandas as pd

search_result = investpy.search_quotes(text='ETH', products=['cryptos'], n_results=10)

for s_coin in search_result:
    coin = json.loads(str(s_coin))
    print('name: {} symbol: {}'.format(coin['name'], coin['symbol']))

# search cryptos with "eth"
l_crypto = investpy.crypto.get_cryptos_list()
l_crypto_eth = [s for s in l_crypto if "eth" in str(s).lower()]

pd_crypto_eth = pd.DataFrame()
l_pd_crypto = []

for str_crypto in l_crypto_eth:
    pd_crypto = investpy.crypto.get_crypto_recent_data(str_crypto, as_json=False, order='ascending', interval='Daily')
    # build list of Dataframes
    l_pd_crypto.append(pd_crypto)

pd_crypto_eth = pd.concat(l_pd_crypto, keys=l_crypto_eth)

print(pd_crypto_eth)
