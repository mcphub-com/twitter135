import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Glavier/api/twitter135'

mcp = FastMCP('twitter135')

@mcp.tool()
def auto_complete(q: Annotated[str, Field(description='Search query')]) -> dict: 
    '''Auto Complete'''
    url = 'https://twitter135.p.rapidapi.com/AutoComplete/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(q: Annotated[str, Field(description='Search query You can use advanced search queries. E.g. dogecoin (from:elonmusk) Check out for more information: https://twitter.com/search-advanced')],
           count: Annotated[Union[int, float, None], Field(description='Number of Tweet results Default: 20')] = None,
           cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None,
           type: Annotated[Literal['Top', 'Latest', 'People', 'Media', 'Lists', None], Field(description='Default: Top Example: Top')] = None,
           safe_search: Annotated[Union[bool, None], Field(description='Default: true Example: true')] = None) -> dict:
    '''Search'''
    url = 'https://twitter135.p.rapidapi.com/Search/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'count': count,
        'cursor': cursor,
        'type': type,
        'safe_search': safe_search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def trends(location_id: Annotated[str, Field(description='Location ID You must use the Locations endpoint to find IDs. Currently only countries are supported')],
           count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None) -> dict:
    '''Trends'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Trends/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'count': count,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def locations(q: Annotated[Union[str, None], Field(description='Search query Leave blank to get countries')] = None) -> dict:
    '''Locations'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Locations/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_detail_conversation(id: Annotated[str, Field(description='Tweet ID')],
                              cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None,
                              rankingMode: Annotated[Literal['Relevance', 'Recency', 'Likes', None], Field(description='Sort replies by Example: Relevance')] = None) -> dict:
    '''Tweet Detail & Conversation'''
    url = 'https://twitter135.p.rapidapi.com/v2/TweetDetail/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'cursor': cursor,
        'rankingMode': rankingMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_detail_alternative(id: Annotated[str, Field(description='Tweet ID')]) -> dict:
    '''Tweet Detail / Alternative'''
    url = 'https://twitter135.p.rapidapi.com/v2/Tweet/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_retweeters(id: Annotated[str, Field(description='Tweet ID')],
                     count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                     cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''Tweet Retweeters'''
    url = 'https://twitter135.p.rapidapi.com/v2/Retweeters/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def translate_tweet(id: Annotated[str, Field(description='Tweet ID')],
                    language: Annotated[str, Field(description='Destination language')]) -> dict:
    '''Translate Tweet'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/TranslateTweet/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_users(ids: Annotated[Union[str, None], Field(description='User IDs A comma separated list of User IDs. Up to 100 are allowed in a single request.')] = None,
              usernames: Annotated[Union[str, None], Field(description='User screen names A comma separated list of Usernames. Up to 100 are allowed in a single request.')] = None) -> dict:
    '''Get Users'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Users/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ids': ids,
        'usernames': usernames,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_by_screen_name(username: Annotated[str, Field(description='Username')]) -> dict:
    '''User By Screen Name'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserByScreenName/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_by_rest_id(id: Annotated[str, Field(description='User ID')]) -> dict:
    '''User By Rest ID'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserByRestId/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def users_by_rest_ids(ids: Annotated[str, Field(description='Users IDs (you can separate with commas)')]) -> dict:
    '''Users By Rest IDs'''
    url = 'https://twitter135.p.rapidapi.com/v2/UsersByRestIds/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_tweets(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                count: Annotated[Union[int, float, None], Field(description='Number of results Default: 40')] = None,
                cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Tweets'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserTweets/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_tweets_replies(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                        count: Annotated[Union[int, float, None], Field(description='Number of results Default: 40')] = None,
                        cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Tweets & Replies'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserTweetsAndReplies/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_media(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
               count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
               cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Media'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserMedia/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followers(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                   count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                   cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Followers'''
    url = 'https://twitter135.p.rapidapi.com/v2/Followers/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followers_light(id: Annotated[Union[str, None], Field(description='User ID')] = None,
                         username: Annotated[Union[str, None], Field(description='Username Exactly one of User ID or Username must be provided.')] = None,
                         count: Annotated[Union[int, float, None], Field(description='Number of results. Max: 200 Default: 20')] = None,
                         cursor: Annotated[Union[str, None], Field(description='Cursor token')] = None) -> dict:
    '''User Followers / Light'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Followers/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followers_ids(id: Annotated[Union[str, None], Field(description='User ID')] = None,
                       username: Annotated[Union[str, None], Field(description='Username Exactly one of User ID or Username must be provided.')] = None,
                       count: Annotated[Union[int, float, None], Field(description='Number of results. Max: 5000 Default: 500')] = None,
                       cursor: Annotated[Union[str, None], Field(description='Cursor token')] = None) -> dict:
    '''User Followers IDs'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/FollowersIds/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_verified_followers(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                            count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                            cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Verified Followers'''
    url = 'https://twitter135.p.rapidapi.com/v2/VerifiedFollowers/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_following(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                   count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                   cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Following'''
    url = 'https://twitter135.p.rapidapi.com/v2/Following/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_following_light(id: Annotated[Union[str, None], Field(description='User ID')] = None,
                         username: Annotated[Union[str, None], Field(description='Username Exactly one of User ID or Username must be provided.')] = None,
                         count: Annotated[Union[int, float, None], Field(description='Number of results. Max: 200 Default: 20')] = None,
                         cursor: Annotated[Union[str, None], Field(description='Cursor token')] = None) -> dict:
    '''User Following / Light'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Following/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_following_ids(id: Annotated[Union[str, None], Field(description='User ID')] = None,
                       username: Annotated[Union[str, None], Field(description='Username Exactly one of User ID or Username must be provided.')] = None,
                       count: Annotated[Union[int, float, None], Field(description='Number of results. Max: 5000 Default: 500')] = None,
                       cursor: Annotated[Union[str, None], Field(description='Cursor token')] = None) -> dict:
    '''User Following IDs'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/FollowingIds/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'username': username,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_subscriptions(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                       count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                       cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Subscriptions'''
    url = 'https://twitter135.p.rapidapi.com/v2/Subscriptions/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_affiliates(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                    count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                    cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Affiliates'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserAffiliates/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_highlights(id: Annotated[str, Field(description='User ID Use the User By Screen Name endpoint to find the ID from a username.')],
                    count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                    cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''User Highlights'''
    url = 'https://twitter135.p.rapidapi.com/v2/UserHighlights/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def translate_profile(id: Annotated[str, Field(description='User ID')],
                      language: Annotated[str, Field(description='Destination language')]) -> dict:
    '''Translate Profile'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/TranslateProfile/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_details(list_id: Annotated[str, Field(description='List ID')]) -> dict:
    '''List Details'''
    url = 'https://twitter135.p.rapidapi.com/v2/ListDetails'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_timeline(list_id: Annotated[str, Field(description='List ID')],
                  count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                  cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''List Timeline'''
    url = 'https://twitter135.p.rapidapi.com/v2/ListTimeline/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_subscribers(list_id: Annotated[str, Field(description='List ID')],
                     count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                     cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''List Subscribers'''
    url = 'https://twitter135.p.rapidapi.com/v2/ListSubscribers'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_members(list_id: Annotated[str, Field(description='List ID')],
                 count: Annotated[Union[int, float, None], Field(description='Number of results Default: 20')] = None,
                 cursor: Annotated[Union[str, None], Field(description='Cursor for other results')] = None) -> dict:
    '''List Members'''
    url = 'https://twitter135.p.rapidapi.com/v2/ListMembers'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def community_details(community_id: Annotated[str, Field(description='Community ID')]) -> dict:
    '''Community Details'''
    url = 'https://twitter135.p.rapidapi.com/v2/CommunityDetails'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'community_id': community_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def community_moderators(community_id: Annotated[str, Field(description='Community ID')],
                         count: Annotated[Union[int, float, None], Field(description='Default: 20')] = None,
                         cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Community Moderators'''
    url = 'https://twitter135.p.rapidapi.com/v2/CommunityModerators'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'community_id': community_id,
        'count': count,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def community_member_search(community_id: Annotated[str, Field(description='Community ID')],
                            prefix: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Community Member Search'''
    url = 'https://twitter135.p.rapidapi.com/v2/CommunityMemberSearch'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'community_id': community_id,
        'prefix': prefix,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def community_members(community_id: Annotated[str, Field(description='Community ID')],
                      cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Community Members'''
    url = 'https://twitter135.p.rapidapi.com/v2/CommunityMembers'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'community_id': community_id,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashflags() -> dict:
    '''Hashflags'''
    url = 'https://twitter135.p.rapidapi.com/v1.1/Hashflags/'
    headers = {'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def notifications(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Notifications'''
    url = 'https://twitter135.p.rapidapi.com/v1/Notifications'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def update_profile(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Update Profile'''
    url = 'https://twitter135.p.rapidapi.com/v1/UpdateProfile'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def create_tweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Create Tweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/CreateTweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_tweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Delete Tweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/DeleteTweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def favorite_tweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Favorite Tweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/FavoriteTweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def unfavorite_tweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Unfavorite Tweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/UnfavoriteTweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def create_retweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Create Retweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/CreateRetweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_retweet(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Delete Retweet'''
    url = 'https://twitter135.p.rapidapi.com/v1/DeleteRetweet'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def tweet_analytics(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Tweet Analytics'''
    url = 'https://twitter135.p.rapidapi.com/v1/TweetAnalytics'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def unfollow(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Unfollow'''
    url = 'https://twitter135.p.rapidapi.com/v1/Unfollow'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def follow(data: Annotated[dict, Field(description='')] = None) -> dict:
    '''Follow'''
    url = 'https://twitter135.p.rapidapi.com/v1/Follow'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter135.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
