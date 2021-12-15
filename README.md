# chart-lyrics-analysis
This repository accompanies my bachelor thesis *Lyrics Mining: Investigating the Influence of the Coronavirus on 2020s Music Charts*.
Make sure to install the required packages: `pip install -r requirements.txt` for alle components to run properly.

## Execution Order
1. **top100_spider.py**

    `cd crawler/crawler`
    
    `scrapy crawl top100 -O R20-BB.json`
    
     - crawls Billboard Weekly Hot 100 Charts data
  
2. **billboard_weekly_100.ipynb**

    - consolidates G19-BB and R20-BB into BB-T100
  
3. **artist_song.ipynb**

    - groups unique songs and artists and removes censored words
    - generates BB-AS
  
4. **get_genius_lyrics.py \ get_genius_resources_v2.py**

    - utilizes LyricsGenius
    - gets lyrics, comments, annotations, descriptions, urls, ids, release dates from genius.com 
    - generates BB-L_raw
  
5. **lyrics_validation.ipynb**

    - validates lyrics
    - exports invalid lyrics with manually added GeniusIDs

6. **get_genius_resources_v2.py**

    - updates invalid genius.com data

7. **lyrics_preparation.ipynb**

    - adds updated data to BB-L_raw
    - determines language with LanguageDetector
    - changes shape and sorting
    - generates BB-L

8. **data_selection.ipynb**

    - filters English songs
    - generates BB-T100-EN and BB-L-EN

9. **keywords.ipynb**

    - gets keywords
    - determines COVID-19 songs
    - generates wordclouds for most used words

10. **sentiment.ipynb**

    - calculates and plots sentiment scores for lyrics

11. **topics.ipynb**

    - trains LDA model with AZLyrics data
    - uses model to determine topics for lyrics
    - plots topic distributions and frequency trends
