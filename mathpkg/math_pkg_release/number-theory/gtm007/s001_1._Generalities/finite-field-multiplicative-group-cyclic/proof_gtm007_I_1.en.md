---
role: proof
locale: en
of_concept: finite-field-multiplicative-group-cyclic
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

If $d$ is an integer $\geq 1$, recall that $\phi(d)$ denotes the Euler $\phi$-function, i.e. the number of integers $x$ with $1 \leq x \leq d$ which are prime to $d$ (in other words, whose image in $\mathbb{Z}/d\mathbb{Z}$ is a generator of this group). It is clear that the number of generators of a cyclic group of order $d$ is $\phi(d)$.

\textbf{Lemma 1.} If $n$ is an integer $\geq 1$, then $n = \sum_{d \mid n} \phi(d)$.

If $d$ divides $n$, let $C_d$ be the unique subgroup of $\mathbb{Z}/n\mathbb{Z}$ of order $d$, and let $\Phi_d$ be the set of generators of $C_d$. Since every element of $\mathbb{Z}/n\mathbb{Z}$ generates one of the $C_d$, the group $\mathbb{Z}/n\mathbb{Z}$ is the disjoint union of the $\Phi_d$. Thus

$$n = \operatorname{Card}(\mathbb{Z}/n\mathbb{Z}) = \sum_{d \mid n} \operatorname{Card}(\Phi_d) = \sum_{d \mid n} \phi(d),$$

which proves Lemma 1.

\textit{Proof of Theorem 2.} Let $n = q-1$ be the order of $\mathbf{F}_q^*$. For every divisor $d$ of $n$, let $\psi(d)$ be the number of elements of order $d$ in $\mathbf{F}_q^*$. If such an element exists, it generates a cyclic subgroup of order $d$, which has $\phi(d)$ generators. Hence $\psi(d)$ is either $0$ or $\phi(d)$. Since every element has some order dividing $n$, we have

$$n = \sum_{d \mid n} \psi(d).$$

But by Lemma 1, $n = \sum_{d \mid n} \phi(d)$. Hence $\psi(d) = \phi(d)$ for every $d \mid n$. In particular, $\psi(n) = \phi(n) \geq 1$, so there exists an element of order $n = q-1$. Therefore $\mathbf{F}_q^*$ is cyclic.
