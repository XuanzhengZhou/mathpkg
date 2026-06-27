---
role: proof
locale: en
of_concept: elementary-prime-function
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

Let $\text{PM}$ denote the set of prime numbers, which is elementary. Define the relation $N$ of consecutive primes:
$$N = \{(x, y) : x, y \in \text{PM}, \; x < y, \text{ and } y \text{ is the next prime after } x\}.$$
This can be expressed as
$$N = \{(x, y) : x, y \in \text{PM} \text{ and } x < y \text{ and for all } z < y, \text{ either } z \leq x \text{ or } z \notin \text{PM}\},$$
so $N$ is elementary by closure under bounded quantifiers.

Now define the relation $Pr$ that pairs a prime with its index:
$$Pr = \{(x, k) : x \text{ is the } (k+1)\text{st prime}\}.$$
Then $(x, k) \in Pr$ iff $x \in \text{PM}$ and $\sum_{y < x} \chi_{\text{PM}}(y) = k$, so $Pr$ is elementary.

Finally,
$$p_k = \mu x < \exp(2, 2^k) + 1 \; ((x, k) \in Pr).$$
Since $\exp(2, 2^k) = 2^{2^k}$ provides an upper bound for the $(k+1)$-st prime, and the bounded $\mu$-operator preserves elementarity, $p$ is elementary.
