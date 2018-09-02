#!/usr/bin/python
import sys
import getopt

def main(trusted_domains, storage_class, bucket, region, aws_key, aws_secret, password_salt, nextcloud_secret, dbname, dbhost, dbport, dbuser, dbpass):
    config_str = ""
    config_str += """
    <?php
    $CONFIG = array (
        'htaccess.RewriteBase' => '/',
        'memcache.local' => '\\OC\\Memcache\\APCu',
        'apps_paths' => array (
            0 => array (
                'path' => '/var/www/html/apps',
                'url' => '/apps',
                'writable' => false,
             ),
            1 => array (
                'path' => '/var/www/html/custom_apps',
                'url' => '/custom_apps',
                'writable' => true,
            ),
        ),
        'quota_include_external_storage' => true,
        'loglevel' => 'all',
        'trusted_domains' => array ( 
    """
    index = 0
    for domain in trusted_domains:
        config_str+= "%d => '%s'," % (index, domain)
        index += 1
    config_str += """),
    'objectstore' => array (
        'class' => 'OC\\Files\\ObjectStore\\%s',
        'arguments' => array (
            'bucket' => '%s',
            'autocreate' => false,
            'region' => '%s',
            'use_ssl' => false,
            'key' => '%s',
            'secret' => '%s',
        ),
    ),
    'passwordsalt' => '%s',
    'secret' => '%s',
    'datadirectory' => '/var/www/html/data',
    'dbtype' => 'pgsql',
    'version' => '14.0.0.16',
    'dbname' => '%s',
    'dbhost' => '%s',
    'dbport' => '%s',
    'dbtableprefix' => '',
    'dbuser' => '%s',
    'dbpassword' => '%s',
    'installed' => true,
);    
    """ % (storage_class, bucket, region, aws_key, aws_secret, password_salt, nextcloud_secret, dbname, dbhost, dbport, dbuser, dbpass)
    print(config_str)
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"s:b:r:::::d:h:p:u:P::",["storage=","bucket=","region=","aws-key=","aws-secret=","password-salt=","nextcloud-secret=","dbname=","dbhost=","dbport=","dbuser=","dbpass=","trusted-domain="])
        trusted_domains = []
        storage_class = None
        bucket = None
        region = None
        aws_key = None
        aws_secret = None
        password_salt = None
        nextcloud_secret = None
        dbname = None
        dbhost = None
        dbport = None
        dbuser = None
        dbpass = None
        for opt, arg in opts:
            if opt == '--trusted-domain':
                trusted_domains.append(arg)
            if opt == '--storage':
                if arg == 'S3':
                    storage_class = arg
                else:
                    print("storage option is not set correctly, either Swift or S3")
            if opt == '--bucket':
                bucket = arg
            if opt == '--region':
                region = arg
            if opt == '--aws-key':
                aws_key = arg
            if opt == '--aws-secret':
                aws_secret = arg
            if opt == '--password-salt':
                password_salt = arg
            if opt == '--nextcloud-secret':
                nextcloud_secret = arg
            if opt == '--dbname':
                dbname = arg
            if opt == '--dbhost':
                dbhost = arg
            if opt == '--dbport':
                dbport = arg
            if opt == '--dbuser':
                dbuser = arg
            if opt == '--dbpass':
                dbpass = arg

        if storage_class is None:
            print("--storage is not defined")
            sys.exit(2)
        if bucket is None:
            print("--bucket is not defined")
            sys.exit(2)
        if region is None:
            print("--region is not defined")
            sys.exit(2)
        if aws_key is None:
            print("--aws-key is not defined")
            sys.exit(2)
        if aws_secret is None:
            print("--aws-secret is not defined")
            sys.exit(2)
        if password_salt is None:
            print("--password-salt is not defined")
            sys.exit(2)
        if nextcloud_secret is None:
            print("--nextcloud_secret is not defined")
            sys.exit(2)
        if dbname is None:
            print("--dbname is not defined")
            sys.exit(2)
        if dbhost is None:
            print("--dbhost is not defined")
            sys.exit(2)
        if dbport is None:
            print("--dbport is not defined")
            sys.exit(2)
        if dbuser is None:
            print("--dbuser is not defined")
            sys.exit(2)
        if dbpass is None:
            print("--dbpass is not defined")
            sys.exit(2)
        if len(trusted_domains) == 0:
            print("--trusted-domain is not defined, please set at least one or the nextcloud instance will not be accessible")
            sys.exit(2)
        main(trusted_domains, storage_class, bucket, region, aws_key, aws_secret, password_salt, nextcloud_secret, dbname, dbhost, dbport, dbuser, dbpass)
    except getopt.GetoptError as e:
        print(e)
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
