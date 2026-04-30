A reverse proxy sits in front of backend services and handles client-facing traffic.

Typical responsibilities:
- TLS termination
- load balancing
- request routing
- caching/compression
- auth/rate-limit enforcement

Why it matters in microservices:
- Hides internal service topology.
- Centralizes cross-cutting concerns.
- Improves security by exposing fewer internal endpoints.

Common tools: NGINX, Envoy, HAProxy, cloud API gateways.

---

Topics: "Backend, [[Microservices]], Networking"
Reference: "NGINX and Envoy official docs"
Type: #atom
