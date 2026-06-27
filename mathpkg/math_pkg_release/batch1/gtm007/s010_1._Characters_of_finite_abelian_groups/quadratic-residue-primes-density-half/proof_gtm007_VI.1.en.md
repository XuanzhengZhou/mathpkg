---
role: proof
locale: en
of_concept: quadratic-residue-primes-density-half
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Assume $a$ is square-free and let $m = 4|a|$. By Proposition 5, there exists a nontrivial quadratic character $\chi_a$ modulo $m$ such that $\chi_a(p) = (a/p)$ for $p \nmid m$. The kernel $H = \ker \chi_a \subset G(m)$ has index 2, so $|H| = \phi(m)/2$.

A prime $p \nmid m$ satisfies $(a/p) = 1$ if and only if $\bar{p} \in H$. The set of such primes is a union of $\phi(m)/2$ residue classes modulo $m$, each having density $1/\phi(m)$ by Theorem 2. Hence the total density is $\phi(m)/2 \times 1/\phi(m) = 1/2$.
