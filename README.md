# Linux-Visual-Search
Script to provide a functionality similar to Bing Visual Search to Linux

running the start.sh will take screenshot of your current screen and will open an image window.

click and drag the area you want to perform OCR and press C.

The text will be copied to your clipboard.

### Note

In order to perform OCR with the image, you need to have tesseract OCR installed in your system.

Open your terminal and type the following command to install Tesseract-ocr

```
sudo apt-get install tesseract-ocr
```

Also make sure that you have python3 in your system and have the required modules installed. 

After cloning the repo, In your terminal, type the following command to install the required modules

```
pip install -r requirements.txt
```

And don't forget to change the file paths to their full path [Absolute Path]

## Tip
You can create a file and place it in ```/usr/bin``` directory and execute it as a terminal command. </br>

Here's how you can do so. </br>
#### Creating Files for scripts
```
cp start.sh vSearch
cp cropper.py cropper
cp copytext.py copytext
```
#### Converting cropper as linux command
Open the file cropper in nano editor
```
nano cropper
```
Now add the following line on top of the cropper file
```
#!/usr/bin/python3
```
Then move the cropper file to ```/usr/bin```.
```
sudo cp cropper /usr/bin
```
#### Converting copytext as linux command
Open the file copytext in nano editor
```
nano copytext
```
Now add the following line on top of the cropper file
```
#!/usr/bin/python3
```
Then move the cropper file to ```/usr/bin```.
```
sudo cp copytext /usr/bin
```

## If you liked this project or found this useful..

Kindly tweet it out or share this in any other social Media platform so that more people can make use of this :)

## Demo GIF

![Linux-Visual-Search](https://user-images.githubusercontent.com/74530357/120639861-73f90880-c48f-11eb-8a3d-398eba5303c3.gif)


Feel free to ping me if you have any doubts or you wish to contribute :)
