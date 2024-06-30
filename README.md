# 2024-Election-Report
 Extraction of election results and generating comperhensive report on it 

 This is partially achieved project based on the task assigned by Kalvium as a part of their recruitment process. 

Task:
1) Scrape the information of the recently concluded Lok Sabha election from https://results.eci.gov.in 
2) Build a report of 10 key insight that you can derive from the data, and submit that in the repository.

## Stages of developemnt
### Set up Environmrnt
Required libarires for this project are imported 
- requests: A simple yet powerful library for making HTTP requests to interact with web services and APIs.
- pandas: A versatile data analysis and manipulation library providing data structures like DataFrames for handling structured data.
- beautifulsoup4: A library for parsing HTML and XML documents, making it easy to extract data from web pages.
- selenium: A tool for automating web browsers, often used for web testing and web scraping when JavaScript rendering is required.

### Soup of the webpage
Extracting soups to navigate through the html unicode. List of States are noted here. This is further used to navigate through each state pages. Similarly for each Constituencies under that.

### Selenium to navigate
Moving to all the required pages through automated functions, together with beautiful soup helps program to extract from different pages in a go.

### Approach to locate information 
- State list is accquired from soup
- Using selenium, selection of each state leads to the pag having information about the state
- Under the state page, Constituencies are parsed the similar way
- For better and more information, table format of the data is extracted

### Pandas Dataframe 
The extracted information of Candidate, the party they belong, votes counts and more are fed to the dataframe of pandas. The dataframe contains rows of each candidate filling the column information of State, Constituency, Candidate, Party, EVM_votes, Postal_votes, total_votes and percentage_of_votes

### Further developements are yet to complete
Part one of the task is completed here, extracted the information from the website completely into the dataframe.
Next part consists of refining the data, define the key insights of the results, and visualising them for user convience.

## Problems faced during development
### Chromedriver
Selenium did not work in the absence of chromedriver.
The selenium needed chromedriver installed to operate and automate in chrome. Firefox and other web browsers have different drivers.
Added it's path to environment varibales and passed the loaction of the chromedriver for argument of chromedriver() function 

### Deprecated attributes of driver
find_element_by_* was deprecated and is not longer used.
driver.find_element(attribute, value) is used in this project instead
This was used to select the drop dowm menu option

### Extracted Data Difference 
The Constituency list extracted using beautifulsoup is "Dhubri  - 2"
The Constituency drop down menu could only navigate "Dhubri - 2"
Still unreasonble to why it happened, this difference was followed to other few slective constituencies too.
This was solved by splitting the string from the list by beautifulsoup and using join() they are mapped together by its componets.  

### Deprecated append funtion 
Append() attribute of dataframe is no longer supported
Concat() and join() is used to merge and add dataframes together

## Why these details?
I like documenting.