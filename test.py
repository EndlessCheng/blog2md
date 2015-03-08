# -*- coding:utf-8 -*-
import blog2md

# b = blog2md.Blog(
# "http://jianyan.me/page/",
# first_page_url="http://jianyan.me/",
#     article_tag='section',
# )
# for article in b.get_all_articles():
#     blog2md.article_to_md(article)
# print u"所有文章已下载完毕"
# print ""
#
# b2 = blog2md.Blog(
#     "https://www.byvoid.com/blog/page/",
#     article_class='post hentry clearfix',
#     title_class='post_header_link',
# )
# for article in b2.get_all_articles():
#     blog2md.article_to_md(article)
# print u"所有文章已下载完毕"
# print ""
#
# # b3 = blog2md.Blog(
# #     "https://blog.cee.moe/page/",
# #     verify=False,
# # )
# # for article in b3.get_all_articles():
# #     blog2md.article_to_md(article)
# # print ""
#
# b4 = blog2md.Blog(
#     "http://www.wdk.pw/page/",
#     start_page=16,
# )
# for article in b4.get_all_articles():
#     blog2md.article_to_md(article)
# print ""
#
# b5 = blog2md.Blog(
#     "http://www.cnblogs.com/chujian123/default.html?page=",
#     article_tag='div',
# )
# for index, article in enumerate(b5.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""

# b6 = blog2md.Blog(
#     "http://blog.csdn.net/wxg694175346/article/list/",
#     article_tag='span',
#     article_class='link_title',
# )
# for index, article in enumerate(b6.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""

# b7 = blog2md.Blog(
#     "http://www.xysay.com/page/",
#     article_tag='h2',
#     article_class='h1',
# )
# for index, article in enumerate(b7.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""

# b8 = blog2md.Blog(
#     "http://www.findspace.name/page/",
#     start_page=14,
# )
# for index, article in enumerate(b8.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""

# b9 = blog2md.Blog(
#     "http://mindhacks.cn/page/",
#     article_tag='div',
#     article_class='entry-thumbnails',
#     start_page=1
# )
# for index, article in enumerate(b9.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""

b10 = blog2md.Blog(
    "http://yuguo.us/",
    article_tag='p',
    url_with_page=False
)
for index, article in enumerate(b10.get_all_articles(), 1):
    print index,
    extract_pair_list = [
        ('p', 'previous-next-nav'),
    ]
    blog2md.article_to_md(*article, article_class='single-post', extract_pair_list=extract_pair_list)
print ""

# b11 = blog2md.Blog(
#     "https://blog.phoenixlzx.com/page/",
#     first_page_url='https://blog.phoenixlzx.com/',
#     article_tag='h1',
#     article_class='title',
# )
# for index, article in enumerate(b11.get_all_articles(), 1):
#     print index,
#     blog2md.article_to_md(article)
# print ""