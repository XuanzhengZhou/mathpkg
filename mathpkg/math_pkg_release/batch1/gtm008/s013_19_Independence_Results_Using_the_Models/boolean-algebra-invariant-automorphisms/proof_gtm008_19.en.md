---
role: proof
locale: en
of_concept: boolean-algebra-invariant-automorphisms
source_book: gtm008
source_chapter: "19"
source_section: "19"
---

Let $b \in B$ with $0 < b < 1$. Then there exist $p, q \in P$ such that $[p] \subseteq b$ and $[q] \subseteq -b$. By Theorem 11.6, there exists $\pi \in \operatorname{Aut}(P)$ such that $\pi(p)$ and $q$ are compatible. Extending $\pi$ to an automorphism of $B$ (also denoted $\pi$), we have

$$\pi(b) \cdot (-b) \geq \pi([p]) \cdot [q] = [\pi(p)] \cdot [q] > 0.$$

Therefore $\pi(b) \neq b$. Since any non-trivial element $b$ is moved by some automorphism, the only elements invariant under all automorphisms are $0$ and $1$.
