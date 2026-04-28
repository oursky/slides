# Redis HA Example

## Setup
- redis1: initially master
- redis2: initially slave
- sentinel: failover by switching master between redis1/redis2
- haproxy: provide endpoint to application, check each node's role, route to current master.
- redis-cli: test client connect to redis via haproxy

## Test
### Start all servers
```
podman-compose --podman-run-args=--replace up -d redis1 redis2 sentinel haproxy
```
### Connect rediscli
```
podman-compose run --rm redis-cli redis-cli -h haproxy -a 1234
haproxt:6379> set test "1234"
haproxt:6379> get test
"1234"
```
### Stop redis1
```
podman-compose stop redis1
```
> See redis2 promoted to master.

```
haproxy:6379> get test
Error: Server closed the connection
not connected> get test
"1234"
```
### Start redis1
```
podman-compose up -d redis1
```
> See redis1 acts as slave and sync from redis2.
### Stop redis2
```
podman-compose stop redis2
```
> See redis1 promoted to master.

```
haproxy:6379> get test
Error: Server closed the connection
not connected> get test
"1234"
```
### Start redis2
```
podman-compose up -d redis2
```
> See redis2 acts as slave and sync from redis1.
```
