FROM postgres:18.3-trixie

# Reference: https://pg-auto-failover.readthedocs.io/en/main/install.html
RUN apt-get update && apt-get install -y --no-install-recommends \
    pg-auto-failover-cli \
    postgresql-18-auto-failover \
    && rm -rf /var/lib/apt/lists/*

# Bypass initdb of a "main" cluster
RUN echo 'create_main_cluster = false' | tee -a /etc/postgresql-common/createcluster.conf
