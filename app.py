from bottle import default_app, get, post
import git 

# https://GITHUB-TOKEN-HERE@github.com/GITUHB-USERNAME/mysite.git

##############################
@post('/SECRET-URL-HERE')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

##############################
@get("/")
def _():
    return "x"

##############################
app = default_app()
