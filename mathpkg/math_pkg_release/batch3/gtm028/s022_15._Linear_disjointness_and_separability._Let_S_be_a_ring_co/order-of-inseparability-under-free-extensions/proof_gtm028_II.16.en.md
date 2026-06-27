---
role: proof
locale: en
of_concept: order-of-inseparability-under-free-extensions
source_book: gtm028
source_chapter: "II"
source_section: "§16. Order of inseparability"
---

**Proof.** If $K$ is a finite extension of $k$, then (6) and (7) show that the purely inseparable parts behave well. Let $k'$ be the maximal separable extension of $k$ in $K$, so that $[K:k]_i = [K:k']$ and $K/k'$ is purely inseparable. Then $k'(x)/k'$ has the same order of inseparability behavior. Hence $[K(x):K]_i = [k'(x):k']_i$. We now have, for any transcendence basis $\{z\}$ of $k(x)/k$:

$$[k(x):k(z)]_i = p^s[k'(x):k'(z)]_i = p^s[K(x):K(z)]_i,$$

where

$$p^s = \frac{[k(x):k]_i}{[k'(x):k']_i} = \frac{[k(x):k]_i}{[K(x):K]_i},$$

and this establishes the theorem in the case where $K$ is an algebraic extension of $k$.

In the general case we consider a transcendence basis $B$ of $K/k$. Since $K$ and $k(x)$ are free over $k$, the elements of $B$ are algebraically independent over $k(x)$. Hence by Corollary 1 of Lemma 1 we have

$$[k(B,x):k(B,z)]_i = [k(x):k(z)]_i$$

for any transcendence basis $\{z\}$ of $k(x)/k$. Hence

$$[k(B,x):k(B)]_i = [k(x):k]_i.$$

Since $K$ is an algebraic extension of $k(B)$, we have by the preceding case:

$$[k(B,x):k(B,z)]_i = p^s[K(x):K(z)]_i,$$

where

$$p^s = \frac{[k(B,x):k(B)]_i}{[K(x):K]_i},$$

and from this the theorem follows in view of the two equalities above.
