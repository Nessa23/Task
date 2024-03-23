# The code in file game_score.py generates a list of game score states during a match. 
A function get_score(game_stamps, offset) was developed. It returns the score at the time of offset in the game_stamps list.

# Code in unittest_for_game.py: for the function get_score(game_stamps, offset) developed in file game_score.py, unit tests were made on the unittest framework.
The tests take into account all possible use cases of the function, focus on checking one case, tests are not repeated, the name of the tests reflect the essence of the test being performed.

# File parser.py: A parser was developed. It should have collected information about operating system versions in the top 100 smartphones with the highest user rating in the ozon.ru catalog.

On the site ozon.ru in the category "Electronics -> Phones and smartwatches" with sorting "High rating" information about the first 100 smartphones in the sample is collected. 
On the the page with each of them information about the operating system version from the characteristics was taken. According to the collected data a distribution of models by operating system version in descending order should be build, for example:

Android 8 - 12
Android 10 - 9
iOS 14 - 8
...
For parsing Scrapy framework was used, for downloading dynamic parts of the site Scrapy+Selenium was used. The scrapy proxy rotation middleware was used.

Pandas framework was used to calculate the distribution.

# Error 403 in parser
