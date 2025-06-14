### APIテスト
#### yfinance API
```
python test/yfinance_example.py
```

### ローカル開発環境
```
go run [fine name]
```
別のターミナル開いて  
```
ngrok http [port]
```

### 画像をなんとかする
```
cd images
python -m http.server 6000
ngrok http 6000
```