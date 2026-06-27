---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Gödel number of a Markov algorithm is a natural number that uniquely encodes the entire algorithm. Each row $(a_i, b_i, c_i)$ of the algorithm is encoded as a product $2^{g a_i} \cdot 3^{g b_i} \cdot 5^{c_i}$, where $g a_i$ and $g b_i$ are the Gödel numbers of the words $a_i$ and $b_i$, and $c_i$ indicates whether the row is terminating. The algorithm's Gödel number is then obtained by taking the product of powers of consecutive primes, enabling the study of Markov algorithms within formal arithmetic.
