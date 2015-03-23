# blog2md
Translate your blog articles to markdown files!

# How to use
```python
import blog2md

my_blog = blog2md.Blog(
    "http://blog.csdn.net/synapse7/article/list/",
    entry_tag='span',
    entry_class='link_title',
)
for article in my_blog.get_all_articles():
    article.to_hexo(
        content_class='article_content',
        time_class='link_postdate',
        tag_class='tag2box',
    )
```

Result:

![](http://endless.qiniudn.com/blogblod2md4.png)

See [test.py](https://github.com/EndlessCheng/blog2md/blob/master/test.py) for more details.

# Notice
There is a BUG in `html2text/config.py`:

```python
# Wrap long lines at position. 0 for no wrapping. (Requires Python 2.3.)
BODY_WIDTH = 78
```

Change 78 to 0 to disable wrapping before you run.
