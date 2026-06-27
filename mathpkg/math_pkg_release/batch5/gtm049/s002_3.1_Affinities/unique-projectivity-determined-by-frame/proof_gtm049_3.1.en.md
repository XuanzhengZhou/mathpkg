---
role: proof
locale: en
of_concept: unique-projectivity-determined-by-frame
source_book: gtm049
source_chapter: "3"
source_section: "3.1 Affinities"
---

Suppose that the simplex $(A_0, \ldots, A_n)$ and the unit point $U$ are given. Let $a_0, \ldots, a_n$ be any homogeneous vectors for $A_0, \ldots, A_n$, respectively (i.e., $[a_i] = A_i$ for $i = 0, \ldots, n$). Then there is a unique isomorphism $f$ of $V$ onto $F^{n+1}$ taking $a_i$ to $e_i$ for each $i$, and the projectivity $\pi = \mathcal{P}(f)$ certainly takes $A_i$ to $[e_i]$ for $i = 0, \ldots, n$.

To ensure $U\pi = [e_0 + \cdots + e_n]$, we choose the homogeneous vectors so that $u = a_0 + \cdots + a_n$ represents $U$. By Lemma 1, such a choice exists: if $u$ is any homogeneous vector for $U$ and $c_0, \ldots, c_n$ are any homogeneous vectors for $A_0, \ldots, A_n$, we can write $u = x_0 c_0 + \cdots + x_n c_n$ with $x_i \neq 0$ and set $a_i = x_i c_i$, giving $[a_i] = A_i$ and $u = a_0 + \cdots + a_n$. Uniqueness follows from Proposition 1: if $f$ and $g$ are two isomorphisms taking $a_i$ to $e_i$, they must differ by a scalar, but the condition on the unit point forces the scalar to be $1$.
