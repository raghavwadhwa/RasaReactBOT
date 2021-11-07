# MYNTRA BACKEND SERVER

This is the Django Rest Framework Server for the VoiceBot that we have developed.

# Python Setup

```bash
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

# Venv Steps

```
sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate

To QUIT -> quit()
```

# Django and other Dependencies Installation

```bash
pip install Django
pip install djangorestframework
pip install django-cors-headers
pip install requests
```

# Text and Speech Recognition and Conversion Dependencies

```bash
pip install googletrans==3.1.0a0
pip install SpeechRecognition
pip install gTTS
pip install gTTS-token
```

# Django Server Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Quit Server

```
Quit the server by pressing "CTRL+C"
```

## Learn More

You can learn more about the Django Framework and about it's development server in the [Django Writing Your First App](https://docs.djangoproject.com/en/3.2/).

To learn about the Django Rest Framework, check out the [Django Rest Framework Documentation](https://www.django-rest-framework.org/tutorial/quickstart/)
