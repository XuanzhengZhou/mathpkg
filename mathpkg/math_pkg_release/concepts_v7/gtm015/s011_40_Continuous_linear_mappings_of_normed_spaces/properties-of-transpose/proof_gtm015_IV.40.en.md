---
role: proof
locale: en
of_concept: properties-of-transpose
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Algebraic and metric properties of the transpose of a continuous linear mapping

**Theorem (40.19).** Let $E$ and $F$ be normed spaces over $\mathbb{K}$, and let $S, T \in \mathcal{L}(E, F)$ and $\lambda \in \mathbb{K}$. Then:

(i) $(S + T)' = S' + T'$.
(ii) $(\lambda T)' = \lambda T'$.
(iii) $T'' x'' = (Tx)''$ for all $x \in E$.
(iv) $\|T'\| = \|T\|$.
(v) If $T$ is isometric and surjective, then so is $T'$.

**Proof.**

**(i), (ii)** Recall that for $T \in \mathcal{L}(E, F)$, the transpose $T': F' \to E'$ is defined by $T'g = g \circ T$ for all $g \in F'$. For any $g \in F'$ we have, citing the linearity of $g$:

$$(S + T)'g = g \circ (S + T) = g \circ S + g \circ T = S'g + T'g = (S' + T')g,$$

$$(\lambda T)'g = g \circ (\lambda T) = \lambda(g \circ T) = \lambda(T'g) = (\lambda T')g.$$

Thus $(S + T)' = S' + T'$ and $(\lambda T)' = \lambda T'$.

**(iii)** Let $x \in E$. Then $x'' \in E''$ and $Tx \in F$, therefore $T'' x'' \in F''$ and $(Tx)'' \in F''$, so $T'' x''$ and $(Tx)''$ are both elements of $F''$ and can be compared. For any $g \in F'$:

$$(T'' x'')(g) = (x'' \circ T')(g) = x''(T'g) = (T'g)(x) = (g \circ T)(x) = g(Tx) = (Tx)''(g).$$

Since this holds for all $g \in F'$, we conclude $T'' x'' = (Tx)''$.

**(iv)** For any $g \in F'$ with $\|g\| \leq 1$ and any $x \in E$ with $\|x\| \leq 1$,

$$|(T'g)(x)| = |g(Tx)| \leq \|g\| \cdot \|Tx\| \leq \|Tx\| \leq \|T\| \cdot \|x\| \leq \|T\|.$$

Thus $\|T'g\| = \sup\{|(T'g)(x)| : \|x\| \leq 1\} \leq \|T\|$, and consequently $\|T'\| = \sup\{\|T'g\| : \|g\| \leq 1\} \leq \|T\|$.

Conversely, for any $x \in E$ with $\|x\| \leq 1$, by the Hahn-Banach theorem for normed spaces (40.10) applied to $Tx$ in $F$, there exists $g \in F'$ with $\|g\| = 1$ and $g(Tx) = \|Tx\|$ (if $Tx \neq \theta$; if $Tx = \theta$, the inequality $\|Tx\| \leq \|T'\|$ is trivial). Then

$$\|Tx\| = g(Tx) = (T'g)(x) \leq \|T'g\| \cdot \|x\| \leq \|T'\| \cdot \|g\| \cdot \|x\| \leq \|T'\|.$$

Taking the supremum over $\|x\| \leq 1$ gives $\|T\| \leq \|T'\|$. Therefore $\|T'\| = \|T\|$.

**(v)** If $T: E \to F$ is isometric and surjective, then $T$ is bijective with $\|Tx\| = \|x\|$ for all $x$. Since $T$ is surjective, $T'$ is injective: if $T'g = 0$, then $g \circ T = 0$, and for any $y \in F$, writing $y = Tx$, we have $g(y) = g(Tx) = 0$, so $g = 0$. Moreover, for any $g \in F'$, $\|T'g\| = \sup_{\|x\|\leq 1}|g(Tx)| = \sup_{\|x\|\leq 1}|g(Tx)|$. Since $T$ is isometric and surjective, $\{Tx : \|x\| \leq 1\} = \{y \in F : \|y\| \leq 1\}$, so $\|T'g\| = \sup_{\|y\|\leq 1}|g(y)| = \|g\|$. Thus $T'$ is isometric. To see that $T'$ is surjective: given $h \in E'$, define $g \in F'$ by $g(y) = h(T^{-1}y)$; then $T'g = g \circ T = h$.
