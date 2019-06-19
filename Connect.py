import pyrebase

config = {
  "apiKey": "AIzaSyC4xTkRgBx0FsRDTThHda6B_29XDQ4CFK4",
  "authDomain": "magic-ate-ball-58b99.firebaseapp.com",
  "databaseURL": "https://magic-ate-ball-58b99.firebaseio.com/",
  "storageBucket": "magic-ate-ball-58b99.appspot.com"
}

firebase = pyrebase.initialize_app(config)
