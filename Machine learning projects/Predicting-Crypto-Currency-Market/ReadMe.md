# Crypto Currecny Price Predictions
This folder holds my findings about the connection between the ETF and Crypto-Currency market.
The ETF data will be gathered from www.justetf.com and the crypto currency from www.coingecko.com.
Coingecko even has a free API.

To use this project, run the make file with GNU make:
* 

Websites I coulde use:
* https://www.coingecko.com/en/api
* https://www.investing.com/indices/world-indices

* https://www.finanzen.net/indizes/alle
* https://www.justetf.com/de-en/find-etf.html?sortField=weekReturnCUR&orderDir=desc&groupField=index&sortOrder=asc&tab=rollreturn
* https://p.nomics.com/cryptocurrency-bitcoin-api
* https://messari.io/api

Examples
* https://github.com/nrese
* https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-2fa30d661c1e
* https://www.oreilly.com/openbook/make3/book/

## Project structure
```
Predicting_Crypto_Currency_Market
    |- data
    |   |- interim      <- merges different raw data
    |   |- processed    <- cleaned data
    |   |- raw          
    |- models           <- Serialized model
    |- notebooks        <- Jupyter Notebooks for exploration, communication and prototyping
    |- src          
        |- data         <- Scripts to generate data
        |- features     <- Scripts to transform data for modelling
        |- model        <- Scripts to train and predict
```
## Summary:
work in progress


## Techniques used in the following project:

* Data collection
    - Scrapy
    - API interaction
* Exploration of the generated datasets
* Predicting some currency values via machine learning algorithms


