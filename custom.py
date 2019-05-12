# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# メンションと文字列があった場合に返す
@respond_to('メンション')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ') # メンション

