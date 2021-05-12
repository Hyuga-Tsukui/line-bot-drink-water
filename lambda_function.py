import json
import datetime
import os
import traceback
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

def lambda_handler(event, context):

    try:
        print(event)

        line_bot_api = LineBotApi(channel_access_token=os.environ['ACCESS_TOKEN'])
        line_bot_api.push_message(os.environ['GROUP_ID'], TextSendMessage(text='💧水のんだ？💧'))

        return {
            'statusCode': 200,
            'body': json.dumps('ok', ensure_ascii=False)
        }
    except:
        traceback.print_exc()
        return {
            'statusCode': 200,
            'body': json.dumps('ok', ensure_ascii=False)
        }
