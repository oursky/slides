AWS ELB vs AWS ALB vs Google L7 LB
===

Created with Marp
12 August 2016

Updated
16 Jan 2018

---

# What is Load Balancer

- Common for web applications to be served by a number of servers, for performance and availability
- Load balancer routes traffic to your servers
- How to decide where to route traffic to?

---

# What is L4 and L7

- ISO OSI Model

![](http://www.highteck.net/images/22-TCP-IP-ISO-OSI.jpg)

---

# AWS Classic Load Balancer (formerly Elastic Load Balancer)

- L4 Load Balancer (TCP level)
- Understand TCP traffic only (with minimal support for HTTP headers)
- Route traffic based on TCP port number
- Route traffic to only one Autoscaling Group (i.e. can only route to one application)

---

# AWS Application Load Balancer

- L7 Load Balancer
- Understand HTTP traffic (and websocket too)
- Route traffic based on path-based rules
- Route traffic to multiple Autoscaling Groups (requests to /jane and requests to /linda are routed to different applications)

---

![](https://media.amazonwebservices.com/blog/2016/alb_con_splash_1.png)

---

# Google L7 Load Balancer

- L7 Load Balancer
- Understand HTTP traffic
- Route traffic based on host name, and path rules
- Route traffic to multiple Target Groups (requests to example.com/jane and example.org/jane are routed to different applications)

---

# Why route requests based on host name and path?

- www.example.com route to web application server
- admin.example.com route to admin panel server
  - require host-based rules
- www.example.com/static route to static file servers
  - require path-based rules

---

# Why exciting? Pricing!

- ELB
  - $0.025 per ELB-hour ($18/month)
  - $0.008 per GB
- ALB
  - $0.0225 per ALB-hour ($16.2/month)
  - $0.008 per LCU-hour (roughly translate to connections and throughput per hour)
- Google L7
  - $0.025 per hour (5 rules included)  ($18/month)
  - $0.010 per additional rule 
  - $0.008 per GB

## Still don't get it?

---

# If you have 3 applications

- ELB
  - $0.025 * 3
  - $54 per month + $0.008 per GB
- ALB
  - $0.0225 * 1
  - **$16.2** per month + $0.008 per “throughput”
- Google L7
  - $0.025 * 1
  - **$18** per month + $0.008 per GB

---

# If you have 10 applications

- ELB
  - $0.025 * 10
  - $180 per month + $0.008 per GB
- ALB
  - $0.0225 * 1
  - **$16.2** per month + $0.008 per “throughput”
- Google L7
  - $0.025 * 1 + $0.010 * 5
  - **$54** per month + $0.008 per GB

