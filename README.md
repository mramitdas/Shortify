# Shortify

A URL shortener takes Youtube long, unwieldy link and turns it into a shorter link, one that's easy to share.

- For example:
  - Input: https://youtu.be/Li0Abz-KT78
  - Output: https://shrtco.de/qTsuEz

## Table of Contents

- [Introduction](#Introduction)  
- [Getting Started](#Getting-Started)  
- [Tech Stack](#Tech-Stack)
- [Installation](#Installation)
- [Project Structure](#Project-Structure)
- [Features](#Features)
  - [URL Shortner](#URL-Shortner)
  - [Encryption & Decryption](#Encryption-&-Decryption)
  - [Recent Video](#Recent-Video)
  - [Url Tracker](#Url-Tracker)
 

## Introduction

While **Shortify** used to be useful for shortening longer links to fit character limits on social media and messaging apps, a lot of platforms take care of that for you. **Shortify** allow you to provide a typable link on a business card, print ad, podcast interview, or any other situation where someone can't just click on a nice hyperlink. 

## Getting Started

Clone or download this repository.
> $ git clone https://github.com/mramitdas/shortify.git 

> $ python ./main.py

## Tech Stack

A simple web application built with

- Flask  
- MongoDB
- Requests
- CryptoCode
- Socket

## Installation

You can install above packages using following command:
> $ pip install Flask, pymongo, dnspython, requests, cryptocode

Or you can install from source with:
> $ pip install requirements.txt

## Project Structure
```
|   main.py
|   Procfile
|   README.md
|   requirements.txt
+---static
|   +---css
|   |       main_table.css
|   |       style.css
|   |       result.css
|   +---fonts
|   |       font-awesome-4.7.0
|   |       OpenSans         
+---templates
|       index.html
|       track.html
|       video.html
|       result.html
+---Utils
|       database.py
|       security.py
```

## Features

### URL Shortner

https://user-images.githubusercontent.com/83647604/165144416-245b23a3-4436-431e-9ba3-e02ac3523413.mov

### Encryption & Decryption

https://user-images.githubusercontent.com/83647604/165144615-4b5669b9-cbd4-4969-899f-529a9e81968c.mov

### Recent Video

https://user-images.githubusercontent.com/83647604/165144697-59c92c8a-89c0-4bd3-8153-60f44b8c2d27.mov

### Url Tracker

https://user-images.githubusercontent.com/83647604/165145014-f41ff9a8-e0c1-412b-9e44-00b89ca8db7d.mov


