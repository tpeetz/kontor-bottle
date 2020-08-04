# -*- coding: utf-8 -*-
from mongoengine import connect, Document
from mongoengine import StringField, BooleanField
from mongoengine import ListField, ReferenceField, GenericReferenceField
import pprint


class Publisher(Document):
    name = StringField(required=True)

    def __str__(self):
        s = "Publisher(%s)" % self.name
        return s


class Artist(Document):
    name = StringField(required=True)
    className = StringField()

    def __str__(self):
        s = "Artist(%s)" % self.name
        return s


class Issue(Document):
    number = StringField()
    comic = GenericReferenceField()
    is_read = BooleanField(default=False)
    is_stock = BooleanField(default=False)

    def __str__(self):
        s = "Issue(%s # %s, %s)" % (self.comic.title, self.number, self.is_read)
        return s


class StoryArc(Document):
    name = StringField(required=True)
    comic = GenericReferenceField()
    issues = ListField(ReferenceField(Issue))

    def __str__(self):
        s = "StoryArc(%s, %s)" % (self.name, self.comic.title)
        return s


class Volume(Document):
    name = StringField(required=True)
    comic = GenericReferenceField()
    issues = ListField(ReferenceField(Issue))

    def __str__(self):
        s = "Volume(%s, %s, %s)" % (self.id, self.name, self.comic.title)
        return s


class Comic(Document):
    title = StringField(required=True)
    publisher = ReferenceField(Publisher)
    current_order = BooleanField()
    completed = BooleanField()
    issues = ListField(ReferenceField(Issue))
    stories = ListField(ReferenceField(StoryArc))

    def __str__(self):
        if self.publisher is None:
            s = "Comic(%s, %s, %s, %s)" % (self.title, self.publisher, self.current_order, self.completed)
            return s
        else:
            s = "Comic(%s, %s, %s, %s)" % (
                self.title, self.publisher.name, self.current_order, self.completed)
            return s


class TradePaperback(Document):
    comic = ReferenceField(Comic)
    issue_start = StringField()
    issue_end = StringField()

    def __str__(self):
        s = "TPB(%s)" % self.comic.title
        return s


def get_publisher(name):
    publisher = Publisher.objects(name=name)
    if publisher.count() > 0:
        return publisher[0]
    else:
        return None


def get_comic(title):
    comic = Comic.objects(title=title)
    if comic.count() > 0:
        return comic[0]
    else:
        return None


def get_issue(title, number):
    comic = get_comic(title)
    issues = Issue.objects(number=number, comic=comic)
    if issues.count() > 0:
        return issues[0]
    else:
        return None

if __name__ == '__main__':
    connect('comics')
    for publisher in Publisher.objects:
        pprint.pprint(publisher)
    for artist in Artist.objects:
        pprint.pprint(artist)
    for comic in Comic.objects:
        pprint.pprint(comic)
    for issue in Issue.objects:
        pprint.pprint(issue)
    for story in StoryArc.objects:
        pprint.pprint(story)
    for tpb in TradePaperback.objects:
        pprint.pprint(tpb)
