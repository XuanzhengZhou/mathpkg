---
role: proof
locale: en
of_concept: stone-cech-extension-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Compactification"
---

# Proof of the Stone–Čech Extension Theorem

**Theorem 24 (Stone–Čech).** If $X$ is a Tychonoff space and $f$ is a continuous function on $X$ to a compact Hausdorff space $Y$, then there is a continuous extension of $f$ which carries the compactification $\beta(X)$ into $Y$. More precisely, if $(e, \beta(X))$ is the Stone–Čech compactification, then $f \circ e^{-1}$ can be extended to a continuous function on $\beta(X)$ to $Y$.

*Proof.* Recall the setup: $F(X)$ is the family of all continuous functions on $X$ to the closed unit interval $Q = [0,1]$. The cube $Q^{F(X)}$ is compact by the Tychonoff theorem. The evaluation map $e: X \to Q^{F(X)}$ is defined by $e(x)(h) = h(x)$ for each $h \in F(X)$; it is a homeomorphism onto its image since $X$ is Tychonoff. The Stone–Čech compactification is $(e, \beta(X))$ where $\beta(X) = \overline{e[X]}$ in $Q^{F(X)}$.

Given $f: X \to Y$ continuous with $Y$ compact Hausdorff, define:

1. $f^*: F(Y) \to F(X)$ by $f^*(a) = a \circ f$ for each $a \in F(Y)$. This is well-defined since the composition of continuous functions is continuous.

2. $f^{**}: Q^{F(X)} \to Q^{F(Y)}$ by $f^{**}(q) = q \circ f^*$ for each $q \in Q^{F(X)}$. By Lemma 23, $f^{**}$ is continuous.

Let $g: Y \to Q^{F(Y)}$ be the evaluation map of $Y$. Since $Y$ is compact Hausdorff, $g$ is a homeomorphism of $Y$ onto $\beta(Y) = \overline{g[Y]}$.

The situation is summarized in the following commutative diagram:

\[
\begin{CD}
\beta(X) \;\subset\; Q^{F(X)} @>{f^{**}}>> Q^{F(Y)} \;\supset\; \beta(Y)\\
@A{e}AA @| \\
X @>{f}>> Y @>{g}>{\cong}> \beta(Y)
\end{CD}
\]

We verify commutativity on $X$: for $x \in X$ and $h \in F(Y)$,

\[
(f^{**} \circ e)(x)(h) = (e(x) \circ f^*)(h) = e(x)(f^*(h)) = e(x)(h \circ f) = (h \circ f)(x) = h(f(x)).
\]

On the other hand,

\[
(g \circ f)(x)(h) = g(f(x))(h) = h(f(x)).
\]

Thus $f^{**} \circ e = g \circ f$ on $X$. Since $f^{**}$ is continuous, $f^{**}(\beta(X)) = f^{**}(\overline{e[X]}) \subset \overline{f^{**}(e[X])} = \overline{g(f[X])} \subset \overline{g[Y]} = \beta(Y)$. So $f^{**}$ maps $\beta(X)$ into $\beta(Y)$.

Finally, define $\tilde{f} = g^{-1} \circ f^{**}|_{\beta(X)}: \beta(X) \to Y$. Then $\tilde{f}$ is continuous (composition of continuous maps), and for $x \in X$,

\[
\tilde{f}(e(x)) = g^{-1}(f^{**}(e(x))) = g^{-1}(g(f(x))) = f(x).
\]

Hence $\tilde{f} \circ e = f$, i.e., $\tilde{f}$ extends $f \circ e^{-1}$. $\square$
