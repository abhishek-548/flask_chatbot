from flask import Flask, render_template, url_for, request, session, redirect


app = Flask(__name__)
# signup or home page
@app.route("/")
def home():
  return render_template("index.html")

#covidpage
@app.route("/covidpage")
def covidpage():
  return render_template("covidpage.html")

#pagetochatbot
@app.route("/pagetochatbot")
def pagetochatbot():
  return render_template("pagetochatbot.html")

#calculator
@app.route("/calculator")
def calculator():
  return render_template("calculator.html")

#contact
@app.route("/contact")
def contact():
  return render_template("contact.html")


#chatbotindia
@app.route("/chatbotindia")
def chatbotindia():
  return render_template("chatbotindia.html")

#chatbotworld
@app.route("/chatbotworld")
def chatbotworld():
  return render_template("chatbotworld.html")







if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=5000  # Randomly select the port the machine hosts on.
	)
