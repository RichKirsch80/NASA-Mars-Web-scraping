Landing Page for Mars Info web-scraped from NASA websites

Custom landing page that displays previously scraped data as well as a scrape button to pull most recent data.

Completed an initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of your scraping and analysis tasks. 
The following data is scraped from the NASA Mars website.

NASA Mars News
Scrapes the Mars News Site and collect the latest News Title and Paragraph Text. Assigned both variables for results index.html page.

JPL Mars Space Images - Featured Image
Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

Mars Facts
Visits the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Saved into dataframe, formatted and coverted to html.

Mars Hemispheres
Visits the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
Saves both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
Uses a Python dictionary to store the data using the keys img_url and title.

Step 2 - MongoDB and Flask Application
Uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Created Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and 
return one Python dictionary containing all of the scraped data.

Next, created a route called /scrape that will import your scrape_mars.py script and call your scrape function.
Stored the return value in Mongo as a Python dictionary.
Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the 
appropriate HTML elements.
