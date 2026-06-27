---
role: proof
locale: en
of_concept: "multiplicative-group-finite-field-cyclic"
source_book: gtm007
source_chapter: "I"
source_section: "1.2"
---
If $d$ is an integer $\geq 1$, recall that $\phi(d)$ denotes the Euler $\phi$-function. The number of generators of a cyclic group of order $d$ is $\phi(d)$.

**Lemma 1.** If $n \geq 1$, then $n = \sum_{d | n} \phi(d)$.

Let $C_d$ be the unique subgroup of $\mathbb{Z}/n\mathbb{Z}$ of order $d$ (if $d$ divides $n$). Every element of $\mathbb{Z}/n\mathbb{Z}$ generates one of the $C_d$, so $n = \sum_{d|n} \phi(d)$.

Now let $\mathbb{F}_q^*$ have order $q-1$. For each $d | (q-1)$, let $\psi(d)$ be the number of elements of order $d$ in $\mathbb{F}_q^*$. If $\psi(d) > 0$, let $x$ have order $d$; the cyclic group $\langle x \rangle$ contains all $d$ roots of $X^d - 1 = 0$, hence all elements of order $d$ are in $\langle x \rangle$, so $\psi(d) = \phi(d)$. Thus $q-1 = \sum_{d|(q-1)} \psi(d) \leq \sum_{d|(q-1)} \phi(d) = q-1$, forcing $\psi(d) = \phi(d)$ for all $d$. In particular $\psi(q-1) = \phi(q-1) > 0$, so a generator exists.
