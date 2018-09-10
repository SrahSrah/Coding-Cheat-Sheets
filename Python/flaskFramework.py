from satellite import satellite
from flask import Flask

app = Flask(__name__)  # pass in name to help Flask determine root path


# Routing/Mapping: connecting functions to webpages
# The @ signifies a decorator- a way to wrap a func and modify its behavior
# In flask, we use it to map a url to a return value
@app.route("/ssa")  # url of webpage
def ssa():
    iss = satellite()
    iss.tle2OE("C:/Users/SRHERNA1/Documents/0) STM/issTLE.txt")
    x, y = iss.sgp4Test()
    vecotrs = str(x) + "   " + str(y)
    return vecotrs

#You can pass in HTML to webpages:
@app.route("/tuna")
def tuna():
    return "<h2> Tuna is good </h2>"

#Using vars with URL:
#If I got to /profile/ANYNAME, ANYNAME will be displayed automatically
@app.route("/profile/<username>")
def profile(username):
    return "<h2>Hey there %s</h2>" % username

#Using integers:
@app.route("/post/<int:postID>")
def post(postID):
    return "<h2>Post ID is: %s</h2>" % postID

# Sets up server:
# Checks we only run webserver when file called directly:
if __name__ == "__main__":
    app.run(debug=True)  # starts app
