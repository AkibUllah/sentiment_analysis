For Api I Use Rest Framework 

# Update system
````
sudo apt-get update
sudo apt-get upgrade
````
## env
````
# For Ubunt/macos
python3 -m pip install --user virtualenv

# For Windows
py -m pip install --user virtualenv

# Create Env For Ubunt/macos
python3 -m venv env

# Create Env For Windowa
py -m venv env

#Active Env For Ubunt/macos
source env/bin/activate

#Active Env For Windowa
.\env\Scripts\activate
````

# Create a directory called Projects in $HOME if not exists already and switch
````
mkdir $HOME/sentiment_analysis_api
cd $HOME/sentiment_analysis_api
````
# Install pip requirements
````
pip install -r requirements.txt
````
# Run Project
````
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
````

# Api

````
/api/v1/sentiment-analysis/
````

# Body
````
{
    "text": "I Love Anime"
}
````

# Response
### Success Response
````
{
    "sentiment": "positive"
}
````

### Error Response
````
{
   'messages': "Text Field Is Missing"
}
or
{
   'messages': "Text Can't Be Empty"
}
or
{
   'messages': "Only Sentence Are Allowed"
}
or
{
   'messages': "Text Can't Be Integer"
}
````