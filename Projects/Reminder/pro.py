# # import pydub
# # from pydub import AudioSegment
# # from pydub.playback import play
# # import datetime

# # time = input('enter the time: ')
# # alarm = AudioSegment.from_mp3('Projects/Reminder/voice/alarmTest.mp3')
# # play(alarm)

# # while True:
# #     time_now = datetime.datetime.now()
# #     now = time_now.strftime('%H:%M:%S')
# #     if now == time:
# #         medcine = AudioSegment.from_mp3('Projects/Reminder/voice/alarmTest.mp3')
# #         play(medcine)





# #     if now > time_now:
# #         break



import datetime
import time
from pydub import AudioSegment
from pydub.playback import play
import vonage

alarm_time = input(('Enter the alarm time : '))
alarm = AudioSegment.from_mp3('Projects/Reminder/voice/voice1.mp3')
play(alarm)

while True:
    time_now = datetime.datetime.now()
    now = time_now.strftime('%H:%M:%S')
    if now == alarm_time:
        alarm_sound = AudioSegment.from_mp3('Projects/Reminder/voice/alarmTest.mp3')
        play(alarm_sound)
        client = vonage.Client(key="1f2e4142", secret="cy0ItPgKO7Z52v5J")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
    {
        "from": "AI NINE",
        "to": "201092604920",
        "text": "Hurry up, you will miss your tasks",
    }
    )

    # client = vonage.Client(
    # application_id='VONAGE_APPLICATION_ID',
    # private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    # )
    # response = client.voice.create_call({
    # 'to': [{'type': 'phone', 'number': TO_NUMBER}],
    # 'from': {'type': 'phone', 'number': VONAGE_NUMBER},
    # 'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
    #  })
    # if now > time_now:
    #     break

