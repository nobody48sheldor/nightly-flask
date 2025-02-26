# for of :

https://github.com/damnitharshit/nightly

<p align="center">
<img src="logo.svg" width="250"/>
</p>

A minimal and configurable start page for the web browser of your choice.

## Installation

### For Chromium-based browsers
- Download [New Tab Redirect](https://chrome.google.com/webstore/detail/new-tab-redirect/icpgjfneehieebagbmdbhnlpiopdcmna).
- In your autostart script of your DE/WM, add `export FLASK_APP=PATH/flask-local.py && flask run -p PORT`
- Go to extension settings and set `127.0.0.1:PORT` as Redirect URL.

### For Firefox-based browsers
- Download [New Tab Override](https://addons.mozilla.org/en-US/firefox/addon/new-tab-override/).
- In your autostart script of your DE/WM, add `export FLASK_APP=PATH/flask-local.py && flask run -p PORT`
- Go to extension settings and set `127.0.0.1:PORT` as Redirect URL.

NOTE : The blur effect in this project is applied with [this CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) which isn't enabled by default in firefox. Follow the steps on [this guide](https://dev.to/snkds/how-to-enable-backdrop-filter-in-firefox-2n8e) to enable it manually and the blur should work fine. 

## FAQs

### How do I change the settings?
Let's take the example of changing the background :
- You go on the internet, find an image and download it such that its path is `/home/myusername/Downloads/myimg.png`.
- You open [our site](https://damnitharshit.github.io/nightly/) and click on the settings icon.
- You click on the button labelled `GENERAL`.
- You enter `/home/myusername/Downloads/myimg.png` in the field under the label `Background`.

..and that's it! The image would have been applied to the background, and it'll stay that way until you clear your browser cache or move the image to another place.

### How do I change the search engine ?
look through the code of `flask-local.py` and at the line `return(redirect("https://search.brave.com/search?q={}&source=web".format(value)))`, you can change the url to use whatever search engine you want

## Preview
<p align="center">
<img src="nightly-flask.png" width="600">
</p>

