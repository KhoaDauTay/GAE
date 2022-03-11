FROM traefik:v2.2.11
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/gae-gw-systems.cert \
  && touch /etc/traefik/acme/gae-gw-systems.key \
  && chmod 777 /etc/traefik/acme/gae-gw-systems.cert \
  && chmod 777 /etc/traefik/acme/gae-gw-systems.key
COPY ./compose/production/traefik/traefik.yml /etc/traefik
