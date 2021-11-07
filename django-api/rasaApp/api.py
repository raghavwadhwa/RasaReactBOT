from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from googletrans import Translator
import speech_recognition as sr
import os
import requests
import json
from gtts import gTTS
import ast
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TranslateViewSet(APIView):

    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def post(self, request, format=None):
        permission_class = [permissions.AllowAny]
        print(request.FILES['file'])
        fs = FileSystemStorage()
        myfile = request.FILES['file']
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        LANGUAGE = "en_US"
        print("starting...")
        print(myfile.name)
        r = sr.Recognizer()
        temp = str(os.getcwd()+'/media/'+filename)
        print(temp)
        with sr.AudioFile(temp) as source:
            audio = r.record(source)
        command = r.recognize_google(audio, language=LANGUAGE)
        translator = Translator()
        print(command)
        lang = translator.detect(command)
        lang = lang.lang
        command = translator.translate(command, dest=lang)
        command = command.text
        print(lang)
        return Response({"lang": lang, "msg": command})


class ResponseViewSet(APIView):

    def post(self, request, format=None):
        permission_class = [permissions.AllowAny]
        print(type(request.body))
        obj = request.body.decode('utf8').replace("'", '"')
        print(obj)
        obj = json.dumps(obj)
        obj = json.loads(obj)
        obj = ast.literal_eval(obj)
        msg = str(obj["msg"])
        language = str(obj["lang"])
        translator = Translator()
        out = translator.translate(msg, dest="en")
        sender = "yashwant"
        print(out.text)
        response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                                 json={"message": out.text, "sender": sender})
        try:
            print(response)
            response = json.loads(response.text)
            print(response)
            response = response[0]["text"]
            print(response)
            print(len(response), response)
        except:
            response = "Sorry, I was not able to understand your query. Please try again!"
        if(language != "en"):
            response = translator.translate(response, dest=language)
            response = response.text
        tts = gTTS(text = response, lang = language, slow = False)
        path = os.getcwd()
        os.chdir(path+'//media//')
        rnd = id_generator()
        name = sender+str(rnd)+".wav"
        tts.save(name)
        os.chdir(path)
        uploaded_file_url = "http://127.0.0.1:8000/media/"+name
        print(uploaded_file_url)
        return Response({"msg": response, "url": uploaded_file_url})
