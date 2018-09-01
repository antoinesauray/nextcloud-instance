#!/bin/bash
mkdir -p /var/www/html/data
mkdir -p /var/www/html/config
chown -R www-data /var/www/html
: ${STORAGE:?"STORAGE needs to be defined"}
: ${BUCKET:?"BUCKET needs to be defined"}
: ${REGION:?"REGION needs to be defined"}
: ${AWS_KEY:?"AWS_KEY needs to be defined"}
: ${AWS_SECRET:?"AWS_SECRET needs to be defined"}
: ${PASSWORD_SALT:?"PASSWORD_SALT needs to be defined"}
: ${NEXTCLOUD_SECRET:?"NEXTCLOUD_SECRET needs to be defined"}
: ${DBNAME:?"DBNAME needs to be defined"}
: ${DBHOST:?"DBHOST needs to be defined"}
: ${DBPORT:?"DBPORT needs to be defined"}
: ${DBUSER:?"DBUSER needs to be defined"}
: ${DBPASS:?"DBPASS needs to be defined"}
: ${TRUSTED_DOMAIN:?"TRUSTED_DOMAIN needs to be defined"}

python /config-gen.py --storage=$STORAGE --bucket=$BUCKET --region=$REGION --aws-key=$AWS_KEY --aws-secret=$AWS_SECRET --password-salt=$PASSWORD_SALT --nextcloud-secret=$NEXTCLOUD_SECRET --dbname=$DBNAME --dbhost=$DBHOST --dbport=$DBPORT --dbuser=$DBUSER --dbpass=$DBPASS  --trusted-domain=$TRUSTED_DOMAIN > /var/www/html/config/config.php
/entrypoint.sh $@
