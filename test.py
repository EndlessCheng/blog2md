# -*- coding:utf-8 -*-
import blog2md

b = blog2md.Blog(
    "http://jianyan.me/page/",
    first_page_url="http://jianyan.me/",
    entry_tag='section',
    entry_class='post',
    description_tag='p',
)
for index, article in enumerate(b.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='article-content',
        tag_class='article-tags',
    )
print ""

b2 = blog2md.Blog(
    "https://www.byvoid.com/blog/page/",
    entry_tag='section',
    entry_class='entry-body entry-body-content',
)
for index, article in enumerate(b2.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_tag='section',
        content_class='entry-body entry-body-content',
        tag_class='entry-meta',
    )
print ""

# FIXME: test verify
# b3 = blog2md.Blog(
#     "https://blog.cee.moe/page/",
#     verify=False,
# )
# for index, article in b3.get_all_articles():
#     print index,
#     article.to_hexo(
#
#     )
# print ""

b4 = blog2md.Blog(
    "http://www.wdk.pw/page/",
)
for index, article in enumerate(b4.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='post-content',
    )
print ""

b5 = blog2md.Blog(
    "http://www.cnblogs.com/chujian123/default.html?page=",
    entry_tag='div',
    entry_class='post',
)
for index, article in enumerate(b5.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='cnblogs_post_body',
        time_class='post-date',
        tag_class='EntryTag',
    )
print ""

b6 = blog2md.Blog(
    "http://blog.csdn.net/synapse7/article/list/",
    entry_tag='span',
    entry_class='link_title',
)
for index, article in enumerate(b6.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='article_content',
        time_class='link_postdate',
        tag_class='tag2box',
    )
print ""

# FIXME: 乱码？？？
# b7 = blog2md.Blog(
#     "http://www.findspace.name/page/",
#     entry_tag='h2',
#     entry_class='title',
# )
# for index, article in enumerate(b7.get_all_articles(), 1):
#     print index,
#     article.to_hexo(
#         content_class='post-single-content box mark-links',
#     )
# print ""

b8 = blog2md.Blog(
    "http://mindhacks.cn/page/",
    entry_tag='div',
    entry_class='entry-thumbnails',
)
for index, article in enumerate(b8.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='entry-content clearfix',
        time_class='published',
        time_attr='title',
    )
print ""

b9 = blog2md.Blog(
    "http://yuguo.us/",
    entry_tag='p',
    is_single_page=True,
)
for index, article in enumerate(b9.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='single-post',
    )
print ""

b10 = blog2md.Blog(
    "https://blog.phoenixlzx.com/page/",
    first_page_url='https://blog.phoenixlzx.com/',
    entry_tag='h1',
    entry_class='title',
)
for index, article in enumerate(b10.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='entry',
    )
print ""

b11 = blog2md.Blog(
    "http://blog.daimajia.com/page/",
    entry_tag='h1',
    entry_class='entry-title',
)
for index, article in enumerate(b11.get_all_articles(), 1):
    print index,
    article.to_hexo(
        content_class='entry-content',
    )
print ""