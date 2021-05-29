python3 cropper.py &
wait
tesseract cropped.png final
printf "\n\n\n"
cat final.txt
python3 copy.py &
wait
notify-send 'Copying successful' 'Text copied successfully to clipboard'
