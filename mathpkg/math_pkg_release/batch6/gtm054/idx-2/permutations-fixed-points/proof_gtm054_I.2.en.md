---
role: proof
locale: en
of_concept: permutations-fixed-points
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

Let $B$ be an $n$-set and define $f: B \to \mathcal{P}(\Pi(B))$ by $f(b) = \{\varphi \in \Pi(B) : \varphi(b) = b\}$. Then $(\Pi(B), f, B)$ is a system. A permutation $\varphi$ belongs to block $b$ if and only if $b$ is a fixed point of $\varphi$. Thus we seek the number of vertices (permutations) lying in exactly $r$ blocks. This is given by Theorem E13(a).

First, by E8(d), if $A \subseteq B$, then $\overline{s^*}(A)$ is the number of permutations of $B$ which fix $A$ pointwise, which is $(|B| - |A|)! = (n - |A|)!$. Hence
$$\sum_{|A|=r+i} \overline{s^*}(A) = \binom{n}{r+i} (n - (r+i))! = \frac{n!}{(r+i)!}.$$

Substituting into E13(a):
\begin{align*}
\sum_{i=0}^{n-r} (-1)^i \binom{r+i}{i} \frac{n!}{(r+i)!} &= \frac{n!}{r!} \sum_{i=0}^{n-r} \frac{(-1)^i}{i!}.
\end{align*}
