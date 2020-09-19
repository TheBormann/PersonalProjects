

## Install Dependencies
requirements:
	conda env update -f environment.yml -n cryptoCurrencyPred


## Downloads data from the cloud
#download:

##  gathers data though periodically API calls and web scraping
gather :
	python src/data/cryptoCurrency.py


#all:
# will run whole pipeline from beginning to the end

clean:
	rm -f data/gathered/crypto.json

	rm -f data/raw/*.csv
	rm -f data/interim/*.csv
	rm -f data/interim/*.pickle
	rm -f data/interim/*.xlsx
	rm -f data/processed/*.pickle
	rm -f data/processed/*.xlsx
	rm -f data/processed/*.csv
	rm -f reports/figures/*.png
	rm -f models/*.model
