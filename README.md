"# Python-Automation-" 
"# Python-Automation" 


To run the tests parallel use the below one in terminal
pytest -v -s -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

To capture logs in html reports 
pytest -v --html=Reports\report.html testCases/test_login.py --browser chrome
