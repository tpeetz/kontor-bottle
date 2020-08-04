# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
import sys

class PublisherDAO:

    # constructor for the class
    def __init__(self, database):
        self.db = database
        self.publishers = database.publishers

    def get_publishers(self):
        cursor = self.publishers.find()
        l = []
        for publisher in cursor:
            l.append({'name':publisher['name'], '_id':publisher['_id']})
        return l

    def get_publisher(self, publisher_id):
        publisher = self.publishers.find_one({"_id": ObjectId(publisher_id)})
        return publisher

    def insert_entry(self, publisher_name):
        print("inserting publisher entry", publisher_name)

        publisher = {"name": publisher_name}

        # now insert the post
        try:
            result = self.publishers.insert_one(publisher)
            print("Matching publisher: ", result.matched_count)
            print("Modified publisher: ", result.modified_count)
        except:
            print("Error inserting publisher")
            print("Unexpected error:", sys.exc_info())
        
    def update_entry(self, publisher_id, publisher_name):
        print("upserting publisher entry", publisher_name)

        filter_doc = {"_id": ObjectId(publisher_id)}
        publisher = { "$set": {"name": publisher_name}}

        # now insert the post
        try:
            result = self.publishers.update_one(filter_doc, publisher)
            print("Modified publisher: ", result.modified_count)
        except:
            print("Error inserting publisher")
            print("Unexpected error:", sys.exc_info())
