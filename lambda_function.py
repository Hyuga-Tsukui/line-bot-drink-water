import json
import datetime 
import os
import traceback
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)


def is_holiday(date):
    holiday = [5, 6]
    if date.weekday() in holiday:
        return True
    else:
        False



def lambda_handler(event, context):

    today = datetime.date.today()

    if is_holiday(today):
        return {
            'statusCode': 200,
            'body': json.dumps('ok', ensure_ascii=False)
        }

    try:
        print(event)

        line_bot_api = LineBotApi(channel_access_token=os.environ['ACCESS_TOKEN'])
        buttons_tmplate_messages = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='ぶぶチェック',
                text='水のんだ？',
                actions=[
                    PostbackAction(
                        label='のんだ！',
                        display_text='のんだ！',
                        data='status=ok'
                    ),
                    PostbackAction(
                        label='のんでない！',
                        display_text='のんでない！',
                        data='status=ng'
                    )
                ]
            )
        )
        line_bot_api.push_message(os.environ['GROUP_ID'], buttons_tmplate_messages)

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