#!/bin/bash

# composer
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer
if [ -f /var/www/app/composer.json ]; then
    composer install -d /var/www/app -vvv
fi

# start supervisor services
supervisord -n -c /etc/supervisord.conf
