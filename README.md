# irden-fire server
## web-developer forrana (forrana@gmail.com)
### Irden web-page server
###### Based on django and django-rest-framework backend server which responsible for keep and manage data, sending e-mails and so on.

For work with this project you need to install python then pip, then django
and django-rest-framework  
After that you need to execute in root of the project next commands:
1. python manage.py migrate;
2. python manage.py createsuperuser;
3. python manage.py runserver;
4. log in to admin section by the link 127.0.0.1:8000/admin/ If you need to watch
into your site records;
5. Also please setup smtp e-mail server to your personal temporary account, you can
type settings into ./irden_fire_server/settings.py
(EMAIL_HOST_USER = 'your@gmail.com', EMAIL_HOST_PASSWORD = 'your password');

If you stuck out on it. Checkout it in more details here please:
http://www.django-rest-framework.org/tutorial/quickstart/
