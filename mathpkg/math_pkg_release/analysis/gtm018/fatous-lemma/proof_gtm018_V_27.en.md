---
role: proof
locale: en
of_concept: fatous-lemma
source_book: gtm018
source_chapter: "V"
source_section: "27"
---
**Proof.** Let $g_n(x) = \inf\{f_i(x) : n \leq i < \infty\}$. Then $g_n \leq f_n$, each $g_n$ is measurable and integrable (by Theorem A, since $0 \leq g_n \leq f_n$), and $\{g_n\}$ is increasing. Since $\int g_n d\mu \leq \int f_n d\mu$,
$$\lim_n \int g_n d\mu \leq \liminf_n \int f_n d\mu < \infty.$$
Since $\lim_n g_n(x) = \liminf_n f_n(x) = f(x)$, it follows from the monotone convergence theorem (Theorem B) that $f$ is integrable and
$$\int f d\mu = \lim_n \int g_n d\mu \leq \liminf_n \int f_n d\mu.$$
