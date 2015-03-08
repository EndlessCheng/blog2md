# -*- coding: utf-8 -*-
__author__ = 'Endless'
__version__ = '2.0.0'

import urlparse
from bs4 import BeautifulSoup
import requests
from html2text import html2text

import os
import platform
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

INVALID_CHAR_LIST = '\\/:*?"<>|\r\n'
HEADERS = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
}
COMMON_EXTRACT_PAIR_LIST = [
    ('div', 'article_manage'),
    ('div', 'related-posts'),
    ('div', 'relatedposts'),
    ('section', 'related-post'),
    ('div', 'author_info'),
    ('div', 'navigation'),
    ('ul', 'article_next_prev'),
    ('li', 'comment-count'),
    ('td', 'gutter'),

    ('img', 'code_img_closed'),
    ('img', 'code_img_opened'),
    ('span', 'cnblogs_code_collapse'),

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

session = requests.session()


def get_valid_file_name(file_name):
    # file_name = file_name.translate(None, INVALID_CHAR_LIST)
    for c in INVALID_CHAR_LIST:
        file_name = file_name.replace(c, "")
    return file_name


def get_article_text(article_soup, article_tag='div', article_class=None, extract_pair_list=None):
    if article_class is None:
        article_content = article_soup.find(article_tag)
    else:
        article_content = article_soup.find(article_tag, class_=article_class) or article_soup.find(article_tag,
                                                                                                id=article_class)
    if article_content is None:
        raise u"未找到正文，请确认填写是否正确（如 '-', '_'）"
    extract_pair_list = extract_pair_list or []
    extract_pair_list.extend(COMMON_EXTRACT_PAIR_LIST)
    for tag, class_ in extract_pair_list:
        extract_list = article_content.find_all(tag, class_=class_)
        for extract in extract_list:
            extract.extract()
        extract_list = article_content.find_all(tag, id=class_)
        for extract in extract_list:
            extract.extract()
    # print article
    article_soup.body.extract()
    article_soup.head.insert_after(article_soup.new_tag('body'))
    article_soup.body.append(article_content)
    # print article_soup
    return article_soup


def article_to_md(article_soup, url, article_tag='div', article_class=None, extract_pair_list=None):
    dir_path = os.path.join(os.getcwd(), "markdown")  # or name it by self.url
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    article_title = get_valid_file_name(article_soup.title.string.encode('utf-8')) + ".md"
    if platform.system() == 'Windows':
        article_title = article_title.encode('gbk')
    # print article_title.decode('gbk')
    file_path = os.path.join(dir_path, article_title)
    extract_pair_list = extract_pair_list or []
    md_text = html2text(get_article_text(article_soup, article_tag=article_tag, article_class=article_class,
                                         extract_pair_list=extract_pair_list).decode('utf-8'))
    f = open(file_path, 'w')
    f.write(md_text)

    if platform.system() == 'Windows':
        f.write("#### 原文：[%s](%s)" % (url, url))

    f.close()

    print u"" + file_path.decode('gbk')


# def article_url_to_md(url, article_tag='div', article_class='post-content', verify=True, extract_pair_list=None):
# soup = BeautifulSoup(session.get(url, headers=HEADERS, verify=verify).content)
# extract_pair_list = extract_pair_list or []
# article_to_md(soup, url, article_tag=article_tag, article_class=article_class, extract_pair_list=extract_pair_list)


class Blog:
    def __init__(self, url, first_page_url=None, start_page=1, url_with_page=True, article_tag='article',
                 article_class=None, title_tag='a', title_class=None, verify=True):

        url_parse = urlparse.urlparse(url)
        self.netloc = url_parse.netloc
        self.site_name = url_parse.scheme + '://' + url_parse.netloc
        self.url = url
        self.first_page_url = first_page_url
        self.start_page = start_page
        self.url_with_page = url_with_page
        self.article_tag = article_tag
        self.article_class = article_class
        self.title_tag = title_tag
        self.title_class = title_class
        self.verify = verify

    def get_all_article_head_soup(self, url):
        if not self.is_valid_url(url):
            return
        print u""
        print u"正在打开 %s" % url
        s = session.get(url, headers=HEADERS, verify=self.verify)
        s.raise_for_status()
        soup = BeautifulSoup(s.content)  # Verify the SSL certificate?
        # print soup
        if self.article_class is None:
            article_head_soup_list = soup.find_all(self.article_tag)
        else:
            article_head_soup_list = soup.find_all(self.article_tag, class_=self.article_class)
        # print self.article_tag, self.article_class
        if not article_head_soup_list:
            return
        # print len(article_head_soup_list)
        return article_head_soup_list

    def is_valid_url(self, url):
        return url is not None and urlparse.urlparse(url).netloc == self.netloc

    def get_all_articles(self):
        try:
            if self.url_with_page:
                start_page = self.start_page
                url_set = set()
                while True:
                    if start_page == 1 and self.first_page_url is not None:
                        article_head_soup_list = self.get_all_article_head_soup(self.first_page_url)
                    else:
                        article_head_soup_list = self.get_all_article_head_soup(self.url + str(start_page))
                    if article_head_soup_list is None:
                        print u"所有文章已下载完毕"
                        return
                    for article_head_soup in article_head_soup_list:
                        article_url = self.get_article_url(article_head_soup)
                        if not self.is_valid_url(article_url):
                            continue

                        if article_url in url_set:
                            print u"所有文章已下载完毕"
                            return
                        url_set.add(article_url)

                        print u""
                        print u"解析 %s" % article_url

                        s = session.get(article_url, headers=HEADERS, verify=self.verify)
                        s.raise_for_status()
                        article_soup = BeautifulSoup(s.content)
                        yield (article_soup, article_url)
                    start_page += 1
            else:
                article_head_soup_list = self.get_all_article_head_soup(self.url)
                if article_head_soup_list is None:
                    print u"所有文章已下载完毕"
                    return
                for article_head_soup in article_head_soup_list:
                    article_url = self.get_article_url(article_head_soup)
                    if not self.is_valid_url(article_url):
                        continue

                    print u""
                    print u"解析 %s" % article_url

                    s = session.get(article_url, headers=HEADERS, verify=self.verify)
                    s.raise_for_status()
                    article_soup = BeautifulSoup(s.content)
                    yield (article_soup, article_url)
        except requests.HTTPError:
            print u"所有文章已下载完毕"
            return
        except requests.ConnectionError:
            print u"网络异常，解析中断"
            return

    def get_title_soup(self, soup):
        if self.title_class is None:
            title_soup = soup.find(self.title_tag)
        else:
            title_soup = soup.find(self.title_tag, class_=self.title_class)
        return title_soup

    def get_article_title(self, article_soup):
        title_soup = self.get_title_soup(article_soup)
        # print title_soup
        if title_soup is None:
            return u"未找到 <%s>" % self.title_tag
        if title_soup.has_attr('title'):
            return title_soup['title']
        return title_soup.string

    def get_article_description(self, article_soup):
        pass

    def get_article_url(self, article_head_soup):
        title_soup = self.get_title_soup(article_head_soup)
        if title_soup is None:
            return
        if title_soup.has_attr('href'):
            if urlparse.urlparse(title_soup['href']).scheme == '':  # not begin with 'http://' or 'https://'
                return urlparse.urljoin(self.site_name, title_soup['href'])
            return title_soup['href']
        raise u"Error @ get_article_url()"