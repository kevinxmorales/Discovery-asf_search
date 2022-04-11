from asf_search.ASFSession import ASFSession

def run_auth_with_creds(username: str, password: str):
    session = ASFSession()
    session.auth_with_creds(username=username, password=password)

def run_auth_with_token(token: str):
    session = ASFSession()
    session.auth_with_token(token=token)
