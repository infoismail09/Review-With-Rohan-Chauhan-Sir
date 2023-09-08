import requests
import time
from django.core.cache import cache  # Imported Django's caching module
from rest_framework.views import APIView
from rest_framework.response import Response


class CustomizedDataView(APIView):
    def get(self, request):
        cache_temp = "customized_data"  
        cached_data = cache.get(cache_temp)

        if cached_data:
            return Response(cached_data)
        else:
            max_retries = 5
            retry_delay = 1  

            for retry_count in range(max_retries):
                try:
                    response = requests.get("https://reqres.in/api/unknown")
                    response.raise_for_status()
                    data = response.json().get("data", [])
                    customized_data = [{"id": item["id"], "msg": f"Hello My name is {item['name']} and my age is {item['year']}"} for item in data]

                    # Cacheing the data for 1 minutes
                    cache.set(cache_temp, customized_data, 60)  
                    print(cache.get(cache_temp))

                    return Response(customized_data)
                except requests.exceptions.RequestException as e:
                    if retry_count < max_retries - 1:
                      
                        time.sleep(retry_delay)
                        retry_delay += 1  
                    else:
                        return Response({"error": "Max retries !!!!!!!!!"}, status=500)

            return Response({"error": "Failed to fetch data after multiple retries."}, status=500)
