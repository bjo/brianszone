"""
Main app file for brians.zone site
Theme used is default bootstrap theme:
https://getbootstrap.com/docs/4.3/getting-started/introduction/
"""

from flask import Flask, render_template, request, redirect, url_for

# Create Flask webapp object
app = Flask(__name__)


# APIKEY = os.environ.get('APIKEY')

# decorator syntax - associated a URL with the python function
# instead of dealing with redirects, we can associate multiple URLs to a function
@app.route('/')
def entry_page() -> 'html':
    # provide the name of the template, and the value to go with the_title
    return render_template('index.html', the_title="Welcome to Brian's zone!")


# app.run()
# If run locally, it will run in debug mode. Otherwise, the deployment will run
# its own version of app.run()
if __name__ == '__main__':
    app.run(debug=True)
