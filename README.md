# Smart-Mirror

This repository contains custom code for the UI and server for a Smart Mirror.

## Features

Users can choose what information they want to be displayed on the mirror as well as their position (the four corners). A website is exposed where users can change these settings live.

## Development

- **UI** - The user interface uses Python and a library call PyQT which makes it easier to develop graphical interfaces in Python and also features a GUI tool to build them (not used for this project).
- **Sever** - The server to handle users changing settings is programmed in Python using the Flask microframework due to it's simplicity. The actual version of Flask used is Flask-Classful which is a fork of the original library.
