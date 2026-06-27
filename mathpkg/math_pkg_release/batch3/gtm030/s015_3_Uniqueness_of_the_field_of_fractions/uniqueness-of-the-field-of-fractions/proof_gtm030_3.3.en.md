---
role: proof
locale: en
of_concept: uniqueness-of-the-field-of-fractions
source_book: gtm030
source_chapter: "III"
source_section: "3"
---

Define a mapping $\tau$ of $\mathfrak{F}_1$ into $\mathfrak{F}_2$ by

$$\tau(a_1 b_1^{-1}) = a_1^\sigma (b_1^\sigma)^{-1}, \quad a_1, b_1 \in \mathfrak{A}_1, \; b_1 \neq 0.$$

We verify that $\tau$ is the desired isomorphism.

**Well-defined.** Suppose $a_1 b_1^{-1} = c_1 d_1^{-1}$. Then $a_1 d_1 = c_1 b_1$ in $\mathfrak{A}_1$. Applying the isomorphism $\sigma$ yields $a_1^\sigma d_1^\sigma = c_1^\sigma b_1^\sigma$ in $\mathfrak{A}_2$. Hence $a_1^\sigma (b_1^\sigma)^{-1} = c_1^\sigma (d_1^\sigma)^{-1}$, so $\tau$ is single-valued.

**Injective.** If $a_1^\sigma (b_1^\sigma)^{-1} = c_1^\sigma (d_1^\sigma)^{-1}$, then $a_1^\sigma d_1^\sigma = c_1^\sigma b_1^\sigma$. Since $\sigma$ is an isomorphism, $(a_1 d_1)^\sigma = (c_1 b_1)^\sigma$ implies $a_1 d_1 = c_1 b_1$, whence $a_1 b_1^{-1} = c_1 d_1^{-1}$. Thus the mapping is 1-1.

**Surjective.** If $a_2 b_2^{-1}$ is any element of $\mathfrak{F}_2$, we can find $a_1, b_1 \in \mathfrak{A}_1$ such that $a_1^\sigma = a_2$ and $b_1^\sigma = b_2$, since $\sigma$ is onto. Then $a_2 b_2^{-1} = a_1^\sigma (b_1^\sigma)^{-1} = \tau(a_1 b_1^{-1})$ is an image. Hence $\tau$ is a mapping of $\mathfrak{F}_1$ onto $\mathfrak{F}_2$.

**Preserves addition.** For $a_1 b_1^{-1}, c_1 d_1^{-1} \in \mathfrak{F}_1$,

$$
\begin{aligned}
a_1 b_1^{-1} + c_1 d_1^{-1}
&= (a_1 d_1 + c_1 b_1)(b_1 d_1)^{-1} \\
&\mapsto (a_1 d_1 + c_1 b_1)^\sigma ((b_1 d_1)^\sigma)^{-1} \\
&= (a_1^\sigma d_1^\sigma + c_1^\sigma b_1^\sigma)(b_1^\sigma d_1^\sigma)^{-1} \\
&= a_1^\sigma (b_1^\sigma)^{-1} + c_1^\sigma (d_1^\sigma)^{-1}.
\end{aligned}
$$

**Preserves multiplication.** For $a_1 b_1^{-1}, c_1 d_1^{-1} \in \mathfrak{F}_1$,

$$
\begin{aligned}
(a_1 b_1^{-1})(c_1 d_1^{-1})
&= a_1 c_1 (b_1 d_1)^{-1} \\
&\mapsto (a_1 c_1)^\sigma ((b_1 d_1)^\sigma)^{-1} \\
&= a_1^\sigma c_1^\sigma (b_1^\sigma d_1^\sigma)^{-1} \\
&= (a_1^\sigma (b_1^\sigma)^{-1})(c_1^\sigma (d_1^\sigma)^{-1}).
\end{aligned}
$$

Thus $\tau$ is an isomorphism of $\mathfrak{F}_1$ onto $\mathfrak{F}_2$.

**Uniqueness.** If $\tau'$ is any isomorphism of $\mathfrak{F}_1$ onto $\mathfrak{F}_2$ that extends $\sigma$, then for any $a_1 b_1^{-1} \in \mathfrak{F}_1$ we must have

$$\tau'(a_1 b_1^{-1}) = \tau'(a_1) \tau'(b_1)^{-1} = a_1^\sigma (b_1^\sigma)^{-1} = \tau(a_1 b_1^{-1}),$$

since every element of $\mathfrak{F}_1$ can be expressed as $a_1 b_1^{-1}$ with $a_1, b_1 \in \mathfrak{A}_1$, $b_1 \neq 0$. Hence $\tau' = \tau$ and the extension is unique.
