FROM python

WORKDIR /app
COPY app /app
COPY cmd.sh /

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install -r requirements.txt
EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]