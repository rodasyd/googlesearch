import serpapi
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')  # get API key from env file
client = serpapi.Client(api_key=api_key)

result = client.search(
    q=input(),  # keyword to search
    engine="google",
    location="Germany",  # add location (country name, city or state)
    hl="en",  # language
    gl="us",  # geo location
    start="0",  # starting page: 10 is second page, 20 is third...
    num="20",  # number of results (currently two pages)
)

# print(result)

# or search_information, local_map, local_results, related_questions, recipes_results, knowledge_graph, search_information > menu_items, search_information > total_results, search_information > query_display:
print(result["organic_results"])

for item in result["organic_results"]:
    print(item['title'])
    print(item['link'])
    print(item['snippet'])
    print('================')
