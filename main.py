from api_connectors.ebird.queries import EbirdQueries
import os 

def main():
    ebird_queries = EbirdQueries(os.getenv("EBIRD_API_TOKEN"))
    print(ebird_queries.get_recent_observations_in_region("KZ"))

if __name__ == "__main__":
    main()