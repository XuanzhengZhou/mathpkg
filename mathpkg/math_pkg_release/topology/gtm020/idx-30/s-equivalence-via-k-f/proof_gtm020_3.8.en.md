---
role: proof
locale: en
of_concept: s-equivalence-via-k-f
source_book: gtm020
source_chapter: "3"
source_section: "3.8"
---

Suppose $X$ satisfies property $(S)$, i.e., every vector bundle over $X$ has an inverse with respect to Whitney sum up to trivial bundles. Let $\alpha: \operatorname{Vect}_F(X) \to K_F(X)$ be the canonical map into the ring completion.

First, we show that $\alpha$ is constant on $s$-equivalence classes. If $\xi \sim_s \eta$, then there exist integers $m, n$ such that $\xi \oplus \theta^m \cong \eta \oplus \theta^n$. In $K_F(X)$, the class of a trivial bundle $\theta^k$ equals $k$ times the unit element, and since $\alpha$ is a semiring homomorphism, we have $\alpha(\xi \oplus \theta^m) = \alpha(\xi) + \alpha(\theta^m)$ and similarly for $\eta$. The isomorphism $\xi \oplus \theta^m \cong \eta \oplus \theta^n$ implies $\alpha(\xi) + \alpha(\theta^m) = \alpha(\eta) + \alpha(\theta^n)$. Since $\alpha(\theta^m)$ and $\alpha(\theta^n)$ are identified in the group completion (they correspond to the rank), we obtain $\alpha(\xi) = \alpha(\eta)$ in $K_F(X)$.

Conversely, suppose $\alpha(\xi) = \alpha(\eta)$ in $K_F(X)$. Since $K_F(X)$ is the group completion of the semiring $\operatorname{Vect}_F(X)$, there exist vector bundles $\zeta$ such that $\xi \oplus \zeta \cong \eta \oplus \zeta$. By property $(S)$, there exists a bundle $\zeta'$ with $\zeta \oplus \zeta' \cong \theta^k$ for some $k$. Adding $\zeta'$ to both sides yields $\xi \oplus \theta^k \cong \eta \oplus \theta^k$, hence $\xi$ and $\eta$ are $s$-equivalent. More directly: in the group completion, equality $\alpha(\xi) = \alpha(\eta)$ means there exists some $\zeta$ such that $\xi \oplus \zeta \cong \eta \oplus \zeta$. Adding a complement $\zeta'$ (using property $(S)$) gives $\xi \oplus \theta^k \cong \eta \oplus \theta^k$, so $\xi \sim_s \eta$.

Thus $\alpha$ descends to a well-defined bijection from the set of $s$-equivalence classes onto $K_F(X)$. This proves the theorem.
