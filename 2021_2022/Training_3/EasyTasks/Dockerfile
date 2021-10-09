FROM php:7.0-apache

RUN apt-get update && \
    apt-get install -y mysql-client && \
    apt-get clean

RUN a2enmod rewrite && service apache2 restart

COPY task /var/www/html/