---
role: proof
locale: en
of_concept: cantorschröderbernstein
source_book: gtm001
source_chapter: "9"
source_section: ""
---

If $a \simeq c \subseteq b$, then $\bar{a} = \bar{c} \leq \bar{b}$. If $b \simeq d \subseteq a$, then $\bar{b} = \bar{d} \leq \bar{

On the other hand, suppose that $(\forall n)[y \notin f"h'n]$. As we will now show, it then follows that $(\forall n)[g'y \notin h'n]$. Assume that this is not the case. Then $(\exists n)[g'y \in h'n]$. Since $h'0 = a - d$ and since $g'y \in d$ it follows that $n \neq 0$. Therefore $(\exists m)[n = m + 1]$. But $h'(m + 1) = g"f"h'm$ and $g'y \in h'(m + 1)$. Since $g$ is one-to-one it then follows that $y \in f"h'm$; but this is a contradiction. And from this contradiction we conclude that $(\forall n)[g'y \notin h'n]$. On the other hand since $y \in b$, it follows that $g'y \in a$. Therefore $F'g'y = (g^{-1})g'y = y$. From this we conclude that $F$ is onto, that is, $\mathcal{W}(F) = b$.

To prove that $F$ is one-to-one assume that $x \in a, y \in a$, and $F'x = F'y$. From this we will first prove that $(\exists m)[x \in h'm]$ iff $(\exists m)[y \in h'm]$. The proof is by contradiction: Suppose that $x \in h'm$ and $(\forall n)[y \notin h'n]$. Then $F'x = F'y$ implies that $f'x = (g^{-1})y$ and hence $y = (g \circ f)'x$. Since $x \in h'm$ it then follows that $y \in (g \circ f)'h'm = h'(m + 1)$. This is a contradiction. Similarly we can prove that $y \in h'm$ and $(\forall n)[x \notin h'n]$ implies that $x \in h'(m + 1)$. This too is a contradiction. From these contradictions we conclude that $(\exists m)[x \in h'm]$ iff $(\exists m)[y \

Remark. In the foregoing argument the proof that $\alpha$ is not equivalent to $\mathcal{P}(\alpha)$ can be easily modified to prove, of any set $a$, that $a$ and $\mathcal{P}(a)$ are not equivalent. Furthermore this proof does not require AC.

From Cantor's theorem it is easy to prove that for any set of cardinal numbers there exists a cardinal larger than each cardinal in the given set.
