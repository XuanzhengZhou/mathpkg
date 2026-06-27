---
role: proof
locale: en
of_concept: hahn-banach-theorem
source_book: gtm024
source_chapter: "I"
source_section: "§6. Alternate Formulations of the Separation Principle"
---

Let $M$ be a subspace of $X$, let $p$ be a sublinear functional on $X$, and let $f$ be a linear functional on $M$ such that $f(x) \leqslant p(x)$ for all $x \in M$. Consider the set $\mathcal{E}$ of all pairs $(N, g)$ where $N$ is a subspace containing $M$ and $g$ is a linear functional on $N$ extending $f$ with $g(x) \leqslant p(x)$ for $x \in N$. Partially order $\mathcal{E}$ by $(N_1, g_1) \leqslant (N_2, g_2)$ if $N_1 \subset N_2$ and $g_2$ extends $g_1$. By Zorn's lemma, $\mathcal{E}$ has a maximal element $(N_0, g_0)$. If $N_0 \neq X$, choose $y \in X \setminus N_0$ and extend $g_0$ to $N_0 + \operatorname{span}\{y\}$ by setting $g_0(x + \alpha y) = g_0(x) + \alpha c$ where $c$ satisfies $\sup_{x \in N_0}\{g_0(x) - p(x - y)\} \leqslant c \leqslant \inf_{x \in N_0}\{p(x + y) - g_0(x)\}$. Such $c$ exists because $g_0(x_1) + g_0(x_2) \leqslant p(x_1 + y) + p(x_2 - y)$. This contradicts maximality, so $N_0 = X$ and $g_0$ is the desired extension.
