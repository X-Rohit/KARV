from django.db import connection

newcoin=1000
x="naruto"
cursor=connection.cursor()
cursor.execute('UPDATE home_register SET coins= %s WHERE username=  %s',[newcoin, x])
         