---
role: proof
locale: en
of_concept: greens-function-existence-bounded-dirichlet
source_book: gtm011
source_chapter: "X"
source_section: "5"
---

*Proof.* Define $f: \partial G \to \mathbb{R}$ by $f(z) = \log |z - a|$, and let $u: G^- \to \mathbb{R}$ be the unique continuous function which is harmonic on $G$ and such that $u(z) = f(z)$ for $z$ in $\partial G$. Then $g_a(z) = u(z) - \log |z - a|$ is easily seen to be the Green's Function:
\begin{itemize}
\item[(a)] $g_a$ is harmonic in $G - \{a\}$ since both $u$ and $\log|z-a|$ are harmonic there;
\item[(b)] $g_a(z) + \log|z-a| = u(z)$ is harmonic in a disk about $a$ (in fact on all of $G$);
\item[(c)] for each $w \in \partial G$, $\lim_{z \to w} g_a(z) = u(w) - \log|w-a| = f(w) - f(w) = 0$.
\end{itemize}
Since $G$ is bounded, $\partial_\infty G = \partial G$ and these properties verify that $g_a$ is the Green's Function. $\square$
