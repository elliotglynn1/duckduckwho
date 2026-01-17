import requests

class EbirdQueries: 
  def __init__(self, token: str):
    self.headers = {
      'X-eBirdApiToken': token
    }
    self.base_url = "https://api.ebird.org/v2/data/obs"
    self.payload = {}

  def get_recent_observations_in_region(self, region_code: str):
    response = requests.request("GET", f"{self.base_url}/{region_code}/recent", headers=self.headers, data=self.payload)
    response.raise_for_status() 
    return response.json()

  def get_recent_notable_observations_in_region(self, region_code: str):
    response = requests.request("GET", f"{self.base_url}/{region_code}/recent/notable?detail=full", headers=self.headers, data=self.payload)
    response.raise_for_status() 
    return response.json()

  def get_recent_observations_of_species_in_region(self, region_code: str, species_code: str):
    response = requests.request("GET", f"{self.base_url}/{region_code}/recent/{species_code}", headers=self.headers, data=self.payload)
    response.raise_for_status() 
    return response.json()

  def get_recent_nearby_observations(self, lat: float, lng: float):
    response = requests.request("GET", f"{self.base_url}/geo/recent?lat={lat}&lng={lng}", headers=self.headers, data=self.payload)
    response.raise_for_status()
    return response.json()
