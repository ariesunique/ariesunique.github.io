import sys
from datetime import datetime

TEMPLATE_LONG = """
{hashes}
{title}
{hashes}

:date: {year}-{month:02d}-{day:02d} {hour}:{minute:02d}
:tags:
:category: blog
:slug: {slug}
:summary: This is the summary.

.. role:: text-primary
.. role:: text-warning
.. role:: lead

.. |br| raw:: html

       <br />
       
:lead:`Write something interesting here to get reader's attention`

.. contents::

{equals}
This is a header
{equals}

Write your content here.

"""


TEMPLATE_SHORT = """
{hashes}
{title}
{hashes}

:date: {year}-{month:02d}-{day:02d} {hour}:{minute:02d}
:tags:
:category: blog
:slug: {slug}
:summary: This is the summary.

Write your content here.

"""




def make_entry(title, articletype="short"):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug)
    template = TEMPLATE_SHORT if articletype == "short" else TEMPLATE_LONG
    t = template.strip().format(title=title,
                                hashes='#' * len(title),
                                equals="="*25,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        title = sys.argv[1]
        articletype = "short"
        if len(sys.argv) > 2:
            articletype = "long" if sys.argv[2] == "long" else "short"
        make_entry(title, articletype)
    else:
        print("Please provide a title and optionally the article type (long or short - short is default.)")
        