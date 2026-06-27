---
role: proof
locale: en
of_concept: completeness-continuity-closed-equivalence
source_book: gtm055
source_chapter: "13"
source_section: "15"
---
That (ii) and (iii) imply one another in the presence of (i) is essentially the content of the closed graph theorem. Thus it suffices to show that if $\mathcal{E}$ is the domain of a linear transformation $T$ that is both closed and continuous, then $\mathcal{E}$ must be complete. Let $\{x_n\}$ be Cauchy in $\mathcal{E}$. Given $\varepsilon > 0$, choose $\delta > 0$ such that $|x| < \delta$ implies $|Tx| < \varepsilon$, and choose $N$ so that $|x_n - x_m| < \delta$ for $m, n \geq N$. Then $|Tx_n - Tx_m| < \varepsilon$ for $m, n \geq N$, so $\{Tx_n\}$ is Cauchy in $\mathcal{F}$. Hence $\{(x_n, Tx_n)\}$ is Cauchy in $\mathcal{E} \oplus_1 \mathcal{F}$ and, belonging to the closed graph of $T$, must converge there, so $\{x_n\}$ converges in $\mathcal{E}$.
