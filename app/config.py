# import os

# # DATABASE_URL = os.getenv("DATABASE_URL","postgresql://postgres:SimplePass!2024@localhost:5432/geo_database")
# # GEOJSON_URL = os.getenv(
# #     "GEOJSON_URL",
# #     "https://file.notion.so/f/f/9301458a-f465-42d3-80eb-7c09bae15034/282d7ed4-5168-4e77-91be-59906c19f9f3/Map_(10).geojson?table=block&id=655f6883-c12c-4503-bd82-157ea8ee1571&spaceId=9301458a-f465-42d3-80eb-7c09bae15034&expirationTimestamp=1733508000000&signature=pxNn_GtkzVZ3wnwKnwbCrWJnIfBqEgnvVEEnb3WqdQs&downloadName=karnataka.geojson"
# # )
# DATABASE_URL = os.getenv("DATABASE_URL", "DATABASE_URL=postgresql://postgres:SimplePass!2024@db:5432/geo_database")

# # You can also add the GEOJSON_URL here if needed
# GEOJSON_URL = os.getenv("GEOJSON_URL", "https://file.notion.so/f/f/9301458a-f465-42d3-80eb-7c09bae15034/282d7ed4-5168-4e77-91be-59906c19f9f3/Map_(10).geojson?table=block&id=655f6883-c12c-4503-bd82-157ea8ee1571&spaceId=9301458a-f465-42d3-80eb-7c09bae15034&expirationTimestamp=1733508000000&signature=pxNn_GtkzVZ3wnwKnwbCrWJnIfBqEgnvVEEnb3WqdQs&downloadName=karnataka.geojson")
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Ensure DATABASE_URL is set correctly
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SimplePass!2024@localhost:5432/geo_database")

# You can also add the GEOJSON_URL here if needed
GEOJSON_URL = os.getenv("GEOJSON_URL", "https://file.notion.so/f/f/9301458a-f465-42d3-80eb-7c09bae15034/282d7ed4-5168-4e77-91be-59906c19f9f3/Map_(10).geojson?table=block&id=655f6883-c12c-4503-bd82-157ea8ee1571&spaceId=9301458a-f465-42d3-80eb-7c09bae15034&expirationTimestamp=1733508000000&signature=pxNn_GtkzVZ3wnwKnwbCrWJnIfBqEgnvVEEnb3WqdQs&downloadName=karnataka.geojson")
