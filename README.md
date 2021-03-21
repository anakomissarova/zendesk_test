How to install and run tests:
1. Clone repo\
`git clone https://github.com/anakomissarova/zendesk_test`
2. Create and activate virtual environment\
`cd zendesk_test/`\
`python3 -m venv venv`\
`source venv/bin/activate`
3. Install required modules\
`pip install requests`\
`pip install pytest`
4. Run tests using your API token\
`pytest tests/ --apiToken="<your API token here>"`\
You may also specify base URL and API version (defaults are https://api.getbase.com and /v2)\
`pytest tests/ --apiToken="<your API token here>" --baseUrl="https://api.getbase.com" --apiVersion="/v2"`
