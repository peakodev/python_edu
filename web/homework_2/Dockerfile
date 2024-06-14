FROM python:3.12

ENV APP_HOME /app
ENV AGENT_NOTES_FOLDER /app/agent_notes
ENV XFILE_SORTER_FOLDER /app/xfiles_sorter
ENV AGENT_BOOK_FOLDER /app/agent_book
ENV JAMESBOT_FOLDER /app/jamesbot

WORKDIR $APP_HOME

COPY . .

RUN pip install pipenv

RUN cd $AGENT_NOTES_FOLDER && \
    python setup.py install

RUN cd $XFILE_SORTER_FOLDER && \
    pipenv install && \
    python setup.py install

RUN cd $AGENT_BOOK_FOLDER && \
    pipenv install && \
    python setup.py install

RUN cd $JAMESBOT_FOLDER && \
    pipenv install && \
    python setup.py install

WORKDIR $JAMESBOT_FOLDER

ENTRYPOINT ["james"]