---
role: proof
locale: en
of_concept: two-point-criterion-for-normality
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

For the first assertion, apply Proposition 9-13:
$$g_0 = ({}^0N f)_0 - \lim_n (P^n {}^0N f)_0.$$
Since ${}^0N_{0k} = 0$ for all $k$, we have $({}^0N f)_0 = 0$. Also ${}^0N_{k0} = 0$ for all $k$, so
$$\lim_n (P^n {}^0N f)_0 = -\lim_n (P^n {}^0N)_{0j} = -{}^0\nu_j.$$
Thus $g_0 = {}^0\nu_j$, and hence ${}^0\lambda_j = {}^0\nu_j / {}^0N_{jj}$ exists.

For the second assertion, the hypothesis about functions implies that ${}^0\lambda_j$ exists for all $j$. Dually, the hypothesis about signed measures (applied to the dual chain $\hat{P}$) implies that ${}^0\hat{\lambda}_j$ exists for all $j$. Both conditions together constitute the definition of normality (Definition 9-20).
