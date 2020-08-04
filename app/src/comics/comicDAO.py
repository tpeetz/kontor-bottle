# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
import sys

class ComicDAO:

    # constructor for the class
    def __init__(self, database):
        self.db = database
        self.comics = database.comics

    def get_comics(self):
        cursor = self.comics.find()
        l = []
        for comic in cursor:
            l.append({'title':comic['title'], 
                      '_id':comic['_id'], 
                      'current_order':comic['current_order'], 
                      'completed':comic['completed']})
        return l

    def get_comic(self, comic_id):
        comic = self.comics.find_one({"_id": ObjectId(comic_id)})
        return comic

    def insert_entry(self, comic_title, comic_publisher=None, comic_order=False, comic_completed=False):
        print("inserting comic entry", comic_title)

        comic = {"title": comic_title, "current_order": comic_order, "completed": comic_completed}

        # now insert the comic
        try:
            result = self.comics.insert_one(comic)
            print("Modified comic: ", result.modified_count)
        except:
            print("Error inserting comic")
            print("Unexpected error:", sys.exc_info())
        
    def update_entry(self, comic_id, comic_title, comic_publisher=None, comic_order=False, comic_completed=False):
        print("upserting comic entry", comic_title)

        filter_doc = {"_id": ObjectId(comic_id)}
        comic = { "$set": {"title": comic_title, 'current_order': comic_order, 'completed': comic_completed}}

        # now insert the post
        try:
            result = self.comics.update_one(filter_doc, comic)
            print("Matching comic: ", result.matched_count)
            print("Modified comic: ", result.modified_count)
        except:
            print("Error inserting comic")
            print("Unexpected error:", sys.exc_info())