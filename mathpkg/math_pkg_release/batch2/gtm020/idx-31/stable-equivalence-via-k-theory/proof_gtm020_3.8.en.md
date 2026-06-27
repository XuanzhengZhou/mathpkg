---
role: proof
locale: en
of_concept: stable-equivalence-via-k-theory
source_book: gtm020
source_chapter: "3"
source_section: "3.8"
---

**Proof.** Let $\alpha: \text{Vect}_F(X) \to K_F(X)$ be the canonical map to the Grothendieck group (or ring) completion of the semiring $\text{Vect}_F(X)$.

($\Rightarrow$) Suppose $\alpha(\xi) = \alpha(\eta)$ in $K_F(X)$. Since $K_F(X)$ is the group completion, equality $\alpha(\xi) = \alpha(\eta)$ means that there exist nonnegative integers $m, n, q$ such that
$$
\xi \oplus \theta^m \oplus \theta^q = \xi \oplus \theta^{m+q}
$$
and
$$
\eta \oplus \theta^n \oplus \theta^q = \eta \oplus \theta^{n+q}
$$
are isomorphic as vector bundles over $X$. Thus $\xi \oplus \theta^{m+q} \cong \eta \oplus \theta^{n+q}$, which is precisely the condition that $\xi$ and $\eta$ are $s$-equivalent.

($\Leftarrow$) Conversely, suppose $\xi$ and $\eta$ are $s$-equivalent, so there exist $n, m$ such that $\xi \oplus \theta^n$ and $\eta \oplus \theta^m$ are isomorphic over $X$. Then
$$
\alpha(\xi \oplus \theta^n) = \alpha(\eta \oplus \theta^m).
$$
Since the completion map $\alpha$ satisfies $\alpha(\zeta \oplus \theta^q) = \alpha(\zeta)$ for any bundle $\zeta$ and any $q$ (adding a trivial bundle does not change the class in the group completion), we obtain
$$
\alpha(\xi) = \alpha(\xi \oplus \theta^n) = \alpha(\eta \oplus \theta^m) = \alpha(\eta).
$$

Thus $\alpha(\xi) = \alpha(\eta)$ if and only if $\xi$ and $\eta$ are $s$-equivalent. $\square$
