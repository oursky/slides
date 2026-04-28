# PgSQL

## HA Solutions
https://www.postgresql.org/docs/current/high-availability.html

### Primay-standby with pg_auto_failover
Reference: https://pg-auto-failover.readthedocs.io/en/main/tutorial.html

1. Primary pgsql
2. Log-shipping standby pgsql
3. Monitor node (`pg_auto_failover`) - it promote standby upon failover.
4. HAProxy - app endpoint route to current primary.
5. Custom http script to tell HAProxy if which node is primary.

### Start Monitor
Start monitor and set password for the monitoring channel.
```
podman-compose up -d monitor
podman-compose exec monitor psql -U autoctl_node pg_auto_failover -c "ALTER USER autoctl_node PASSWORD 'monitor1234'";
```
### Monitoring Dashboard
```
podman-compose exec monitor pg_autoctl watch
```
### Primary Database
Start primary database and configure system passwords.
```
podman-compose up -d pg1
podman-compose exec pg1 psql -U postgres postgres -c "ALTER USER postgres PASSWORD 'postgres1234'";
podman-compose exec pg1 psql -U postgres postgres -c "ALTER USER pgautofailover_replicator PASSWORD 'replica1234'";
```
> NOTE: See pg1 joined on the monitoring dashboard.

### Standby Database
```
podman-compose up -d pg2
```
> NOTE: See pg2 joined on the monitoring dashboard. The accounts and passwords will be synchronized to pg2.

### Adjust pg_hba.conf
By default PAF maintain a strict IP/32 ACL, it works if our database does not change IP, however for podman it changes IP upon restarts.
To allow restarted instance to re-connect, we add an `0.0.0.0/0` entry.
```
podman-compose exec pg1 sh -c 'echo "hostssl replication pgautofailover_replicator 0.0.0.0/0 scram-sha-256" | tee -a /var/lib/postgresql/18/docker/pg_hba.conf'
podman-compose exec pg1 sh -c 'echo "hostssl all all 0.0.0.0/0 scram-sha-256" | tee -a /var/lib/postgresql/18/docker/pg_hba.conf'
podman-compose exec pg1 pg_autoctl reload
```
> NOTE: It will be propoaged to pg2.

### Create App Database & User
```
podman-compose run --rm -e PGSSLMODE=require cli psql -h pg1 -U postgres postgres
  CREATE USER "app" WITH ENCRYPTED PASSWORD 'app1234';
  CREATE ROLE app_owners NOLOGIN;
  GRANT app_owners TO "postgres", "app";
  CREATE DATABASE "appdb" WITH ENCODING='UTF8' OWNER="app_owners";

podman-compose run --rm -e PGSSLMODE=require cli psql -h pg1 -U app appdb
  CREATE TABLE foo(id SERIAL PRIMARY KEY, bar INT NOT NULL);
  INSERT INTO foo(bar) VALUES(1);
  INSERT INTO foo(bar) VALUES(2);
  INSERT INTO foo(bar) VALUES(3);
  SELECT * FROM foo;

podman-compose run --rm -e PGSSLMODE=require cli psql -h pg2 -U app appdb
  SELECT * FROM foo;
  INSERT INTO foo(bar) VALUES(4);
```
> NOTE: write error as standby is read-only.

### HAProxy & Failover
```
podman-compose up -d pg-health1 pg-health2 haproxy
podman-compose run --rm -e PGSSLMODE=require cli psql -h haproxy -U app appdb
podman-compose stop pg1
podman-compose up -d pg1
podman-compose stop pg2
podman-compose up -d pg2
```

#### Trigger failover without down
```
podman-compose exec monitor pg_autoctl perform switchover
```
