# -*- coding:utf-8 -*-
import pymongo
import comics.publisherDAO
import comics.artistDAO
import comics.comicDAO
import bottle
import cgi


__author__ = 'tpeetz'


class Plugin:

    def __init__(self, app, database, sessions):
        self.app = app
        self.db = database
        self.sessions = sessions
        self.publishers = publisherDAO.PublisherDAO(database)
        self.artists = artistDAO.ArtistDAO(database)
        self.comics = comicDAO.ComicDAO(database)
        self.routing()


    def routing(self):
        self.app.route('/comics/', 'GET', self.comic_index)
        self.app.route('/comics/comic', 'GET', self.comic_list)
        self.app.route('/comics/comic/<id>', 'GET', self.comic_details)
        self.app.route('/comics/comic/create', 'GET', self.get_comic_create)
        self.app.route('/comics/comic/create', 'POST', self.post_create_comic)
        self.app.route('/comics/publisher', 'GET', self.publisher_list)
        self.app.route('/comics/publisher/<id>', 'GET', self.publisher_details)
        self.app.route('/comics/publisher/create', 'GET', self.get_publisher_create)
        self.app.route('/comics/publisher/create', 'POST', self.post_create_publisher)
        self.app.route('/comics/artist', 'GET', self.artist_list)
        self.app.route('/comics/artist/<id>', 'GET', self.artist_details)
        self.app.route('/comics/artist/create', 'GET', self.get_artist_create)
        self.app.route('/comics/artist/create', 'POST', self.post_create_artist)
        self.app.route('/comics/storyarc', 'GET', self.storyarc_list)
        self.app.route('/comics/storyarc/<id>', 'GET', self.storyarc_details)
        self.app.route('/comics/storyarc/create', 'GET', self.get_storyarc_create)
        self.app.route('/comics/storyarc/create', 'POST', self.post_create_storyarc)

    def comic_index(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        return bottle.template('comic_index', dict(username=username))


    def comic_list(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        l = self.comics.get_comics()
        return bottle.template('comic_list', dict(comics=l, username=username))


    def comic_details(self, id):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        comic = self.comics.get_comic(id)
        errors = ""
        if comic == None:
            errors = "Entry not found"
        return bottle.template('comic_template', dict(title=comic['title'], 
                                                      id=comic['_id'], 
                                                      current_order=comic['current_order'],
                                                      completed=comic['completed'],
                                                      errors="", 
                                                      username=username))


    def get_comic_create(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        return bottle.template("comic_template", dict(title="", 
                                                      id='newentry',
                                                      current_order=False,
                                                      completed=False,
                                                      errors="", 
                                                      username=username))


    def post_create_comic(self):
        comic_id = bottle.request.forms.get("id")
        comic_title = bottle.request.forms.get("title")
        comic_order = bottle.request.forms.get("current_order")
        comic_completed = bottle.request.forms.get("completed")
        if comic_id == "newentry":
            self.comics.insert_entry(comic_title, None, comic_order, comic_completed)
        else:
            self.comics.update_entry(comic_id, comic_title, None, comic_order, comic_completed)
        bottle.redirect("/comics/comic")


    def publisher_list(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        l = self.publishers.get_publishers()
        return bottle.template('publisher_list', dict(publishers=l, username=username))


    def publisher_details(self, id):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        publisher = self.publishers.get_publisher(id)
        errors = ""
        if publisher == None:
            errors= "Entry not found"
        return bottle.template('publisher_template', dict(name=publisher['name'], id=publisher['_id'], errors="", username=username))


    def get_publisher_create(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        return bottle.template("publisher_template", dict(name="", id='newentry', errors="", username=username))


    def post_create_publisher(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        publisher_id = bottle.request.forms.get("id")
        publisher_name = bottle.request.forms.get("name")
        if publisher_id == "newentry":
            self.publishers.insert_entry(publisher_name)
        else:
            self.publishers.update_entry(publisher_id, publisher_name)
        bottle.redirect("/comics/publisher")


    def artist_list(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        l = self.artists.get_artists()
        return bottle.template('artist_list', dict(artists=l, username=username))


    def artist_details(self, id):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        artist = self.artists.get_artist(id)
        errors = ""
        if artist == None:
            errors= "Entry not found"
        return bottle.template('artist_template', dict(name=artist['name'], id=artist['_id'], errors="", username=username))


    def get_artist_create(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        return bottle.template("artist_template", dict(name="", id='newentry', errors="", username=username))


    def post_create_artist(self):
        artist_id = bottle.request.forms.get("id")
        artist_name = bottle.request.forms.get("name")
        if artist_id == "newentry":
            self.artists.insert_entry(artist_name)
        else:
            self.artists.update_entry(artist_id, artist_name)
        bottle.redirect("/comics/artist")


    def storyarc_list(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        l = self.storyarcs.get_storyarcs()
        return bottle.template('storyarc_list', dict(storyarcs=l, username=username))


    def storyarc_details(self, id):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        storyarc = self.storyarcs.get_storyarc(id)
        errors = ""
        if storyarc == None:
            errors = "Entry not found"
        return bottle.template('storyarc_template', dict(title=storyarc['title'], id=storyarc['_id'], errors="", username=username))


    def get_storyarc_create(self):
        cookie = bottle.request.get_cookie("session")
        username = self.sessions.get_username(cookie)
        return bottle.template("storyarc_template", dict(title="", id='newentry', errors="", username=username))


    def post_create_storyarc(self):
        storyarc_id = bottle.request.forms.get("id")
        storyarc_title = bottle.request.forms.get("title")
        if storyarc_id == "newentry":
            self.storyarcs.insert_entry(storyarc_title)
        else:
            self.storyarcs.update_entry(storyarc_id, storyarc_title)
        bottle.redirect("/comics/storyarc")
