echo "Launching the app"

echo "installing libraries"
pip3 install -r requirements.txt

echo "starting server"
uvicorn main:app