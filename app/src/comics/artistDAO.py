# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
import sys

class ArtistDAO:

    # constructor for the class
    def __init__(self, database):
        self.db = database
        self.artists = database.artists

    def get_artists(self):
        cursor = self.artists.find()
        l = []
        for artist in cursor:
            l.append({'name':artist['name'], '_id':artist['_id']})
        return l

    def get_artist(self, artist_id):
        artist = self.artists.find_one({"_id": ObjectId(artist_id)})
        return artist

    def insert_entry(self, artist_name):
        print("inserting artist entry", artist_name)

        artist = {"name": artist_name}

        # now insert the post
        try:
            result = self.artists.insert_one(artist)
            print("Matching artist: ", result.matched_count)
            print("Modified artist: ", result.modified_count)
        except:
            print("Error inserting artist")
            print("Unexpected error:", sys.exc_info())
        
    def update_entry(self, artist_id, artist_name):
        print("upserting artist entry", artist_name)

        filter_doc = {"_id": ObjectId(artist_id)}
        artist = { "$set": {"name": artist_name}}

        # now insert the post
        try:
            result = self.artists.update_one(filter_doc, artist)
            print("Modified artist: ", result.modified_count)
        except:
            print("Error inserting artist")
            print("Unexpected error:", sys.exc_info())
