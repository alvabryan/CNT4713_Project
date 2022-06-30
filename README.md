# CNT4713_Project

Python flask

source venv/bin/activate

# Running app
# setting FLASK_APP (doesn’t need to be set if app name is app.py or wsgi.py)
export FLASK_APP=app.py
# starting debug mode
export FLASK_DEBUG=1
# running flask app 
flask run

# Running app with app.run()
# since we have app.run() in our main app then we can just run app using python
python app.py
