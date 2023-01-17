import google.oauth2.credentials
import google_auth_oauthlib.flow


flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=[
        'https://www.googleapis.com/auth/userinfo.email	',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/calendar.events.readonly',
    ])
flow.redirect_uri = 'http://5.189.145.181/'
authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'
)

