FROM nextcloud:14-beta-apache
COPY config.php /var/www/html/config/config.php
RUN chown www-data -R /var/www/html/config/
RUN touch /var/www/html/data/.ocdata
