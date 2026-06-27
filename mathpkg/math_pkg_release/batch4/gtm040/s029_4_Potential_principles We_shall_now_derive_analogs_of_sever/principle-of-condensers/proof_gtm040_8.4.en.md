---
role: proof
locale: en
of_concept: principle-of-condensers
source_book: gtm040
source_chapter: "8"
source_section: "4"
---

Let $g_i = {}^F H_{iE}$, the probability starting at $i$ that $E$ is reached before $F$. Clearly, $g$ is $1$ on $E$ and $0$ on $F$. Furthermore, $0 \leq g \leq h^E$. Since $P^n h^E \to 0$ for the equilibrium set $E$, we have $P^n g \to 0$.

Let $f = (I - P)g$. To apply Corollary 8-8 and conclude that $g$ is a potential with charge $f$, we must show that $\alpha f$ is finite. If $i$ is in the complement of $E \cup F$, then $(Pg)_i = g_i$ since $g$ is regular off $E \cup F$, so $f_i = 0$ there. The non-zero contributions to $f$ come only from $E$, $F$, and the finite boundary $\bar{E}$. By the finite boundary condition and the boundedness of $g$, the total charge $\alpha f$ is finite. The signs of $f$ on $E$ and $F$ give $f^+$ supported in $E$ and $f^-$ supported in $F$, with $\alpha f \geq 0$.
