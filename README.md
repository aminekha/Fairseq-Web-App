# Pytorch Translator Web App

## Introduction
This translation web app is built using Pytorch, Fairseq, and Django. The current version can translate text from English to French but with future updates I will add new languages.

## Features
<ul>
    <li>Train your own model or use the pretrained model (link below)</li>
    <li>Beautiful UI to interact with the app</li>
    <li>Easy to use</li>
</ul>

## Setup
Setup everything using the requirements.txt file. 
Just run ``` python3 -r requirements.txt ```

## Usage
If you have everything installed (including Pytorch and Django) you just need to run:
``` python3 manage.py runserver ``` 
Then wait for it to load the model. 
Then all you need is to open 127.0.0.1:8000 and interact with the chatbot.

## Pretrained Models
You can find all the pretrained models for different languages <a target="_blank" href="https://github.com/pytorch/fairseq#pre-trained-models-and-examples">here.</a>