FROM pemcconnell/phpnginx 
MAINTAINER Peter McConnell <me@petermcconnell.com>

# additional software
RUN apt-get update --fix-missing
RUN apt-get install -y git

# file management
ADD ./ops/supervisord.conf /etc/supervisord.conf
ADD ./ops/vhost.conf /etc/nginx/sites-available/default
ADD ./app /var/www/app
RUN touch /var/log/php5-fpm.log
RUN chown -R www-data /var/www/app

# expose ports
EXPOSE 80

# rev er up
ADD ./ops/start.sh /start.sh
RUN chmod 755 /start.sh
CMD ["/bin/bash", "/start.sh"]
