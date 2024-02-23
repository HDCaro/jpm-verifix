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

