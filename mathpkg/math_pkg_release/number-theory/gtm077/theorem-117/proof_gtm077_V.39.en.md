---
role: proof
locale: en
of_concept: theorem-117
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 117

**Theorem 117.** Let $\mathfrak{p}$ be a prime ideal of $k$ and let $K = k(\sqrt[l]{\mu})$ have relative degree $l$ over $k$. Only the following possibilities exist for the behavior of $\mathfrak{p}$ under passage to $K$:

- $\mathfrak{p}$ remains a prime ideal in $K$,
- $\mathfrak{p}$ becomes the $l$-th power of a prime ideal in $K$,
- $\mathfrak{p}$ becomes the product of $l$ distinct prime ideals in $K$.

**Proof.** Let $\mathfrak{P}$ be a prime ideal in $K$ dividing $\mathfrak{p}$. By Theorem 107, the relative norm of $\mathfrak{P}$ is

$$\mathfrak{P} \cdot s\mathfrak{P} \cdots s^{l-1}\mathfrak{P} = \mathfrak{p}^{f_1},$$

where $f_1$ is the relative degree of $\mathfrak{P}$ and $s$ generates the Galois group of $K/k$ (which is cyclic of order $l$). Thus no prime ideal other than the conjugates $s^m\mathfrak{P}$ can divide $\mathfrak{p}$.

Now there are two cases:

**Case 1.** $\mathfrak{P}$ is equal to one of its nontrivial conjugates $s^m\mathfrak{P}$ ($m \not\equiv 0 \pmod{l}$). Then, since $s$ has order $l$ and $l$ is prime, $\mathfrak{P}$ is equal to all of its conjugates: $\mathfrak{P} = s\mathfrak{P} = \cdots = s^{l-1}\mathfrak{P}$. The relative norm formula then gives $\mathfrak{P}^l = \mathfrak{p}^{f_1}$. Since $\mathfrak{p}$ is prime in $k$ and $\mathfrak{P}$ is prime in $K$, this forces $\mathfrak{P}^l = \mathfrak{p}$, i.e., $f_1 = 1$ and $\mathfrak{p}$ becomes the $l$-th power of $\mathfrak{P}$ in $K$.

**Case 2.** $\mathfrak{P}$ is distinct from all its conjugates $s^m\mathfrak{P}$ ($m \not\equiv 0 \pmod{l}$). Then the $l$ ideals $\mathfrak{P}, s\mathfrak{P}, \ldots, s^{l-1}\mathfrak{P}$ are pairwise distinct. By the relative norm formula, their product is $\mathfrak{p}^{f_1}$. Since these $l$ distinct prime ideals all divide $\mathfrak{p}$, we must have $f_1 = 1$ and

$$\mathfrak{p} = \mathfrak{P} \cdot s\mathfrak{P} \cdots s^{l-1}\mathfrak{P},$$

so $\mathfrak{p}$ splits into the product of $l$ distinct prime ideals in $K$.

The remaining case (that $\mathfrak{p}$ remains prime in $K$) corresponds to $f_1 = l$, which occurs when $\mathfrak{P} = \mathfrak{p}$ (i.e., the extension of $\mathfrak{p}$ to $K$ is itself a prime ideal).
