FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --upgrade pip
RUN groupadd -f user
RUN useradd -d /home/user -g user -s /bin/bash user
RUN ["mkdir", "/code"]
RUN ["chown","-R","user:user","/code"]
RUN ["mkdir", "/home/user"]
RUN ["chown","-R","user:user","/home/user"]
ENV PATH="/home/user/.local/bin:${PATH}"
USER user
WORKDIR /code
COPY --chown=user:user conf/requirements.txt /code/
RUN pip install --user --no-cache-dir -r requirements.txt