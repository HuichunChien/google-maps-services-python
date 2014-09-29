"""Tests for the elevation module."""

import unittest
import datetime
import responses

import googlemaps

class ElevationTest(unittest.TestCase):

    def setUp(self):
        self.key = 'AIzaasdf'
        self.ctx = googlemaps.Context(self.key)

    @responses.activate
    def test_elevation_single(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/elevation/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.elevation(self.ctx, (40.714728, -73.998672))

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/elevation/json?'
                          'locations=40.714728%%2C-73.998672&key=%s' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_elevation_single_list(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/elevation/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = googlemaps.elevation(self.ctx, [(40.714728, -73.998672)])

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/elevation/json?'
                          'locations=40.714728%%2C-73.998672&key=%s' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_elevation_multiple(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/elevation/json',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        locations = [(40.714728, -73.998672), (-34.397, 150.644)]
        results = googlemaps.elevation(self.ctx, locations)

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/elevation/json?'
                          'locations=40.714728%%2C-73.998672%%7C-34.397000%%2C'
                          '150.644000&key=%s' % self.key,
                          responses.calls[0].request.url)

    def test_elevation_along_path_single(self):
        with self.assertRaises(Exception):
          results = googlemaps.elevation_along_path(self.c,
                    [(40.714728, -73.998672)], 5)

    @responses.activate
    def test_elevation_along_path(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/elevation/json',

                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        path = [(40.714728, -73.998672), (-34.397, 150.644)]
        
        results = googlemaps.elevation_along_path(self.ctx, path, 5)

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/elevation/json?'
                          'path=40.714728%%2C-73.998672%%7C-34.397000%%2C150.644000&'
                          'key=%s&samples=5' % self.key,
                          responses.calls[0].request.url)
