FROM nextcloud:14-beta-apache
COPY configuration-entrypoint.sh /
RUN chmod +x /configuration-entrypoint.sh
CMD ["apache2-foreground"]
ENTRYPOINT ["/configuration-entrypoint.sh"]
