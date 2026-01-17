from api_connectors.ebird.queries import EbirdQueries
from models.birds import Birds
import os 
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def main():
    api_token = os.getenv("EBIRD_API_TOKEN")
    if not api_token:
        print("Error: EBIRD_API_TOKEN environment variable is not set.", file=sys.stderr)
        print("Please set it using: set EBIRD_API_TOKEN=your_token", file=sys.stderr)
        sys.exit(1)
    
    ebird_queries = EbirdQueries(api_token)
    try:
        ebird_response = ebird_queries.get_recent_observations_in_region("KZ")
        birds = Birds.from_ebird_response(ebird_response)
        birds.dataframe.show()
    except Exception as e:
        print(f"Error fetching eBird data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
