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

## Data transfer models

Generally most data is transferred via JSON or XML. JSON, by virtue of being string oriented has trouble parsing non-standard values. For example handling numbers greater than $2^{53}$ in floating point. One way around it was to encode everything as string and convert to base 64.  
