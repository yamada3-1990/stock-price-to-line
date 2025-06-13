公開範囲を限定するには合言葉制/passwordにした方が良いの？かな？

webhook url必要なのかあ ngrokでできるらしい
```
ngrok http 8080
```
いちいち.exeあるとこに移動するのめんどい ngrokのパス追加するべきかーーーーーー

##### webhookの設定で詰まる
*line_bot_ex.go
アプリケーション立ち上げ->ngrok立ち上げ  
webhook urlを入力して検証すると404 page not foundなる
http://localhost:5000/ にアクセスしてもなる


https://~~~/callback に変更したら成功した；；
>l:38 http.HandleFunc("/callback", func(w http.ResponseWriter, req *http.Request) 
で/callbackで受け付けてた  

成功したらwebhookの利用をオンにするのを忘れずに


##### 画像メッセージについて
画像のURLとしてHTTPSのURLを使用する必要がある
ローカルにHTTPサーバーを立てて、画像を配信するように設定→ngrokを使って、そのローカルサーバーをHTTPSで公開→そのURLを指定 らしい  
originalContentUrl と previewImageUrlどっちにも設定する必要があるって