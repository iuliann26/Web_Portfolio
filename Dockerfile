FROM python:3.11-slim
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl apt-transport-https gpg openssh-server && \
    # Configurare SSH 
    echo "root:Docker!" | chpasswd && \
    # Configurare MSSQL
    curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev && \
    # Curățenie pentru a menține imaginea mică
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/run/sshd
WORKDIR /app_project
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80 2222
CMD service ssh start && gunicorn --bind 0.0.0.0:80 "app:create_app()"