# out-there-website

A blog for *Out There*, a midwest outdoor performance series showcasing strange sounds in unique places.

Built with [Pelican](https://getpelican.com/), styled with [Bootstrap](https://getbootstrap.com/) and hosted on [Netlify](https://www.netlify.com/).

## Creating new content

Blog content comes in two varieties: **news**, representing announcements or recaps, and **events** containing information about a specific performance event.

To post a news or event article, create a markdown file with the appropriate metadata (see below) and place it in either `out-there-website/content/events` or `out-there-website/content/news`.

Run `pelican -t theme --autoreload --listen content` and you will see the new post locally. Commit and push the new content to Github and it will appear on the website.

See below for instructions and metadata descriptions for each type of content.

## News

> Represents a blog post or announcement. 

### Metadata

- **`title`** (*str*)
    
    The title of the article. Will appear at the top of the page and in the browser tab.

**`template`** (*str*)

    The name of the HTML template for rendering the content. Use "news" for news articles and "event" for event articles.

- **`date`** (*`YYYY-MM-DD`, optional*)
    
    The article's publishing date in `YYYY-MM-DD` (eg. "posted on [DATE]"). Defaults to the date of article creation via Pelican's automatic `locale_date` attribute. Supply a `date` value to backdate an article.

- **`content`** (*str, markdown*)
    
    The body of the news article. Anything below the metadata section is considered to be `content`. Full markdown syntax support.

### News example

```
title: New example announcement!
template: news

This is the body of the annoucement. I can use **markdown** `syntax`.
```

## Events

> Represents a single event in the Out There series.

### Metadata

- **`title`** (*str*)

    The title of the event. Will appear at the top of the page and in the browser tab.

**`template`** (*str*)

    The name of the HTML template for rendering the content. Use "news" for news articles and "event" for event articles.

- **`event-date`** (*`YYYY-MM-DD`*)

    The date that the event will occur.

- **`event-flyer`** (*file path, optional*)

    A filepath to an image for the event, relative to `out-there-website/content/images/`.

- **`event-time`** (*str*)

    The starting time of the event. 

- **`event-location`** (*str*)

    The name and/or address of the event location.

- **`date`** (*`YYYY-MM-DD`, optional*)

    The article's publishing date, eg. "posted on `[DATE]`". Defaults to the date of article creation via Pelican's automatic `locale_date` attribute. Supply a `date` value to backdate an article.

- **`content`** (*str, markdown*)
    
    The body of the event article. Anything below the metadata section is considered to be `content`. Full markdown syntax support.

### Event example

```
title: June 2nd: TBA @ TBA
template: event
event-date: 2022-06-02
event-flyer: my-flyer.jpg
event-time: 6:00pm
event-location: TBA

Announcing our next show, **TBA @ TBA** featuring your favorites, *TBA*. 
```