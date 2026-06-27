---
role: proof
locale: en
of_concept: godel-numbers-of-markov-algorithms-elementary
source_book: gtm037
source_chapter: "4. Recursive Function Theory"
source_section: "4.1"
---

**Proof.** $n$ is the Gödel number of a Markov algorithm iff $n \geq 2$ and
$$\forall i \leq \operatorname{lh} n \left[ ((n)_i)_0 \text{ and } ((n)_i)_1 \text{ are Gödel numbers of words, } ((n)_i)_2 \leq 1, \text{ and } \operatorname{lh}((n)_i) \leq 2 \right].$$

Here $\operatorname{lh} n$ denotes the length (number of prime factors) of $n$, $(n)_i$ denotes the exponent of the $i$-th prime in the factorization of $n$, and $((n)_i)_j$ denotes the $j$-th component of the encoding of the $i$-th row. The conditions state that each row $(a_i, b_i, c_i)$ consists of Gödel numbers of words $a_i$ and $b_i$ plus a bit $c_i \leq 1$, and that the encoding of each row uses at most two primes (for the triple encoding). Since the property of being a Gödel number of a word is elementary, and all quantifiers are bounded, the defining formula is elementary.
