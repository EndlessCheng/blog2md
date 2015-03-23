# -*- coding: utf-8 -*-
__author__ = 'EndlessCheng'
__version__ = '2.1.0'

import urlparse
from bs4 import BeautifulSoup
import requests
from html2text import html2text

from datetime import datetime
from dateutil import parser, tz
import os
import platform
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

_INVALID_CHAR_LIST = '\\/:*?"<>|\r\n'
_HEADERS = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
}
_COMMON_EXTRACT_PAIR_LIST = [
    ('div', 'article_manage'),
    ('div', 'related-posts'),
    ('div', 'relatedposts'),
    ('section', 'related-post'),
    ('div', 'author_info'),
    ('div', 'navigation'),
    ('ul', 'article_next_prev'),
    ('li', 'comment-count'),
    ('td', 'gutter'),
    ('div', 'toc-article'),  # Contents
    ('div', 'toc'),  # Contents
    ('div', 'article-tags'),
    ('p', 'article-author'),
    ('p', 'article-time'),
    ('a', 'post_header_link'),
    ('span', 'post-meta'),

    ('img', 'code_img_closed'),
    ('img', 'code_img_opened'),  # cnblogs
    ('span', 'cnblogs_code_collapse'),

    ('div', 'loc_link'),
    ('p', 'previous-next-nav'),
    ('div', 'about-author clearfix'),
    ('nav', 'article-nav clearfix'),
    ('div', 'jiathis_style'),
    ('div', 'digg'),
    ('p', 'postfoot'),
    ('noscript', ''),
    ('div', 'ds-ssr'),
    ('a', 'dsq-brlink'),  # Disqus
    # ('p', 'copyright'),
]

_session = requests.session()


def _get_soup(url, verify=True):
    s = _session.get(url, headers=_HEADERS, verify=verify)  # Verify the SSL certificate
    s.raise_for_status()  # FIXME: add try-except block here.
    return BeautifulSoup(s.content)


def _get_valid_file_name(file_name):
    # file_name = file_name.translate(None, INVALID_CHAR_LIST)
    for c in _INVALID_CHAR_LIST:
        file_name = file_name.replace(c, "")
    return file_name


class Blog:
    def __init__(self, url, first_page_url=None, start_page=1, is_single_page=False, verify=True,
                 entry_tag='article', entry_class=None, entry_title_tag='a', entry_title_class=None,
                 description_tag=None, description_class=None):
        """
        :param first_page_url: set this when he first page return 404 and the home page isn't the netloc
        """
        url_parse = urlparse.urlparse(url)
        self.netloc = url_parse.netloc
        self.site_name = url_parse.scheme + '://' + url_parse.netloc
        self.url = url
        self.first_page_url = first_page_url
        self.start_page = start_page
        self.is_single_page = is_single_page
        self.verify = verify

        self.entry_tag = entry_tag
        self.entry_class = entry_class
        self.entry_title_tag = entry_title_tag
        self.entry_title_class = entry_title_class
        self.description_tag = description_tag
        self.description_class = description_class

    def _get_page_url(self, start_page):
        if self.is_single_page:
            return self.url
        if start_page == 1 and self.first_page_url is not None:
            return self.first_page_url
        return self.url + str(start_page)

    def _get_all_entry_soup(self, url):
        print u""
        print u"正在打开 %s" % url
        soup = _get_soup(url, self.verify)
        return soup.find_all(self.entry_tag) if self.entry_class is None else soup.find_all(self.entry_tag,
                                                                                            class_=self.entry_class)

    def _get_article_url_and_title(self, entry_soup):
        entry_title_soup = entry_soup.find(self.entry_title_tag)
        if self.entry_title_tag != 'a':
            entry_title_soup = entry_title_soup.a  # get the first <a>
        article_url = entry_title_soup['href']
        if urlparse.urlparse(article_url).scheme == '':  # article_url isn't begin with 'http://' or 'https://'
            article_url = urlparse.urljoin(self.site_name, article_url)
        if entry_title_soup.has_attr('title'):
            article_name = entry_title_soup['title']
        else:
            article_name = "".join(list(entry_title_soup.stripped_strings))
            if article_name == "":  # get next tag
                article_name = "".join(list(entry_soup.next_sibling.stripped_strings))
        return article_url, _get_valid_file_name(article_name)

    def _get_article_description(self, entry_soup):
        if self.description_tag is None and self.description_class is None:
            return ""
        return entry_soup.find(self.description_tag).string

    def get_all_articles(self):
        try:
            start_page = self.start_page
            url_set = set()
            while start_page:
                url = self._get_page_url(start_page)
                entry_soup_list = self._get_all_entry_soup(url)
                if not entry_soup_list:
                    print u"所有文章已下载完毕"
                    return
                for entry_soup in entry_soup_list:
                    (article_url, article_title) = self._get_article_url_and_title(entry_soup)

                    if article_url in url_set:  # This happens when we reach end_page+1 page in some blogs.
                        print u"所有文章已下载完毕"
                        return
                    url_set.add(article_url)

                    print u""
                    print u"解析 %s" % article_url
                    yield Article(article_url, verify=self.verify, title=article_title,
                                  description=self._get_article_description(entry_soup))
                if self.is_single_page:
                    return
                start_page += 1
        except requests.HTTPError:
            print u"所有文章已下载完毕"
        except requests.ConnectionError:
            print u"网络异常，解析中断"


