import googlemaps
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
import redis
from django.conf import settings



@api_view(['GET'])
def getPlace(request):
    query = request.query_params.get('query')
    key = settings.GOOGLE_KEY

    if not query:
        return Response({"error": "wrong parameter data"}, status=status.HTTP_400_BAD_REQUEST)
    try:

        gmaps = googlemaps.Client(key)

        places = gmaps.places(query)
        if places['status'] == 'OK':
            result = [places]
            return Response({"places": result}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No places found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def save_place(request):

        try:
            data = json.loads(request.body)

            if data:

                r = redis.StrictRedis(host='redis', port=6379, db=1)
                field_name = "place_id"
                field_value = data.get(field_name)
                json_string = json.dumps(data)
                r.set(field_value, json_string)
                return Response({"message": f"Data stored in Redis successfully {field_value} "})

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=400)


@api_view(['PATCH'])
def description_place(request, place_id):
    try:
        r = redis.StrictRedis(host='redis', port=6379, db=1)
        description = json.loads(request.body)
        if description:
            retrive_data_from_redis = r.get(place_id)
            convert_data_to_json = json.loads(retrive_data_from_redis)
            merged_json = {**convert_data_to_json, **description, }
            convert_json_to_str = json.dumps(merged_json)
            r.set(place_id, convert_json_to_str)
            return Response({"description": description}, status=status.HTTP_200_OK)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON format"}, status=400)
