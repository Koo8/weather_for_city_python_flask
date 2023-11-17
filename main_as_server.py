from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

"""create a Flask app"""
app = Flask(__name__)

"""routes of this app"""
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather_data():
    city = request.args.get('city') # city from the form input 
    if city:
        weather_data = get_current_weather(city)
    else:
        weather_data = get_current_weather()
    
    if weather_data['cod'] != 200:
        return render_template('city_not_found.html')

    return render_template(
        'weather.html',
        title = weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == '__main__':
    """development stage"""
    # app.run(host='0.0.0.0', port=8000)

    """deployment stage using waitress"""
    serve(app, host='0.0.0.0', port=8000)