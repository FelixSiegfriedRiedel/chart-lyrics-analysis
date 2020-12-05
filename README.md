# chart-lyrics-analysis
*Exploration of 2020s most heard lyrics based on [Billboard's weekly top 100 lists](https://www.billboard.com/charts/hot-100/2020-01-04).*

## Setup
### [Scrapy](https://scrapy.org/) package to crawl Billboard
`pip install Scrapy`

### [lyricsgenius](https://pypi.org/project/lyricsgenius/) package for calling the Genius API
`pip install lyricsgenius`

### [Jupyter](https://jupyter.org/) for creating jupyter notebooks
`pip install jupyter`

### Common packages for exploring and manipulating data
`pip install numpy`

`pip install pandas`

`pip install seaborn`

`pip install matplotlib`

## Crawling Billboard's weekly top 100 list
*Crawling is rather time consuming and is only necessary when new weekly list is available*

`cd crawler`

`scrapy crawl top100 -O ..\input\top100.json`
