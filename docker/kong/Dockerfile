FROM kong

RUN apk update \
    && apk add postgresql git

COPY kong-plugin-cookie-jwt /home/kong/kong-plugin-cookie-jwt 

RUN cd /home/kong/kong-plugin-cookie-jwt \
    && luarocks make

ENV KONG_PLUGINS=bundled,cookie_jwt

COPY docker-entrypoint.sh /
