# Link Preview (unfurl)
Install the Heroku CLI
Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```bash
heroku login
```
Add heroku remote if you already have app from heroku dashboard
```
heroku git:remote -a preview-link
```
Create heroku app
```
heroku create preview-link
```
Push to heroku
```
git push heroku main
```
