# jira-issues-parser
JIRA Issues Parser

Generate keys
-------------

# Run the following commands

- openssl genrsa -out jira_privatekey.pem 1024

- openssl req -newkey rsa:1024 -x509 -key jira_privatekey.pem -out jira_publickey.cer -days 365

- openssl pkcs8 -topk8 -nocrypt -in jira_privatekey.pem -out jira_privatekey.pcks8

- openssl x509 -pubkey -noout -in jira_publickey.cer  > jira_publickey.pem

Generate config.example
-----------------------

**If you don't have java on your PC you have to install it to execute this command**

- java -jar OAuthTutorialClient-1.0.jar requestToken


Create application link
-----------------------

- Go to https://jira-tt-123.atlassian.net/plugins/servlet/applinks/listApplicationLinks

- Type http://example.com in the field and click "Create new link"

- Wait a few seconds until modal window opens and click "Continue"

- Next modal window opens, fill in the fields as shown below

* Application Name = anything you want
* Application Type = Generic application
* Service Provider Name = anything you want
* Consumer key = OauthKey
* Shared secret = anything you want
* Request Token URL = http://example.com
* Access token URL = http://example.com
* Authorize URL = http://example.com

- Click "Continue"

- Next modal window opens, fill in the fields as shown below

* Consumer Key = OauthKey
* Consumer Name = Your name
* Public Key = copy the public key from the `jira_publickey.pem` file and paste it into this field
  Warning: You need to copy only the text between `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` not all the content.
* Click "Continue"

Change config.example settings
------------------------------

- Open `jira_privatekey.pcks8` and copy only the text between `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----`

- Open this website https://www.textfixer.com/tools/remove-line-breaks.php and paste the content in the field then click **Remove Line Breaks**

- Scroll down, the new content is inside **New Text without Line Breaks** click **Copy to Clipboard**

- Open `config.properties` remove the text in front of `private_key` and paste the text from the previous step

- Inside `config.properties` change **consumer_key** value to `OauthKey` and **jira_home** to your domain for example: https://askar.atlassian.net

- Save the file

Generate tokens
---------------

# Run the following commands

- `java -jar OAuthTutorialClient-1.0.jar requestToken`
- If everything is correct, the result will be something like this:
`
Token:            ec3dj4byySM5ek3XW7gl7f4oc99obAlo
Token Secret:   OhONj0eF7zhXAMKZLbD2Rd3x7Dmxjy0d
Retrieved request token. go to https://jira101.atlassian.net/plugins/servlet/oauth/authorize?oauth_token=ec3dj4byySM5ek3XW7gl7f4oc99obAlo to authorize it
`
- Copy **Token Secret** key and paste it to **secret_token** in `settings.py`
- Copy **Retrieved request token URL** and open it in your browser
- You will see a **Welcome to Jira** message, click **Allow** button
- Copy the verification code that retrieved from the website, for example: **You have successfully authorized ''. Your verification code is 'fIc2e9'.**
- `java -jar OAuthTutorialClient-1.0.jar accessToken qTJkPi`, replace code with yours.
- Copy **Access token** key and paste it to **access_token** in `settings.py`

Change `settings.py`:
---------------------

# Open `settings.py`

- DOMAIN = your project domain without atlassian.net
- consumer_key = keep it OauthKey
- project_key = change **MYB** to your project key, you can get the key from your JIRA dashboard
