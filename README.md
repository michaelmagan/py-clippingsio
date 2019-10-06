# py-clippingsio

This is a python application that will upload kindle notes to clippings.io.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Requires two packages to generate a working environment:
```
pip install pipenv pyenv
```

Install dependencies using the Pipfile:

```
pipenv install Pipfile
```

## Running

Create an account a https://www.clippings.io.

Add your username and password to the ```example_config.py``` file and remove the "example_" so it looks like ```config.py```.

```
pipenv run main.py
```

## Issues
Today when you run the script it will successfully login and get Auth token. When it tries to upload a clippings file it returns:

```
b'{\r\n  "success": false,\r\n  "ErrorAlreadyUploading": false,\r\n  "ErrorInvalidFileExtension": true,\r\n  "ErrorFileTooLarge": false,\r\n  "ErrorServerError": false,\r\n  "FileQueueID": 0,\r\n  "error": "has an invalid extension",\r\n  "IsOldYourHighlightsPage": false\r\n}'
```

I have it sending the file exactly as its done when I inspect chrome traffic. Even with the ```Content-Type: text/plain``` .
