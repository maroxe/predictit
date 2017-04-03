url='https://www.predictit.org/api/marketdata/all'
DATE=`date +%Y-%m-%d`

echo "Downloading..."
wget $url -O data.xml

echo "Recording..."
python record_quotes.py data/predictitquote.$DATE.sqlite3

