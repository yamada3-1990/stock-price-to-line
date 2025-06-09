公開範囲を限定するには合言葉制/passwordにした方が良いの？かな？

webhook url必要なのかあ ngrokでできるらしい
```
ngrok http 8080
```
~~いちいち.exeあるとこに移動するのめんどい ngrokのパス追加するべきか~~←追加した✅

### webhookの設定で詰まる(解決済み)
*line_bot_ex.go  
アプリケーション立ち上げ->ngrok立ち上げ  
webhook urlを入力して検証すると404 page not foundなる
http://localhost:5000/ にアクセスしてもなる


https://~~~/callback に変更したら成功した；；
>l:38 http.HandleFunc("/callback", func(w http.ResponseWriter, req *http.Request)

で/callbackで受け付けてた  成功したらwebhookの利用をオンにするのを忘れずに
