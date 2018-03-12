# Facebook-Scraper
This script runs on command line, to extract returns the text of the last 8 posts made on Expedia Facebook Page or any page(change the page name in the script), and re-writes such data into a text file using JSON.

Language used: Python
Used Facebook Graph API’s to fetch the data from Expedia public page. 

What information can be inferred from the post?
  
  1. How people has responded to the post?
  In order to gather this information, used reaction data. There are six types of reactions (Like, Wow, Sad, Angry, Love, Ha-ha). Out of which Wow, Like, Love are considered positive response and Angry, Sad are considered negative reactions. Ha-ha is ignored because it can be sarcastic reaction or positive reaction. So, it is better to ignore Ha-ha data instead of making a false assumption.  
  This kind of information can be used to analyse the customer response to promotional posts on Expedia page.
    
  2. Count of people who has responded the post. (Count of people who are active on Expedia page)
  Positive or negative response, increase the total number of active people on Expedia page is more important. So ALL_RESPONSES_COUNT in the Json file gives this information.

Instructions to run:

python Question1.py

Output:

Check Expedia_Page_Top_8_Posts.txt in the same directory as Question1.py

JSON in  Expedia_Page_Top_8_Posts.txt was verified using https://jsonformatter.curiousconcept.com 

Check the following image for sample JSON:

![alt text](https://github.com/RadhikaKalaiselvan/Facebook-Scraper/blob/master/Picture1.png)


Python Version: 3.6.1

Install the following libraries:

pip install facebook-sdk
