#FROM traefik:v2.2.11
#RUN mkdir -p /etc/traefik/acme \
#  && touch /etc/traefik/acme/gae-gw-systems.crt \
#  && touch /etc/traefik/acme/gae-gw-systems.key \
#  && chmod 777 /etc/traefik/acme/gae-gw-systems.crt \
#  && chmod 777 /etc/traefik/acme/gae-gw-systems.key
#COPY ./compose/production/traefik/traefik.yml /etc/traefik
FROM traefik:2.11.0
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/production/traefik/traefik.yml /etc/traefik
