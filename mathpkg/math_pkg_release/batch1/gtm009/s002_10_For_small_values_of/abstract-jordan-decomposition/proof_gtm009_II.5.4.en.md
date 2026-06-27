---
role: proof
locale: en
of_concept: abstract-jordan-decomposition
source_book: gtm009
source_chapter: "II"
source_section: "5.4"
---
Since $L$ is semisimple, $Z(L) = 0$, so the adjoint map $\operatorname{ad}: L \to \operatorname{ad} L$ is an isomorphism of Lie algebras. By Lemma B of (4.2), if $\mathfrak{A}$ is any $F$-algebra of finite dimension, then $\operatorname{Der} \mathfrak{A}$ contains the semisimple and nilpotent parts (in $\operatorname{End} \mathfrak{A}$) of all its elements. In particular, since $\operatorname{ad} L = \operatorname{Der} L$ (a theorem from 5.3 stating that for semisimple $L$, every derivation is inner), $\operatorname{ad} L$ is closed under the Jordan decomposition in $\operatorname{End} L$.

Given $x \in L$, decompose $\operatorname{ad} x = (\operatorname{ad} x)_s + (\operatorname{ad} x)_n$ in $\operatorname{End} L$ (usual Jordan decomposition). Since both parts lie in $\operatorname{ad} L$ (by the lemma above), and $\operatorname{ad}$ is injective, there exist unique $s, n \in L$ with $\operatorname{ad} s = (\operatorname{ad} x)_s$ and $\operatorname{ad} n = (\operatorname{ad} x)_n$. By construction, $\operatorname{ad} x = \operatorname{ad} s + \operatorname{ad} n = \operatorname{ad}(s + n)$, so $x = s + n$. Since $(\operatorname{ad} x)_s$ and $(\operatorname{ad} x)_n$ commute, $\operatorname{ad}[s, n] = [\operatorname{ad} s, \operatorname{ad} n] = 0$, so $[s, n] = 0$ by injectivity. We denote $x_s = s$ (ad-semisimple) and $x_n = n$ (ad-nilpotent).
