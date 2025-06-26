# 株価取得テストコード
# いったん日本株のみで 米国株入れると市場の時間帯が違うのでうまく取得できない

import sys
import yfinance as yf
import mplfinance as mpf
import datetime
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
plt.rcParams['font.family'] = 'MS Gothic'

# 銘柄
ticker_symbol = ["6861.T", "2593.T", "4063.T", "9432.T"]
ticker_name = ["キーエンス", "伊藤園", "信越化学工業", "NTT"]
today = datetime.date.today()



style = mpf.make_mpf_style(
    base_mpf_style='yahoo',
    rc={"font.family": plt.rcParams["font.family"][0]},
    y_on_right=False,
)

for symbol, name in zip(ticker_symbol, ticker_name):
    # Yahoo FinanceのTickerオブジェクトを作成
    ticker = yf.Ticker(symbol)

    print(f"--- 銘柄: {symbol} ({name}) の情報 ---")

    # 現在の株価情報を取得
    try:
        current_data = ticker.info
        if 'currentPrice' in current_data:
            print(f"現在の株価: {current_data.get('currentPrice')} {current_data.get('currency')}")
        else:
            print("現在の株価情報は利用できません。")
        # print(f"市場名: {current_data.get('fullExchangeName')}")
        # print(f"業種: {current_data.get('industry')}")
        # print(f"ウェブサイト: {current_data.get('website')}")
    except Exception as e:
        print(f"現在の株価情報の取得中にエラーが発生しました: {e}")

    print("\n--- 過去の株価データ ---")
    # 過去の株価データを取得 (periodとintervalを指定)
    # interval は '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo' など
    # period は '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max' など
    try:
        start_date = "2025-06-03"
        end_date = "2025-06-04" 

        hist = ticker.history(start=start_date, end=end_date, interval="1h")

        if not hist.empty:
            print(hist)
            mpf.plot(
                hist,
                type='candle',
                volume=True,
                title=f"{name}({symbol.rstrip(".T")}) {start_date}",
                style=style,
                savefig=f'images/{symbol.strip(".T")}.png',
                ylabel='株価 (JPY)',
            )
        else:
            print("指定された期間とインターバルで株価データが見つかりませんでした。")
            print("市場の開場時間やインターバル設定が正しいか確認してください。")

    except Exception as e:
        print(f"過去の株価データの取得中にエラーが発生しました: {e}")

# print("\n--- その他の情報 ---")
# try:
#     print("配当:")
#     print(ticker.dividends.tail()) # 最新の配当
# except Exception as e:
#     print(f"配当情報の取得中にエラーが発生しました: {e}")