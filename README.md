# Exchange-rate-update-script

## Description

This Python script runs a Flask API that returns structured data in CSV format and writes the response to a connected Google Sheet. The API accepts three URL parameters:

- `start_date`: start of the period (format: `yyyy-mm-dd`)
- `end_date`: end of the period (format: `yyyy-mm-dd`)
- `token`: required access token

If dates are not provided, the current date is used by default.

### Output

The response is written to a Google Sheet and returned as a CSV file with the following columns:

- Exchange Date  
- Rate
  
### Deployment and Usage

The script is deployed on PythonAnywhere and can be accessed via a URL request formatted as follows:

https://svetsedykh.eu.pythonanywhere.com/usd_exchange?start_date=2024-04-01&end_date=2024-04-05&token=ACCESS_TOKEN

The parameters are passed in the URL. The returned CSV is suitable for use in tools that support live data connections, including Google Sheets.

### Technologies Used

- Python  
- Flask  
- Requests  
- CSV and io.StringIO  
- PythonAnywhere (for deployment)  
- Google Sheets (connected via `IMPORTDATA`)

