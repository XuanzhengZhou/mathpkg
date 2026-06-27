---
role: proof
locale: en
of_concept: seminorm-ball-scaling
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Scaling property of seminorm balls

Let $E$ be a vector space over $\mathbb{K}$, let $p$ be a seminorm on $E$, and for each $\varepsilon > 0$, define

$$B_{\varepsilon} = \{x : p(x) \leq \varepsilon\}.$$

Then $B_{\varepsilon} = \varepsilon B_1$.

*Proof.* The following conditions imply one another:

$$\begin{aligned}
x \in B_{\varepsilon} &\iff p(x) \leq \varepsilon \\
&\iff p(\varepsilon^{-1}x) \leq 1 \\
&\iff \varepsilon^{-1}x \in B_1 \\
&\iff x \in \varepsilon B_1.
\end{aligned}$$

Thus $B_{\varepsilon} = \varepsilon B_1$ as claimed.
