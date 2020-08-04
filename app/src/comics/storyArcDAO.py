# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
import sys


class StoryArcDAO:
    # constructor for the class
    def __init__(self, database):
        self.db = database
        self.storyarcs = database.storyarcs

    def get_storyarcs(self):
        cursor = self.storyarcs.find()
        l = []
        for storyarc in cursor:
            l.append({'title': storyarc['title'], '_id': storyarc['_id']})
        return l

    def get_storyarc(self, storyarc_id):
        storyarc = self.storyarcs.find_one({"_id": ObjectId(storyarc_id)})
        return storyarc

    def insert_entry(self, storyarc_title):
        print("inserting publisher entry", storyarc_title)

        storyarc = {"name": storyarc_title}

        # now insert the post
        try:
            result = self.storyarcs.insert_one(storyarc)
            print("Matching storyarc: ", result.matched_count)
            print("Modified storyarc: ", result.modified_count)
        except:
            print("Error inserting storyarc")
            print("Unexpected error:", sys.exc_info())

    def update_entry(self, storyarc_id, storyarc_title):
        print("upserting storyarc entry", storyarc_title)

        filter_doc = {"_id": ObjectId(storyarc_id)}
        storyarc = {"$set": {"name": storyarc_title}}

        # now insert the post
        try:
            result = self.storyarcs.update_one(filter_doc, storyarc)
            print("Modified storyarc: ", result.modified_count)
        except:
            print("Error inserting storyarc")
            print("Unexpected error:", sys.exc_info())
