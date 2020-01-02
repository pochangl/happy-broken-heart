import twitter
from credentials import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

api = twitter.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN_KEY,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

statuses = api.GetSearch(term='break-up')
for status in statuses:
    print(status.created_at, '\n', status.text)
