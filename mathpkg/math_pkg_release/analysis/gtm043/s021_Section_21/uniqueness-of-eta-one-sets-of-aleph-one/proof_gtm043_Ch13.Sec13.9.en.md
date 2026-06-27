---
role: proof
locale: en
of_concept: uniqueness-of-eta-one-sets-of-aleph-one
source_book: gtm043
source_chapter: "13"
source_section: "13.9"
---
Well-order $S = \{s_\alpha\}_{\alpha < \omega_1}$ and $T = \{t_\alpha\}_{\alpha < \omega_1}$. Construct $\varphi : S \to T$ by transfinite induction.

At stage $\alpha$, we have $\varphi$ defined on a countable set $S_\alpha$ to $T_\alpha$, order-preservingly, with $\varphi(s_\xi) = t'_\xi$ and $\varphi(s'_\xi) = t_\xi$ for $\xi < \alpha$.

**Defining $t'_\alpha$:** If $s_\alpha \in S_\alpha$, set $t'_\alpha = \varphi(s_\alpha)$. Otherwise, decompose $S_\alpha = A_S \cup B_S$ where $A_S < s_\alpha < B_S$. Since $\varphi$ preserves order, $\varphi[A_S] < \varphi[B_S]$ in $T$. As $T$ is an $\eta_1$-set, there exists $t'_\alpha \in T$ with $\varphi[A_S] < t'_\alpha < \varphi[B_S]$. Set $\varphi(s_\alpha) = t'_\alpha$.

**Defining $s'_\alpha$:** Dually, if $t_\alpha \in T_\alpha$, set $s'_\alpha = \varphi^{-1}(t_\alpha)$. Otherwise, decompose $T_\alpha$ around $t_\alpha$ and use the $\eta_1$ property of $S$ to find $s'_\alpha$.

By induction, $\varphi$ is a bijective order-isomorphism of $S$ onto $T$.