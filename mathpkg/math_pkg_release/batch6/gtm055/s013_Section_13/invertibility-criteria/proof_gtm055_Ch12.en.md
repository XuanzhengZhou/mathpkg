---
role: proof
locale: en
of_concept: invertibility-criteria
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

If $RT = 1_{\mathcal{E}}$ then for each vector $x$ in $\mathcal{E}$ we have $x = RTx$, and therefore

$$\|x\| \leq \|R\| \|Tx\|.$$

Thus $T$ is bounded below. (If $\|R\| = 0$ then $\mathcal{E} = (0)$, and $T$ is trivially bounded below.) If $TS = 1_{\mathcal{F}}$ then for each vector $y$ in $\mathcal{F}$ we have $y = T(Sy)$, so $T$ maps $\mathcal{E}$ onto $\mathcal{F}$. To complete the proof it suffices to show that $T$ is invertible if $\mathcal{R}(T) = \mathcal{F}$ and $T$ is bounded below by some positive number $M$. If these hypotheses are satisfied, then, in the first place, $\mathcal{K}(T) = (0)$ so that $T$ is one-to-one. Consequently $T$ possesses a set-theoretic inverse $S$ defined on $\mathcal{R}(T) = \mathcal{F}$ by $S(Tx) = x$, and $S$ is a linear transformation of $\mathcal{F}$ onto $\mathcal{E}$. Finally, since $\|S(Tx)\| = \|x\| \leq (1/M) \|Tx\|$, we see that $S$ is bounded and that $\|S\| \leq 1/M$, so that $S = T^{-1}$ is an element of $\mathcal{L}(\mathcal{F}, \mathcal{E})$.
