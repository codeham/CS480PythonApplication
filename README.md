How to run this program..

1. install elasticsearch and make sure you have it running on your localhost

	-https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html

	- http:localhost:9200 should be the default port where elasticsearch runs

![Alt text](/README_images/localhost.png?raw=true "Localhost")

2. run app.py in a terminal or IDE, make sure all proper files from the repo are inside the same directory

	- make sure to install the proper elasticsearch python module *pip install elastic search*

![Alt text](/README_images/terminal.png?raw=true "Terminal")

3. go to localhost:9200/mappings/post/# (# is any range between 0 - maximum number of entries inside the log file)

4. the data should display properly organized in a JSON format (I would recommend installing a JSON viewer on your browser)

![Alt text](/README_images/api.png?raw=true "API")
