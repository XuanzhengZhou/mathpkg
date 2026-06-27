---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Lemma 16.4 is a stepping stone toward Lagrange's four-square theorem. It states that for every odd prime $p$, there exists a positive integer $m < p$ such that $mp$ can be expressed as a sum of four integer squares. The proof uses a pigeonhole principle argument on quadratic residues modulo $p$: the sets $\{x^2 \bmod p : 0 \leq x \leq (p-1)/2\}$ and $\{-1 - y^2 \bmod p : 0 \leq y \leq (p-1)/2\}$ must intersect, yielding $x^2 + y^2 + 1 = mp$ for some $x, y$ and $m \geq 1$.
