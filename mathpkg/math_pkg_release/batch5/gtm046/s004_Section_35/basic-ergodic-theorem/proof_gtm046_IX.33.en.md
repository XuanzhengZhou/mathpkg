---
role: proof
locale: en
of_concept: basic-ergodic-theorem
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

The invariant event $D=[\liminf X^n/Y^n\neq\limsup X^n/Y^n]=\bigcup_{a,b}C_{ab}$ where $C_{ab}=[\liminf<a<b<\limsup]$ with $a<b$ rationals. Set $Z^n=Y^n$ in the basic ergodic inequality with $C=C_{ab}=B^m C_{ab}+A^m$. By invariance, $C_{ab}=B_k^m C_{ab}+A_k^m$. The inequality becomes
$$\int_{C_{ab}}(X^n/Y^n-b)-\sum_{k=1}^n\int_{A_k^m}(X_k/Y^n-bY_k/Y^n)+\sum_{k=n+1}^{n+m}\int_{C_{ab}}(X_k/Y^n-bY_k/Y^n)^+\geq 0.$$
Changing $X_k\to -X_k$, $b\to -a$ gives $\liminf\int_{C_{ab}}(a-X^n/Y^n)\geq 0$. Adding yields $(a-b)P(C_{ab})\geq 0$ with $a<b$, so $P(C_{ab})=0$. For B', divide by $Z^n$ throughout.
