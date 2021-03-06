import json
import Queue
import api.errors as api_errors

from urllib2 import HTTPError

from django.core.cache import cache
from api.errors import APIException
from api.handlers.handlers import BaseHandler, BaseObjectHandler
from api.utils import process_latlon, process_boolean, process_integer
from place.models import FoursquarePlace


class PlaceFoursquareHandler(BaseHandler):
    allowed_methods = ('GET',)
    required_fields_for_read = ('latlon',)
    read_kwargs = required_fields_for_read + ('q', 'radius', 'location', 'force_update_cache', 'section')
    read_auth_exempt = True

    def read_validate(self, query_dict, **kwargs):
        query_dict['q'] = query_dict.get('q', '')
        process_boolean(query_dict, ['force_update_cache'])
        lat, lon = process_latlon(query_dict['latlon'])
        process_integer(query_dict, ['radius'])
        query_dict['lat'] = lat
        query_dict['lon'] = lon
        query_dict['radius'] = query_dict.get('radius', 100000) # In kilometer
        query_dict['location'] = query_dict.get('location')
        query_dict['section'] = query_dict.get('section', '')

    def read(self, request):
        lat = request.CLEANED['lat']
        lon = request.CLEANED['lon']
        radius = request.CLEANED['radius']
        location = request.CLEANED['location']
        section = request.CLEANED['section']
        force_update_cache = request.CLEANED.get('force_update_cache')
        q = request.CLEANED['q']

        rounded_latlon = "%s,%s" % (round(float(lat),4), round(float(lon),4))
        version = '1'
        cache_key = 'fsplace_'+rounded_latlon+section+'_'+q+version+str(radius)
        if not cache.get(cache_key) or force_update_cache:
            results = FoursquarePlace.objects.spatial_search(rounded_latlon, q, section=section, radius=radius)
            cache.set(cache_key, results, 3600)

        results = cache.get(cache_key)

        if section and section!="topPicks":
            results = filter(lambda x: x.section==section, results)
        return [result.to_json(request=request) for result in results]


class PlaceFoursquareSearchHandler(BaseHandler):
    allowed_methods = ('GET',)
    read_kwargs = ('q', 'section', 'sw', 'ne')
    read_auth_exempt = True

    def read_validate(self, query_dict, **kwargs):
        query_dict['q'] = query_dict.get('q', '')
        
        if not query_dict.get('sw') or not query_dict.get('ne'):
            raise api_errors.APIException(api_errors.ERROR_GENERAL_BAD_SIGNATURE)
        
        query_dict['section'] = query_dict.get('section', '')

    def read(self, request):
        # TODO: latlon and radius

        sw = request.CLEANED.get('sw')
        ne = request.CLEANED.get('ne')
        q = request.CLEANED['q']

        version = '1'

        if sw and ne:
            results = FoursquarePlace.objects.square_search(sw=sw, ne=ne, q=q)

        return [result.to_json(request=request) for result in results]



class PlaceFoursquareObjectHandler(BaseObjectHandler):
    query_model = FoursquarePlace
    allowed_methods = ('GET',)
    read_auth_exempt = True


class PlaceFoursquarePhotoHandler(BaseHandler):
    allowed_methods = ('GET',)
    read_auth_exempt = True

    def read_validate(self, query_dict, fs_id, **kwargs):
        pass

    def read(self, request, fs_id):
        limit = request.CLEANED['limit']
        return FoursquarePlace.objects.get_photos(fs_id, limit=limit)


