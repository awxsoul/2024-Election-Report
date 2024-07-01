# 2024-Election-Report
 Extraction of election results and generating a comprehensive report on it 

 This is a partially achieved project, based on the task assigned by Kalvium as a part of their recruitment process. 

Task:
1) Scrape the information of the recently concluded Lok Sabha election from https://results.eci.gov.in 
2) Build a report of 10 key insights you can derive from the data, and submit that to the repository.

## Stages of development
### Set up Environment
Required libraries for this project are imported 
- requests: A simple yet powerful library for making HTTP requests to interact with web services and APIs.
- pandas: A versatile data analysis and manipulation library providing data structures like DataFrames for handling structured data.
- BeautifulSoup4: A library for parsing HTML and XML documents, making extracting data from web pages easy.
- selenium: A tool for automating web browsers, often used for web testing and scraping when JavaScript rendering is required.

### Soup of the webpage
Extracted soups to navigate through the HTML Unicode. The list of States is acquired here. This is further used to navigate through each state's pages. Similarly for each Constituency under that.

### Selenium to navigate
Moving to all the required pages through automated functions, together with Beautiful Soup, helps the program to extract from different pages in a go.

### Approach to locate information 
- State list is acquired from soup
- Using selenium, the selection of each state leads to the page having information about the state
- Under the state page, constituencies are parsed in a similar way
- For better and more information, the table format of the data is extracted

### Pandas Dataframe 
The extracted information of Candidates, the party they belong to, vote counts and more are fed to the dataframe of pandas. The dataframe contains rows for each candidate filling the column information of State, Constituency, Candidate, Party, EVM_votes, Postal_votes, total_votes and percentage_of_votes.

### Further developments are yet to complete
Part one of the task is completed here, extracting the information from the website completely into the dataframe.
The next part consists of refining the data, defining the key insights of the results, and visualising them for user convience.

## Problems faced during development
### Chromedriver
Selenium did not work in the absence of the chromedriver.
The selenium needed chromedriver installed to operate and automate in Chrome. Firefox and other web browsers have different drivers.
Added its the path to environment variables and passed the location of the chromedriver for the argument of chromedriver() function.

### Deprecated attributes of driver
find_element_by_* were deprecated and are not longer used. 
driver.find_element(attribute, value) is used in this project instead. 
This was used to select the drop-down menu option.

### Extracted Data Difference 
The Constituency list extracted using beautifulsoup is "Dhubri  - 2". 
The Constituency drop-down menu could only navigate "Dhubri - 2". 
Still unreasonable as to why it happened, this difference was followed by other few selective constituencies too.
This was solved by splitting the string from the list by beautiful soup and using join(), they are mapped together by their components.  

### Deprecated append function 
The append () attribute of the data frame is no longer supported. 
Concat() and join() are used to merge and add dataframes together.

## Why these details?
I like documenting.
