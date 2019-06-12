import sys
from datetime import datetime

TEMPLATE = """
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


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='=' * len(title),
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
        make_entry(sys.argv[1])
    else:
        print("No title given")
        