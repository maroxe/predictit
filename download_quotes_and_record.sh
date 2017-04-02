url='https://www.predictit.org/api/marketdata/category/13'

echo "Downloading..."
wget $url -O data.xml

echo "Recording..."
python record_quotes.py
