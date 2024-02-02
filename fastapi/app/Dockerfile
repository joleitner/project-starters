# Check newest python version: https://hub.docker.com/_/python
FROM python:3.11-alpine

ARG USERNAME=pyuser

# create non-root user and set working directory
RUN adduser -D $USERNAME
WORKDIR /home/$USERNAME/app

# install dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# copy source code
COPY --chown=${USERNAME}:${USERNAME} . .

USER $USERNAME

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
