from flask import Flask, request, Response 
import requests
import csv
import io
from datetime import datetime

app = Flask(__name__)

@app.route('/usd_exchange', methods=['GET'])
def get_usd_exchange():

    ALLOWED_TOKEN = "access_token"

    token = request.args.get('token')
    if token != ALLOWED_TOKEN:
        return Response("Forbidden: Invalid token", status=403)
    
    today_str = datetime.today().strftime('%Y-%m-%d')
    start_date = request.args.get('start_date', today_str)
    end_date = request.args.get('end_date', today_str)

    start_str = start_date.replace('-', '')
    end_str = end_date.replace('-', '')

    url = (
        f"https://bank.gov.ua/NBU_Exchange/exchange_site?"
        f"start={start_str}&end={end_str}&valcode=usd&sort=exchangedate&order=desc&json"
    )

    try:
        api_response = requests.get(url)
        api_response.raise_for_status()
    except requests.RequestException as e:
        return Response(f"Error retrieving exchange rate data: {str(e)}", status=500)

    data = api_response.json()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Exchange Date", "Rate"])

    for record in data:
        writer.writerow([record.get("exchangedate", ""), record.get("rate_per_unit", "")])

    csv_output = output.getvalue()
    output.close()

    return Response(
        csv_output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=usd_exchange.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True)
