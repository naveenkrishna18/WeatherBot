from telnetlib import AUTHENTICATION
import tweepy
import Weather

#twitter developer access
CONSUMER_KEY = " " #Enter your CONSUMER_KEY
CONSUMER_SECRET = " " #Enter your CONSUMER_SECRET

ACCESS_TOKEN = " "  #Enter your ACCESS_TOKEN
ACCESS_TOKEN_SECRET = " " #Enter your ACCESS_TOKEN_SECRET

#authentication of twitter API key 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter = tweepy.API(auth)

#Calling the function from Weather.py file
weather_info = Weather.get_weather_info() #getting weather from the Weather.py file

#converting it to a string
tweet = "Temprature is : " + str(weather_info[0]) + "°C\n" + "Feels Like : " + str(weather_info[1]) + "°C\n"+ "Humidity : " + str(weather_info[2]) + "\n" + "Pressure : " +str(weather_info[3]) + "mb\n" + weather_info[4] +"\n" + "Wind speed : " + str(weather_info[5]) + "kmph\n" + "Wind Direction(in degrees) : " + str(weather_info[6]) +"°"

#Posting the string to twitter
post_tweet = twitter.update_status(tweet) 

