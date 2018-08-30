FROM nextcloud:14-beta-apache
COPY storage.config.php /usr/src/nextcloud/config/storage.config.php
