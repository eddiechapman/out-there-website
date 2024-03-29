# out-there-website

A blog for *Out There*, a midwest outdoor performance series showcasing strange sounds in unique places.

Built with [Pelican](https://getpelican.com/), styled with [Bootstrap](https://getbootstrap.com/) and hosted on [Netlify](https://www.netlify.com/).

## Creating new content

Blog content comes in two varieties: **videos**, representing video releases, and **events** containing information about a specific performance event.

To post a video or event article, create a markdown file with the appropriate metadata (see below) and place it in either `out-there-website/content/events` or `out-there-website/content/videos`.

Run `pelican -t theme --autoreload --listen content` and you will see the new post locally. Commit and push the new content to Github and it will appear on the website.

See below for instructions and metadata descriptions for each type of content.

## Videos

> Represents the videos from a single event. 

### Metadata

- **`title`** (*str*)
    
    The title of the article. Will appear at the top of the page and in the browser tab.

- **`subtitle`** (*str*)
    
    The location and date of the video. Used in the preview card on the list of videos.

- **`template`** (*str*)

    The name of the HTML template for rendering the content. Use "video" for video articles 
    and "event" for event articles.

- **`preview`** (*filepath, optional*)

    A filepath to preview image that will be used as the background of the preview card. 
    Filepath is relative to `out-there-website/content/images/`. Must be 1:1 ratio (square).

- **`date`** (*`YYYY-MM-DD`, optional*)
    
    The date the video was shot in `YYYY-MM-DD`. Defaults to the date of article creation 
    via Pelican's automatic `locale_date` attribute. Supply a `date` value to backdate an article.

- **`content`** (*str, markdown*)
    
    The body of the article. Anything below the metadata section is considered to be `content`. 
    Full markdown syntax support.


## Events

> Represents a single event in the Out There series.

### Metadata

- **`title`** (*str*)

    The title of the event. Will appear at the top of the page and in the browser tab.

- **`template`** (*str*)

    The name of the HTML template for rendering the content. Use "news" for news articles and "event" for event articles.

- **`thumbnail`** (*filepath, optional*)

    A filepath to a thumbnail image to be displayed on the article preview. Filepath is relative to `out-there-website/content/images/`. Must be 1:1 ratio (square).

- **`event-date`** (*`YYYY-MM-DD`*)

    The date that the event will occur.

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
thumbnail: 
event-date: 2022-06-02
event-time: 6:00pm
event-location: TBA

Announcing our next show, **TBA @ TBA** featuring your favorites, *TBA*. 
```

## Color theme

Found here: https://colorhunt.co/palette/fefbf6a6d1e67f52833d3c42


## Changelog

**`2024-02-17`**

- video articles
    + now represent all the videos from a single show
    + preview cards only have `title` and `subtitle`
    + preview cards have background image supplied by John
    + reorganized video md files to reflect this
- nav bar reorganization
    + removed `home` link
    + removed `about` link
- home page 
    + moved `about` content to the home page


**`2024-01-27`**

- color scheme
    + https://colorhunt.co/palette/fefbf6a6d1e67f52833d3c42
    + applies to font text, background pattern, background colors
- nav bar
    + merged "contact" with "about" page
    + reordered nav menu links
    + increased title and header font sizes
    + added instagram link to nav
- carousel
    + swap art with photos from events
    + reduce max height on mobile
    + slow down transition time
    + transition via crossfade

