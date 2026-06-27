---
role: proof
locale: en
of_concept: basis-characterization-uniform-boundedness
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

If $X$ is a basis for $\mathcal{M}$, then for each $x \in \mathcal{M}$ we have $x = \lim_N E_N x$. By the uniform boundedness theorem (Theorem 12.15), the sequence $\{E_N\}$ of bounded operators must be uniformly bounded on $\mathcal{M}$.

Conversely, suppose $\|E_N y\| \leq M \|y\|$ for all $N$ and all $y \in \mathcal{M}$. Given $x \in \mathcal{M}$ and $\varepsilon > 0$, there exists a finite linear combination $x' = \lambda_0 x_0 + \cdots + \lambda_K x_K$ such that $\|x - x'\| < \varepsilon$. By Lemma 19.9, $E_N x' = x'$ for $N \geq K$. Then for $N \geq K$,
$$\|x - E_N x\| \leq \|x - x'\| + \|E_N(x' - x)\| \leq \varepsilon + M\|x' - x\| \leq (1+M)\varepsilon.$$

Thus $E_N x \to x$, showing $X$ is a basis for $\mathcal{M}$.
