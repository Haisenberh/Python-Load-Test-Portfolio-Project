# Python Selenium Web Tests Portfolio

This is a project that contains example of Selenium end-to-end tests written in Python:
- web behaviour driven tests based on [pytest-bdd](https://pypi.org/project/pytest-bdd/) framework
- web tests can run on a Cloud using [CircleCi](https://circleci.com/) continuous integration tool
- tests steps are stored in [Gherkin](https://cucumber.io/docs/gherkin/reference/) syntax, which is easy to read and understand by non programmers  
- project is using  [Page-object](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) pattern, which simply Web page as a class. This reduces the amount of duplicated code  
- config variables are stored in local _.env_ file with usage [env-parse](https://pypi.org/project/envparse/0.1.6/) which help to securely store variables locally and on CircleCi
- Selenium driver instance is designed as [Singleton](https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/) pattern, which allows us to limit concurrent access to a shared driver
- reports are saving using [pytest-html](https://pypi.org/project/pytest-html/) extension. You can see examples of reports in */home/reports* folder

### Please read instructions bellow how to set up the project.

1. create _.env_ file in root directory [env-parse](https://pypi.org/project/envparse/0.1.6/) is used to store sensitive config locally
```
BROWSER=safari
IMPLICIT_WAIT=10
BROWSER_WIDTH=1366
BROWSER_HEIGHT=768
HOME_PAGE=https://demoqa.com/
```
2. Install needed libraries using pip (Make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed)
```
pip3 install -r requirements.txt
```
3. Download and install needed browser drivers (You need to have [brew](https://brew.sh/index_uk) already installed):
```
brew install chromedriver
brew install geckodriver
```
4. Run web selenium tests: 
Example of running all web tests by [pytest-bdd](https://pypi.org/project/pytest-bdd/) (see available tags in tests/features: example _@web_tests_):
```
python3 -m py.test -v -m web_tests --html=e2e-report.html --self-contained-html
```
5. Review the reports (reports folder) and screenshots in */reports* folder
*****
### Run all tests on local CI (using [CircleCi](https://circleci.com/docs/2.0/local-cli/))
Install circle ci (requires brew)
```
brew install circleci
```
Install docker desktop:

https://www.docker.com/products/docker-desktop

Setup circle ci (you must have account there):
```
circleci setup
```
Run web tests:
```
circleci local execute --job run_web_tests
```
### Troubleshooting:
Update chromedriver
```
brew upgrade --cask chromedriver
```
Add permission to execute chromedriver
```
xattr -d com.apple.quarantine /usr/local/bin/chromedriver 
```


