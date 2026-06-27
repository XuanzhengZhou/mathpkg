---
role: proof
locale: en
of_concept: tits-system-parabolic-subgroups
source_book: gtm021
source_chapter: "29"
source_section: "29.2"
---
(a) $P_I$ is closed under taking inverses and under left multiplication by $B$, so it suffices to check closure under left multiplication by $\rho \in I$. But (T1) implies that $\rho B W_I B \subset B W_I B \cup B \rho W_I B \subset P_I$.

(b) The 'only if' part needs proof. Proceed by induction on $\ell(\sigma)$, which we may assume $\leqslant \ell(\sigma')$. If $\ell(\sigma) = 0$, $\sigma = e$ and the assumption reads: $B = B\sigma' B$. So a representative of $\sigma'$ in $N$ lies in $B$. But $B \cap N = T$, so $\sigma' = e$. For the induction step, suppose $B\sigma B = B\sigma' B$ with $\ell(\sigma) \geqslant 1$. Write $\sigma = \rho\sigma_1$ with $\rho \in S$ and $\ell(\sigma_1) = \ell(\sigma) - 1$. Using (T1) and the induction hypothesis, one shows that $\sigma' = \rho\sigma_1 = \sigma$.
