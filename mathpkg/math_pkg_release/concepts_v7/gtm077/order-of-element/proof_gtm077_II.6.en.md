---
role: proof
locale: en
of_concept: order-of-element
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Theorem 20: Order of an Element

**Theorem 20.** For each element $A$ of a finite group $\mathfrak{G}$, there exists a uniquely determined positive integer $a$, the *order* of $A$, such that $A^r = E$ if and only if $a \mid r$. For any positive integer $m$, the order of $A^m$ equals $a/(a, m)$, where $(a, m)$ denotes the greatest common divisor.

**Proof of the first part.** Let $S = \{q \in \mathbb{Z} : A^q = E\}$. Since $\mathfrak{G}$ is finite, there exist $m > n$ with $A^m = A^n$, so $A^{m-n} = E$ with $m-n > 0$. Thus $S$ contains positive integers.

If $q, r \in S$, then $A^{q+r} = A^q A^r = E$ and $A^{-q} = (A^q)^{-1} = E$, so $S$ is a submodule of $\mathbb{Z}$. By Theorem 1, every submodule of $\mathbb{Z}$ is of the form $a\mathbb{Z}$ for a unique $a \geq 0$. Since $S$ contains positive integers, $a > 0$. Then $A^r = E$ iff $r \in a\mathbb{Z}$ iff $a \mid r$.

**Proof of the second part.** Let $a$ be the order of $A$ and let $d = (a, m)$. We claim the order of $A^m$ is $a/d$.

First, $(A^m)^{a/d} = A^{m \cdot a/d} = (A^a)^{m/d} = E^{m/d} = E$, since $m/d$ is an integer. So the order of $A^m$ divides $a/d$.

Conversely, suppose $(A^m)^k = E$. Then $A^{mk} = E$, so $a \mid mk$. Dividing by $d = (a, m)$: since $(a/d, m/d) = 1$, we have $a/d \mid k \cdot (m/d)$, which implies $a/d \mid k$ (because $a/d$ and $m/d$ are coprime). Thus $k$ is a multiple of $a/d$.

Hence the smallest positive $k$ with $(A^m)^k = E$ is $a/d$. The order of $A^m$ is $a/(a, m)$. ∎
