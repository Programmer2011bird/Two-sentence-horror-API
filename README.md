# Two Sentence Horror API
An API that scrapes the subreddit r/TwoSentenceHorror and gives the results, includes the new, top and hot tiers and filters

## Endpoints
- `/?content_type=hot` hot and trending horror stories ( default )
- `/?content_type=new` newest stories
- `/?content_type=top` top stories
 - * `&tops_date=today` today top stories ( default )
 - * `&tops_date=thisweek` this week top stories
 - * `&tops_date=thismonth` this month top stories
 - * `&tops_date=thisyear` this year top stories
 - * `&tops_date=alltime` top stories of all time

## How To Use
<ul>
    <li>in your terminal type ` fastapi dev api.py ` for development</li>
    <li>or ` fastapi run api.py ` for production use</li>
</ul>