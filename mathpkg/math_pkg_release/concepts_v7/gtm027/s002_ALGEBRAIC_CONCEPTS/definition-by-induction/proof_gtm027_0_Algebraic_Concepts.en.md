---
role: proof
locale: en
of_concept: definition-by-induction
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 13: Definition by Induction (Recursion Theorem)

**Theorem 13.** Suppose $a$ is given and $F(g)$ is given whenever $g$ is a function whose domain is of the form $\omega_p = \{q : q \in \omega \text{ and } q \leq p\}$ for some $p$ in $\omega$. Then there is a unique function $f$ such that $f(0) = a$ and $f(p+1) = F(f \mid \omega_p)$ for each $p$ in $\omega$.

*Proof.* Let $\mathfrak{F}$ be the family of all functions $g$ such that the domain of $g$ is a set $\omega_p$ for some $p$ in $\omega$, $g(0) = a$, and $g(q+1) = F(g \mid \omega_q)$ whenever $q+1$ belongs to the domain of $g$. Observe that if $g$ and $h$ belong to $\mathfrak{F}$ and $q$ belongs to the domain of both, then $g(q) = h(q)$ (this follows by induction on $q$). Then let $f = \bigcup \{g : g \in \mathfrak{F}\}$. It follows from the preceding observation that $f$ is a function. Moreover, if $q+1$ belongs to the domain of $f$, then for some $g$ in $\mathfrak{F}$, $q+1$ is a member of the domain of $g$, and hence $f(q+1) = g(q+1) = F(g \mid \omega_q) = F(f \mid \omega_q)$. Finally, to show that the domain of $f$ is $\omega$, suppose that $q$ is the first member of $\omega$ which is not in the domain of $f$. Then $q-1$ is the last member of the domain of $f$, and $f \cup \{(q, F(f))\}$ is a member of $\mathfrak{F}$. Hence $q$ belongs to the domain of $f$, which is a contradiction. The uniqueness of $f$ follows from the observation that any two such functions agree on their common domain by induction.
