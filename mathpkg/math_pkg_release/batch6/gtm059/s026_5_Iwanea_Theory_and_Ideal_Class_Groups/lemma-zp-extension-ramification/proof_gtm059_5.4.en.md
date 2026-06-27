---
role: proof
locale: en
of_concept: lemma-zp-extension-ramification
source_book: gtm059
source_chapter: "5"
source_section: "4"
---

*Proof.* Let $\mathfrak{p}$ be a prime of $K$ that ramifies in $K_\infty$. Since $[K_n : K] = p^n$, the ramification index $e_n = e(\mathfrak{p}, K_n/K)$ divides $p^n$. If $\mathfrak{p}$ ramifies in $K_\infty$, the ramification index must grow without bound as $n \to \infty$, hence $e_n = p^{m_n}$ with $m_n \to \infty$. On the other hand, only finitely many primes can ramify in the whole tower because each ramified prime contributes a factor to the discriminant, and the discriminant of $K_n/K$ is bounded by a power of $p$ only for finitely many primes.

For (i): The discriminant $\operatorname{disc}(K_n/K)$ divides $p^{n \cdot \text{const}}$ times the contribution from ramified primes. Since the $p$-part of the class number is finite, only finitely many primes can appear in the discriminant tower.

For (ii): Suppose $\mathfrak{p}$ ramifies. Let $e_n$ be the ramification index in $K_n/K$. Then $e_n \mid p^n$ and $e_n \leq e_{n+1}$. Since $e_n$ is a power of $p$ that cannot grow indefinitely (by local class field theory, the inertia group is a quotient of the local unit group), it stabilizes. Being non-trivial, it must be $p^{n - n_0}$ for $n \geq n_0$, which means the ramification is total from level $n_0$ onward.

For (iii): If $K_\infty / K$ were everywhere unramified, then $K_\infty$ would be contained in the Hilbert class field tower of $K$, which is a finite extension. But $K_\infty$ has infinite degree over $K$, contradiction.
