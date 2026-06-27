---
role: proof
locale: en
of_concept: projection-operators-are-polynomials
source_book: gtm023
source_chapter: "13"
source_section: "13.5"
---
If $r = 1$, then $\pi_1 = \iota = 1(\varphi)$ and the assertion is trivial. Suppose $r > 1$. Define
$$g_i = f_1^{k_1} \cdots \widehat{f_i^{k_i}} \cdots f_r^{k_r}$$
where the hat denotes omission. According to sec. 12.9, the $g_i$ are relatively prime, hence there exist polynomials $h_i$ such that
$$\sum_i g_i h_i = 1. \tag{13.19}$$

From Corollary II, Proposition II, sec. 13.2, we have
$$K(g_i) = \sum_{j \neq i} E_j,$$
so in particular,
$$h_i(\varphi) g_i(\varphi) x = 0 \quad \text{for } x \in \sum_{j \neq i} E_j. \tag{13.20}$$

Now let $x \in E$ be arbitrary and write $x = \sum_i x_i$ with $x_i \in E_i$ (the decomposition (13.18)). Applying (13.19) and (13.20) yields
$$\sum_i x_i = x = \sum_i h_i(\varphi) g_i(\varphi) x = \sum_i h_i(\varphi) g_i(\varphi) \sum_j x_j = \sum_i h_i(\varphi) g_i(\varphi) x_i,$$
since $g_i(\varphi)x_j = 0$ for $j \neq i$ (as $x_j \in E_j \subset K(g_i)$). Hence
$$x_i = h_i(\varphi) g_i(\varphi) x_i \quad i = 1, \ldots, r. \tag{13.21}$$

From (13.20), for any $j \neq i$, $h_i(\varphi)g_i(\varphi)x_j = 0$. Together with (13.21), this shows that $h_i(\varphi)g_i(\varphi)$ acts as the identity on $E_i$ and vanishes on $E_j$ for $j \neq i$. Therefore
$$\pi_i = h_i(\varphi) g_i(\varphi) \quad i = 1, \ldots, r,$$
which completes the proof.
