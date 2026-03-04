
---

Topics: ComputerNetworks
Reference: https://aws.amazon.com/what-is/cidr/
Type: #atom

---
CIDR is an IP allocation method to improve efficiency on the internet vis-a-vis the data routing. Example: Class A, B and C have subnet masks of 8 prefix bits i.e. 2^24 hosts, 16, and 24 bits as prefix. So class C can have 256 hosts. So an organisation with 300 hosts will have to go for 2^16 hosts, ~65,534. Very inefficient.

### **Create supernets flexibly**

A supernet is a group of subnets with similar network prefixes. CIDR allows flexibility in creating supernets, which isn’t possible in conventional masking architecture. For example, your organization can combine IP addresses into a single network block using a notation like this:

- 192.168.1 /23 
- 192.168.0 /23

This notation applies a subnet mask of 255.255.254.0 to the IP address, which returns the first 23 bits as the network address. The router needs only one routing table entry to manage data packets between devices on the subnets.