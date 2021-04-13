# crawler
A crawler as the term project of CSCI396 Computer Networks

The crawler can work, fits for the project description and what I have in mind (plus you can retool it as something useful later beyond :)). My only worry (that I think I've expressed before) is if you implement this in a way that it's too aggressively crawling :| you might get blocked from certain websites (cf., my ordeal with Umpqua Bank). IF you're doing multithreading (which I'd recommend) don't let it go wide (stick to two, maybe three at most threads and be certain they're stopping when needed).

Baseline Goal: Given a URL, your crawler should return a "map" of all the URLs linked from the first URL that are also on the same server and no higher in hierarchy (e.g., if I give you "reed.edu" it should return many websites including "reed.edu/computer-science/", but given "reed.edu/computer-science/" should not return reed.edu as part of the map). The "map" can be just a textfile with minor formatting indicating what's linked to what, or could be a data structure within your program (e.g., a tree :)) with at least a 'print' sort-of command for me to visualize. Basically, given an address, your crawler goes, retrieves the object (ideally first object is an HTML), parses the object, finds other URLs, checks that they're in the same path as the first object, fetches those objects, parses them, repeat. Makes sense?

I would recommend setting up your own web server with multiple objects and test locally against it (cf., your first mini project :)). 

Challenge Goals:
Read up on robots.txt (i.e., learn more about them), figure out how to parse them, and be able to throw your crawler at a public website without (much) fear of getting blocked by them :). 
Multithread (two threads) 
Pick some social media website, and figure out how to crawl/scrape for a specific object on them (e.g., can we aim your crawler at an Instagram account and get photos with a given hashtag?). This might require diving into the API of a specific website, some are nice some not so much... 

Any other potential challenge goals..?

Things to hand in: Your nicely written code (i.e., comments, good variable names, and efficient), a README indicating what I should run/what order to test it out, and a short writeup (e.g., 1 or 2 pages) describing any design decisions you might have made (e.g., "I used TCP because reason X.") and any potential extensions you see viable for the project (i.e., stuff you'd like to add to it, if you had the time/motivation, and how you might go about adding them). Think of the short writeup closer to a 'development diary' where you explain decisions made during development and sketch out how the project can grow beyond what you deliver. 

Grading: Similar to mini-projects, meaning 15 points are for coding style. The rest are obtained if your project operates as expected following the formula "more challenge goals means your code is allowed to have more weird corner case bugs".

