---
role: proof
locale: en
of_concept: complete-reducibility-criterion-single-transformation
source_book: gtm031
source_chapter: "II"
source_section: "7"
---

($\Rightarrow$) Suppose $A$ is completely reducible. Then by Theorem 2, $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2 \oplus \cdots \oplus \mathfrak{R}_s$ where the $\mathfrak{R}_i$ are invariant and irreducible. By Theorem 3, the minimum polynomial of $A$ restricted to each irreducible component $\mathfrak{R}_i$ is a prime $\pi_i(\lambda)$. The minimum polynomial $\mu(\lambda)$ of $A$ on $\mathfrak{R}$ is the least common multiple of the $\pi_i(\lambda)$. Since each $\pi_i$ is irreducible, their lcm is simply the product of the distinct $\pi_i$ that appear. Hence $\mu(\lambda)$ is a product of distinct primes.

($\Leftarrow$) Conversely, suppose the minimum polynomial $\mu(\lambda)$ of $A$ is a product of distinct primes. Then each invariant factor of $A$ divides $\mu(\lambda)$ and is therefore also a product of distinct primes. By the rational canonical form theorem, each invariant factor corresponds to a cyclic summand whose minimum polynomial is that invariant factor. A cyclic summand with minimum polynomial a product of distinct primes decomposes further into a direct sum of irreducible summands (by the primary decomposition theorem, since distinct prime factors yield a decomposition into primary components, each of which is irreducible because the minimum polynomial restricted to the primary component is a prime). Thus $\mathfrak{R}$ decomposes as a direct sum of irreducible invariant subspaces, and by Theorem 2, $A$ is completely reducible. $\square$
