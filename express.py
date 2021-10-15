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
        "content": ''' <img src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Obverse_of_the_series_2009_%24100_Federal_Reserve_Note.jpg"width="300"height="50">Make 100 Millions of Dollars with Google Api Python library<br> Download Google Python libraries on Googleapis Github''',
        "title": "12 Million Dollars Python Developer",
        }
respost=posts.insert(blogId='913409048670049489',body=payload,isDraft=False).execute() #updating the existing post/page
respost