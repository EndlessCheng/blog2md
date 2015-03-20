# blog2md
Translate your blog articles to markdown files!

# How to use
See [test.py](https://github.com/EndlessCheng/blog2md/blob/master/test.py) for more details.

# Notice
There is a BUG in `html2text/config.py`:

```python
# Wrap long lines at position. 0 for no wrapping. (Requires Python 2.3.)
BODY_WIDTH = 78
```

Change 78 to 0 to disable wrapping before you run.
