FROM nextcloud:14-beta-apache
COPY capacity.config.php /usr/src/nextcloud/config/capacity.config.php
COPY domains.config.php /usr/src/nextcloud/config/domains.config.php
COPY storage.config.php /usr/src/nextcloud/config/storage.config.php
