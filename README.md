# bike-route-path-recommender
```
conda create -y -n manga-rec python=3.8
```

## Content Based Filtering

### Attributes
These are attributes that I felt would help recommend another manga to another person

Title
- type : this can be of type Manga, Manhwa, etc
- score : current MAL score
- rank : overall current rank
- popularity : popularity of the manga
- synopsis : summary of the book TF-IDF
- author : list of authors
- genres : list of genres
- themes : list of themes
- demographics : list of demographics (seinen, shounen)

### Approach
Get 50 pages of 50 manga results = 2500 books in a json file with the above attributes.

Put all into a csv and serialize it

TF-IDF the synopsis

