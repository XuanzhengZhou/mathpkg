---
role: proof
locale: en
of_concept: supremum-of-submartingales
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

We have

$$M[\sup(f_n, g_n)] \leq M[\sup(|f_n|, |g_n|)] = \int_{|f_n| \geq |g_n|} |f_n| \, d\mu + \int_{|f_n| < |g_n|} |g_n| \, d\mu < \infty.$$

The function $\sup(f_n, g_n)$ is clearly constant on cells of $\mathcal{R}_n$ if $f_n$ and $g_n$ each are. Furthermore,

$$M[\sup(f_{n+1}, g_{n+1}) \mid \mathcal{R}_n] \geq M[f_{n+1} \mid \mathcal{R}_n] \geq f_n$$

and

$$M[\sup(f_{n+1}, g_{n+1}) \mid \mathcal{R}_n] \geq M[g_{n+1} \mid \mathcal{R}_n] \geq g_n$$

so that

$$M[\sup(f_{n+1}, g_{n+1}) \mid \mathcal{R}_n] \geq \sup(f_n, g_n).$$

Thus $(\sup(f_n, g_n), \mathcal{R}_n)$ satisfies both the integrability condition and the submartingale inequality.
