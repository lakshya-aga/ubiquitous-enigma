Author: [[Martin Kleppmann]]
Type: #source #book
Link: 
Topics: [[System Design]]

---

## Relational Data bases vs Document Object Models

- There is a tradeoff between read and write for these models
- Normalised RDBMS have the quality of returning data through joins which means if an object property such as profile picture of a user changes, all references do not need to be updated
- However, the joins can sometimes(less often than you would think) prove to be expensive. Instead systems like MongoDB stores stuff as JSON which is a quicker lookup because all information is locally present in the database
- Another tradeoff lies in ordering. JSON can simply have an array of JSON that preserves ordering. Underlying implementation using linked list can make it easy to reorder. For RDS, we need to have a numbering which may need to be redone for simple reordering.

## Data transfer models (Chapter 5)

Generally most data is transferred via JSON or XML. JSON, by virtue of being string oriented has trouble parsing non-standard values. For example handling numbers greater than $2^{53}$ in floating point. One way around it was to encode everything as string and convert to base64. 
But Binary JSONs are generally preferred for space savings.
However, we can do better using Protocol Buffers and Avro. With these, a single source read / write schema is sent with data and packets are simply encoded to lookup keys. leading to good space savings.
These systems have their own schema defining languages as well.
XML is generally unliked due to verbosity.

## Replication

Replication is a very interesting problem and is probably more common than we realise. The basic principle is that one write to a database is propogated to other "replicas" in reduce user reponse time. It may be in different geographical locations altogether or in close vicinity just for load balancing. The leader(s) may write synchronously or asynchronously to the follower databases. Both have merits and demerits. Most commonly, we use half of each in one system.
There are a multi-leader and single leader architectures. Multi-leader is way more complex and requires conflict resolution as well. An example of multi leader is an app that runs offline as well and may need to sync when network is available. I did not pay attention to the details of consistency levels, ensuring same user on different devices sees same data, and specific methods of conflict resolution as they naturally follow from Business logic. 
One vulnerability that replication opens us up to is resolved by use of uuid instead of auto increment in database. Consider the following scenario: A user comes and writes some records, User B does the same. But due to network traffic, writes of B go first and writes of A go second, to a follower. But, the access of resources is mapped to the original order. This opens user A data to user B and vice versa. This actually did happen in an incident in github. The easiest work around is to write exact records.
Automatic Conflict resolutions have 2 algorithms used commonly, OT - Operational transformation, and CRDT - conflict free replicated datatypes. CRDT encodes index and uses those "immutable" values. OT transforms indexes to account for changes.
![[Pasted image 20260604162418.png]]


There is finally leaderless replication. Rarely used, leaderless replication has something called a quorum. The name is self-explanatory. A minimum number of reads and writes to ensure right data is recieved.

General rule: $w + r > n$ 

Here w is number of nodes synchronously written to and r is number of reads to return a value before marking a read is done, This condition ensures that at least 1 overlapping node will be read from and written to.

## Sharding

Just dividing one database across mutiple nodes if it is too big. Complex solution but no other choice for such huge databases to be honest. Also known as region in CockroachDB and TiDB. The most complex part of it in terms of design is to balance flexibility with hot spots. Some shards may be overloaded and may need to be split. This rebalancing can be costly. We also need to decide automatic or manual rebalancing. Automatic can be unpredictable as it is an expensive operation, you might want to have control over it.

Another problem is a co-ordinating node that provides information of which node has which shard based on key. Now during a split + request in flight what happens? Solution is to have a solution like Zookeeper or etcd. Then use [[Consensus Algorithms]] to provide fault tolerance and protection against split brain. Zookeeper maintains the authoritative information and the routing nodes subscribe to the zookeeper to get updates on shard mappings. TiDB uses [[Raft consensus protocol]]. Some others like Riak use [[Gossip Protocol]] where weak consistency is enough.

For secondary indexes use Global / local secondary index. Personally, local doesn't make sense. Global secondary index is basically storing the secondary index separately like the primary index and use it when required to do the lookup. Local is keeping secondary index for a shard within the shard itself. So will need to query each shard for reads on secondary index anyway but less update on updates as localised update is faster than global index update which may span a bigger chunk.

## Transaction

