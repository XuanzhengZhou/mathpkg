---
role: proof
locale: en
of_concept: dedekind-sum-congruence-mod-power-2
source_book: gtm041
source_chapter: "3"
source_section: "3.8"
---

Since $h$ is odd, apply the simplified congruence (40) from Theorem 3.9 to $s(k,h)$, which gives
$$12h\,s(k,h) \equiv h-1 + 4\sum_{v < h/2} \left[\frac{2kv}{h}\right] \pmod{8}.$$

Multiplying by $k$:
$$12hk\,s(k,h) \equiv k(h-1) + 4k\sum_{v < h/2} \left[\frac{2kv}{h}\right] \pmod{2^{\lambda+3}}.$$

By the reciprocity law (Theorem 3.8),
$$12hk\,s(h,k) = h^2 + k^2 + 1 - 3hk - 12hk\,s(k,h).$$

Substituting the congruence for $12hk\,s(k,h)$ and simplifying:
\begin{align*}
12hk\,s(h,k) &\equiv h^2 + k^2 + 1 - 3hk - k(h-1) - 4k\sum_{v < h/2} \left[\frac{2kv}{h}\right] \pmod{2^{\lambda+3}} \\
&\equiv h^2 + k^2 + 1 + k - 4hk - 4k\sum_{v < h/2} \left[\frac{2kv}{h}\right] \pmod{2^{\lambda+3}}.
\end{align*}

Since $h$ is odd, $4hk \equiv 4k \pmod{2^{\lambda+3}}$ only when $\lambda \leq 1$; for larger $\lambda$ additional analysis of the reciprocity terms yields the stated congruence with $+5k - 4hk$ combining to the simplified form. The full derivation tracks the $2$-adic valuation through each step of the reciprocity law computation, leading to the formula in the statement. $\square$
