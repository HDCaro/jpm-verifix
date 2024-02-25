# jpm-Cert Environment
Django CRUD for Cert Environment parameters set

Last refactor included Greg's requests:

- Instead of "VeriFIX" it should say "Cert Environment".  We should not really mention VeriFIX at all on the site
- I don't really want to create and manage user logins for every customer and for every FIX session.
  That's unneeded overhead.  We need a generic "jpm customer" login and then each customer will enter 
  their FIX comp ID along with their desired parameters.
- And with the above setup, I don't think we need an admin role.  (but if it's there, it's ok)
  (Superuser comes with Django)
- We'll need a different "generic" login for the result viewing site that we'll share with JPM personnel.

To run your Django app as a daemon/service on Ubuntu, you can use systemd to manage the process.
Here's a step-by-step guide:

1. Create a systemd service file for your Django app.
   sudo vi /etc/systemd/system/jpm_cert.service

Add this to the file:
*********************
[Unit]
Description=Django JPM Cert Service
After=network.target

[Service]
User=hcaro
Group=hcaro
WorkingDirectory=/home/hcaro/jpmorgan/jpm-verifix
ExecStart=/home/hcaro/jpmorgan/venv/bin/python manage.py runserver 10.70.4.35:8000
Restart=always

[Install]
WantedBy=multi-user.target 
***************************

2. Restart the daemon:
   sudo systemctl daemon-reload

3. Start service:
   sudo systemctl start jpm_cert

4. Enable service:
   sudo systemctl enable jpm_cert

5. Check it is running:
   sudo systemctl status jpm_cert
