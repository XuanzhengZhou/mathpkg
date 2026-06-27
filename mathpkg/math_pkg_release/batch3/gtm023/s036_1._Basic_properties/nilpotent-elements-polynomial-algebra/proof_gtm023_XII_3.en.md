---
role: proof
locale: en
of_concept: nilpotent-elements-polynomial-algebra
source_book: gtm023
source_chapter: "XII"
source_section: "3"
---

Suppose $f(a)$ is nilpotent: $f(a)^m = 0$ for some $m$. Then $\Phi(f^m) = f(a)^m = 0$, so $\mu \mid f^m$. With prime factorization $\mu = \prod f_i^{k_i}$, we have $g = \prod f_i \mid \mu \mid f^m$. By Proposition IV (sec. 12.9), since $g$ is a product of relatively prime irreducibles, $g \mid f$.

Conversely, assume $g \mid f$. Let $k = \max(k_1, \ldots, k_r)$. Then $\mu \mid g^k \mid f^k$. Hence $\Phi(f^k) = f(a)^k = 0$, so $f(a)$ is nilpotent.

If all $k_i = 1$, then $\mu = g$, so $f(a)$ is nilpotent iff $\mu \mid f$, i.e., $f(a) = 0$. Thus no non-zero nilpotent elements exist.
