from api_connectors.ebird.queries import EbirdQueries
from models.birds import Birds
from visualisation.nearby_birds_map import plot_nearby_birds
from models.get_local_position import LocalPosition
import os
import sys

python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

def main():
    api_token = os.getenv("EBIRD_API_TOKEN")
    if not api_token:
        print(
            "Error: EBIRD_API_TOKEN environment variable is not set.", file=sys.stderr
        )
        print("Please set it using: set EBIRD_API_TOKEN=your_token", file=sys.stderr)
        sys.exit(1)

    ebird_queries = EbirdQueries(api_token)
    try:
        local_position = LocalPosition.from_ip()
        ebird_response = ebird_queries.get_recent_nearby_observations(
            lat=local_position.latitude,
            lng=local_position.longitude,
        )
        birds = Birds.from_ebird_response(ebird_response)
        plot_nearby_birds(birds)
    except Exception as e:
        print(f"Error fetching eBird data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
