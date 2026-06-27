---
role: proof
locale: en
of_concept: yoneda-lemma
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Define the map $y: \operatorname{Nat}(D(r, -), K) \to Kr$ by $y(\alpha) = \alpha_r(1_r)$. To show it is a bijection, we construct its inverse.

Given any element $x \in Kr$, define a natural transformation $\alpha^x: D(r, -) \to K$ as follows: for each object $d \in D$ and each arrow $f: r \to d$ in $D(r, d)$, set

\[
\alpha^x_d(f) = K(f)(x) \in Kd.
\]

We verify naturality: for any $g: d \to d'$ in $D$, the diagram

\[
\begin{CD}
D(r, d) @>{\alpha^x_d}>> Kd \\
@V{D(r, g)}VV @VV{K(g)}V \\
D(r, d') @>{\alpha^x_{d'}}>> Kd'
\end{CD}
\]

commutes because for any $f: r \to d$, following the top-right path gives $K(g)(K(f)(x))$, while the left-bottom path gives $K(g \circ f)(x)$, and these are equal by functoriality of $K$.

Now check that $y$ and $x \mapsto \alpha^x$ are inverses:
- $y(\alpha^x) = \alpha^x_r(1_r) = K(1_r)(x) = 1_{Kr}(x) = x$.
- Given $\alpha \in \operatorname{Nat}(D(r, -), K)$, we need $\alpha^{y(\alpha)} = \alpha$. For any $f: r \to d$, naturality of $\alpha$ gives $\alpha_d \circ D(r, f) = K(f) \circ \alpha_r$. Applying this to $1_r \in D(r, r)$:

\[
\alpha_d(f) = \alpha_d(D(r, f)(1_r)) = K(f)(\alpha_r(1_r)) = K(f)(y(\alpha)) = \alpha^{y(\alpha)}_d(f).
\]

Thus $\alpha = \alpha^{y(\alpha)}$, completing the proof.
