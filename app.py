import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery
CLIENT_SECRET = 'client_secret.json'
SCOPE = 'https://www.googleapis.com/auth/blogger'
STORAGE = Storage('credentials.storage')
# Start the OAuth flow to retrieve credentials
def authorize_credentials():
# Fetch credentials from storage
    credentials = STORAGE.get()
# If the credentials doesn't exist in the storage location then run the flow
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, STORAGE, http=http)
    return credentials
credentials = authorize_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ("https://{api}.googleapis.com/$discovery/rest?" "version={apiVersion}")
service = discovery.build('blogger', 'v3', http=http, discoveryServiceUrl=discoveryUrl) 
users = service.users()
    # Retrieve this user's profile information
thisuser = users.get(userId='self').execute()
print('This user\'s display name is: %s' % thisuser['displayName'])
posts=service.posts()
payload={
        "content": "This Blog Post is created with Python,
        "title": "Python Blogger Automation",
        }
respost=posts.insert(blogId='xxxxxxxxxxxxxxxxxx',body=payload,isDraft=False).execute() #updating the existing post/page
respost
