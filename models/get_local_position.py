from dataclasses import dataclass
from typing import Optional

import geocoder


@dataclass
class LocalPosition:
    latitude: float
    longitude: float
    
    def init(self, latitude: Optional[float] = None, longitude: Optional[float] = None):
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_ip(cls) -> Optional["LocalPosition"]:
        """Resolve the current machine's public IP to latitude/longitude."""
        g = geocoder.ip("me")

        if not g.ok or not g.latlng:
            return None

        latitude, longitude = g.latlng

        return cls(
            latitude=latitude,
            longitude=longitude,
        )
        
    @classmethod
    def from_location(cls, location: str) -> Optional["LocalPosition"]:
        """Resolve a location string to latitude/longitude."""
        g = geocoder.google(location)

        if not g.ok or not g.latlng:
            return None

        latitude, longitude = g.latlng

        return cls(
            latitude=latitude,
            longitude=longitude,
        )
