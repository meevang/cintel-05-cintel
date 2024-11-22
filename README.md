# cintel-05-cintel
## Module 5: Building Apps with Live Data &amp; Continuous Intelligence

In this module, we introduce aspects of continuous intelligence - outputs updated on a regular basis or in real time as information becomes available. We provide only basic examples, but the principles enable a variety of continous intelligence aspects for many types of dashboards. 
Your app should have similar functionality to this basic example before you begin: 

Basic App: https://github.com/denisecase/cintel-05-cintel-basicLinks to an external site.
Once we have live data coming in, we need to want to create temporary storage to hold the "most recent" so we can present that - and analyze it online machine learning algorithms such as predicting a trend line using linear regression. We have a whole course on Streaming Data and another on Machine Learning, so you do NOT need to be able to implement those from scratch. Instead, we want to focus on your skills with presenting and displaying the information that might be available in an accessible and useful manner. 

An example that includes storing the readings in a deque (of dictionaries) and wrapping that deque in a reactive value as a way to manage our constantly changing state.

### Your job is to:

implement the example provided and
propose and implement an enhancement, extension, or variation on the app. 
Options include:

Changing the theme, colors, visuals to be more engaging
Changing the layout to better show the current deque
Changing the chart to not flash on each update
Changing the subject domain from temperatures in Antarctica (so we can add it to our Penguin Dashboards) to an alternate focus using random data appropriate for your chosen domain. 
Integrating live data and continuous intelligence into your own previous interactive app
The goal is to understand the possibilities and challenges of working with live data and consider how you can analyze and present "data in motion" to enhance your analytics projects. 

### Customize your requirements.txt
PyShiny Playground already includes all the packages listed below. Please do not add these packages to a requirements.txt running in the Playground - but include them in your requirements.txt that you would use for local development. 

faicons - for Font Awesome free Icons
pandas - for working with tabular data in Python
pyarrow - required by the new pandas
plotly - easy interactive charts
scipy - for the stats linear regression function to build a trend line for our chart
shiny - used to build our web app in Python
shinylive - used to build to our docs folder and host our app on GitHub Pages
shinywidgets - a wrapper for complex widgets like plotly charts

### Implement the Continuous Intelligence App
Code is not written from the top down like a book. Code is written from the outside in. It is typically organized first - using comment blocks.

Functions are "stubbed in" - returning a basic answer first while getting things connected together. Code is slowly added in, and once connected, we generally fine tune and finish implementing each function - adding error handling, and making sure all the possible special cases are covered (e.g. don't attempt to plot if the Data Frame is empty). 

Start here:

https://github.com/denisecase/cintel-05-cintel-basicLinks to an external site.

Then, implement this slightly fancier version:

https://github.com/denisecase/cintel-05-cintel-fancyLinks to an external site.

Then, implement this version with a deque wrapped in a reactive value, showing the associated datagrid and a plotly chart with online machine learning. 

https://github.com/denisecase/cintel-05-cintelLinks to an external site.

Read the comments. Organize the code. When you get your version implemented, save it - use a good commit message to indicate you've recreated the functionality as requested. 

Then, review the app, and:

Propose a modification / enhancement / extension. 
Plan your work. 
Estimate the time it will take. 
Implement your plan. 
Estimating the time a feature will take is a difficult and valuable skill. 