class Article:
    def __init__(self, url, verify=True, title=None, description=""):
        url_parse = urlparse.urlparse(url)
        self.netloc = url_parse.netloc
        self.url = url
        self.soup = _get_soup(url, verify)
        self.title = title
        self.description = description

    def _get_file_name(self, title_class, title_extract_tag):
        """
        Happens when title is None.

        :return: file_name
        """
        if title_class is None:
            file_name = self.soup.title.string
        else:
            title_soup = self.soup.find(class_=title_class).a or self.soup.find(id=title_class).a
            if title_extract_tag is not None:
                title_extract_soup = title_soup.find(title_extract_tag)
                if title_extract_soup is not None:
                    title_extract_soup.extract()
            file_name = title_soup.stripped_strings.next()  # clear blank chars
        file_name = _get_valid_file_name(file_name)
        return file_name

    def _get_date(self, time_class, time_attr):
        """
        return now() when can't find date

        :return: date
        """
        if time_class is None:
            time_soup = self.soup.find(datetime=True)
            if time_soup is None:
                return str(datetime.now())
            return time_soup['datetime']
        time_soup = self.soup.find(class_=time_class) or self.soup.find(id=time_class)
        if time_attr is None:
            return " ".join(list(time_soup.stripped_strings))
        return time_soup[time_attr]

    def _get_hexo_date(self, *args):
        date = parser.parse(self._get_date(*args))
        if date.tzname():
            date = date.astimezone(tz.tzlocal())
        return date.strftime('%Y-%m-%d %H:%M:%S')

    def _get_hexo_head(self, title, time_class, time_attr, tag_class):
        head = "title: %s\n\n" % title
        head += "date: %s\n\n" % self._get_hexo_date(time_class, time_attr)
        head += "tags: ["
        tags_soup = self.soup.find(class_=tag_class) or self.soup.find(id=tag_class)
        if tags_soup is not None:
            for tag in tags_soup.find_all('a'):
                if tag.string:  # some blogs have empty <a> in tags list...
                    head += tag.string + ", "
        head += "]\n\n"
        head += "description: %s\n\n---\n" % self.description
        return head

    def _get_content_soup(self, content_tag, content_class, extract_pair_list):
        article_content_soup = self.soup.find(content_tag, class_=content_class) or self.soup.find(content_tag,
                                                                                                   id=content_class)
        if article_content_soup is None:
            raise u"未找到正文，请确认填写是否正确（如 '-', '_'）"
        article_content_soup = BeautifulSoup(article_content_soup.encode())

        extract_pair_list = extract_pair_list or []
        extract_pair_list.extend(_COMMON_EXTRACT_PAIR_LIST)
        for tag, class_ in extract_pair_list:
            extract_list = article_content_soup.find_all(tag, class_=class_)
            for extract in extract_list:
                extract.extract()
            extract_list = article_content_soup.find_all(tag, id=class_)
            for extract in extract_list:
                extract.extract()

        final_soup = BeautifulSoup(self.soup.encode())
        final_soup.body.replace_with(article_content_soup)
        return final_soup

    def _to_md(self, content_soup, title_class, title_extract_tag, time_class=None, time_attr=None, tag_class=None):
        """
        Must use 'gbk' on file path on Windows

        """
        dir_path = os.path.join(os.getcwd(), self.netloc)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        file_name = self.title if self.title is not None else self._get_file_name(title_class, title_extract_tag)
        # print file_name
        file_path = os.path.join(dir_path, file_name.encode('gbk') + ".md")  # if platform.system() == 'Windows':
        f = open(file_path, 'w')
        if tag_class is None:
            f.write("#  %s\n---\n\n" % file_name)
        else:
            f.write(self._get_hexo_head(file_name, time_class, time_attr, tag_class))
        md_text = html2text(content_soup.encode())
        f.write(md_text)
        if tag_class is None:
            f.write("#### 原文：[%s](%s)" % (self.url, self.url))
        f.close()
        print u"" + file_path.decode('gbk')

    def to_simple_md(self, content_tag='div', content_class=None, extract_pair_list=None,
                     title_class=None, title_extract_tag=None):
        """
        :param title_extract_tag: extract some tags like "[TOP]" in CSDN
        :return: None
        """
        self._to_md(self._get_content_soup(content_tag, content_class, extract_pair_list),
                    title_class, title_extract_tag)

    def to_hexo(self, content_tag='div', content_class=None, extract_pair_list=None,
                title_class=None, title_extract_tag=None, time_class=None, time_attr=None, tag_class='tags'):
        """
        :param title_extract_tag: extract some tags like "[TOP]" in CSDN
        :return: None
        """
        self._to_md(self._get_content_soup(content_tag, content_class, extract_pair_list),
                    title_class, title_extract_tag, time_class, time_attr, tag_class)