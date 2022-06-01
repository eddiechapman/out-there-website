# out-there-website

A website for Out There, a Milwaukee outdoor experimental music series.

## Usage

Development:

```
source venv/bin/activate
pelican -t theme --autoreload --listen content
```

## Planning

Going to be a Pelican static site.

### Examples

- (Experimental Sound Studio)[https://ess.org]
- (Elastic Arts)[https://elasticarts.org/]

### Domains

Searched on (GoDaddy)[https://www.godaddy.com]

- out-there-milwaukee.com
- outtheremilwaukee.com
- out-there-experimental.com
- out-there-experimental.art
- out-there-experimental.info
- out-there-arts.com
- out-there.info
- out-there-series.com
- outthereseries.com

### Hosting

- (Heroku)[https://www.heroku.com/]
- (Netlify)[https://www.netlify.com/]
    + (Tutorial 1)[https://alone-djangonaut.com/how-to-create-a-website-using-pelican-and-netlify-january-2021]
    + (Tutorial 2)[https://frankcorso.dev/deploying-your-pelican-static-site-to-netlify.html]

### Plugins 

- (Events)[https://github.com/getpelican/pelican-plugins/tree/master/events]
- (Pelican YouTube)[https://github.com/kura/pelican_youtube]
- (Photos)[https://github.com/pelican-plugins/photos]

### Site layout

- news
- gallery
- about
- contact
- calendar

## Development

Run the following command to process content, serve on localhost, and autoreload upon updates:

```
pelican -t theme --autoreload --listen content
```