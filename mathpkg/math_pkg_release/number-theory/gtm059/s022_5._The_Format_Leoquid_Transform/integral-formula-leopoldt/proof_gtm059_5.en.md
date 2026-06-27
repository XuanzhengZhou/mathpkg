---
role: proof
locale: en
of_concept: integral-formula-leopoldt
source_book: gtm059
source_chapter: ""
source_section: "5"
---

By continuity in $s$, it suffices to prove the theorem when $s = k$ is an integer $> 1$ and $k \equiv s \pmod{p-1}$. Let $\chi$ be the characteristic function of $\mathbb{Z}_p^*$. Then

$$\int_{\mathbb{Z}_p^*} \omega^k(x) f^*(x) dx = \int_{\mathbb{Z}_p} \omega^k(x) \chi(x) f^*(x) dx.$$

By the properties of the $p$-adic integral, this equals

$$\Gamma_k(f \cdot \chi) = \Gamma_k(f)$$

since $\chi$ acts as a projection onto the $\omega^k$-eigenspace. The equality $\Gamma_k(f) = f^*(k)$ follows from the definition of the Leopoldt transform at integer arguments. This proves the theorem.
