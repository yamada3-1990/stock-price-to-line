// Copyright 2016 LINE Corporation
//
// LINE Corporation licenses this file to you under the Apache License,
// version 2.0 (the "License"); you may not use this file except in compliance
// with the License. You may obtain a copy of the License at:
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

// https://github.com/line/line-bot-sdk-go/blob/master/examples/echo_bot/server.go お借りしました
// 任意のタイミングでプッシュメッセージを送るテストコード
package main

import (
	"log"
	"os"

	// "os/user"

	"github.com/line/line-bot-sdk-go/v8/linebot/messaging_api"
	"github.com/joho/godotenv"
)

func main() {
	// channelSecret := os.Getenv("LINE_CHANNEL_SECRET")
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatal(err)
	}
	LINE_CHANNEL_TOKEN := os.Getenv("LINE_CHANNEL_TOKEN")
	bot, err := messaging_api.NewMessagingApiAPI(
		LINE_CHANNEL_TOKEN,
	)
	if err != nil {
		log.Fatal(err)
	}

	LINE_USER_ID := os.Getenv("LINE_USER_ID")
	log.Printf("LINE_USER_ID: %s", LINE_USER_ID) // デバッグログを追加

	pushMessage := &messaging_api.PushMessageRequest{
		To: LINE_USER_ID,
		Messages: []messaging_api.MessageInterface{
			messaging_api.TextMessage{
				Text: "これはプッシュメッセージのテストです",
			},
		},
	}
	if _, err = bot.PushMessage(
		pushMessage,
		"",
	); err != nil {
		log.Print(err)
	} else {
		log.Println("Sent text reply.")
	}
}
