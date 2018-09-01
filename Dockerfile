FROM nextcloud:14-beta-apache
RUN apt-get update
RUN apt-get install python -y
COPY config-gen.py /
RUN chmod +x /config-gen.py
COPY configuration-entrypoint.sh /
RUN chmod +x /configuration-entrypoint.sh
CMD ["apache2-foreground"]
ENTRYPOINT ["/configuration-entrypoint.sh"]
