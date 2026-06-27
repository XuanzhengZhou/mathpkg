---
role: proof
locale: en
of_concept: galois-action-algebraic-integer-theorem
source_book: gtm059
source_chapter: "1"
source_section: "1. Character Sums"
---

Fix $x$ and view $x^n$ as an integer. Using Fourier inversion on the finite abelian group $(\mathbb{Z}/m\mathbb{Z})^\times$, the Fourier coefficients $A_j$ are known to be integers. The condition $u \equiv 1 \pmod{m}$ implies that $A_j(u) \equiv A_j(1) \pmod{m}$. From the definition, this yields that $\alpha(0)$ is an algebraic integer for all characters. Furthermore, for $d$ coprime to $m$, the character sum $s_d(u)$ satisfies $s_d(u) = \alpha(0)$. By the Plancherel formula, $\sum |d(u)|^2 = \sum |\alpha_k|^2$, and since $|w(u)|^2 = 1$ with $\alpha(k)$ being integers, it follows that $\alpha(k)$ is non-zero for exactly one value and zero otherwise. This forces $w(\alpha, u) = 1$.
