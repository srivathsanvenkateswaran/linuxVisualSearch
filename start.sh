python3 cropper.py &
wait
tesseract cropped.png final &> /dev/null
printf "\n\n\n"
cat final.txt
python3 copytext.py &
wait
notify-send 'Copying successful' 'Text copied successfully to clipboard'
