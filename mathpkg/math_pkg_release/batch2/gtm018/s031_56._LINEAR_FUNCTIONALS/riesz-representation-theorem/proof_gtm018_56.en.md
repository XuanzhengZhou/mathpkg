---
role: proof
locale: en
of_concept: riesz-representation-theorem
source_book: gtm018
source_chapter: "56"
source_section: "56. LINEAR FUNCTIONALS"
---

Write $\lambda(C) = \inf \{ \Lambda(f) : C \subset f \in \mathcal{L}_+ \}$ for every compact set $C$ in $\mathbf{C}$, and let $\mu$ be the Borel measure induced by the content $\lambda$ (via the extension theorems of earlier sections). By Theorem B, we already have $\int f \, d\mu \leq \Lambda(f)$ for every $f \in \mathcal{L}_+$.

To prove the reverse inequality, let $f$ be any function in $\mathcal{L}$. Choose a compact set $C$ such that $f$ vanishes outside $C$, and let $\epsilon > 0$. By Theorem C, there exists $f_0 \in \mathcal{L}_+$ with $C \subset f_0$, $f_0 \leq 1$, and $\Lambda(f_0) \leq \int f_0 \, d\mu + \epsilon$.

We observe that since $C \subset f_0$, it follows that $f f_0 = f$ (because $f_0 = 1$ on the support of $f$). If $c$ is a positive number such that $|f(x)| \leq c$ for all $x$ in $X$, then the function $(f + c)f_0$ belongs to $\mathcal{L}_+$ and hence, by Theorem B,

\begin{align*}
\Lambda(f) + c\Lambda(f_0) &= \Lambda((f + c)f_0) \\
&\geq \int (f + c)f_0 \, d\mu \\
&= \int f \, d\mu + c \int f_0 \, d\mu.
\end{align*}

It follows that

\begin{align*}
\Lambda(f) &\geq \int f \, d\mu + c \left[ \int f_0 \, d\mu - \Lambda(f_0) \right] \\
&\geq \int f \, d\mu - c\epsilon.
\end{align*}

The arbitrariness of $\epsilon$ implies that $\Lambda(f) \geq \int f \, d\mu$, i.e., that Theorem B is true for all $f$ in $\mathcal{L}$. Combining with the inequality from Theorem B yields $\Lambda(f) = \int f \, d\mu$ for all $f \in \mathcal{L}_+$. Applying this equality to the positive and negative parts of an arbitrary $f \in \mathcal{L}$ yields the result for all $f \in \mathcal{L}$.
