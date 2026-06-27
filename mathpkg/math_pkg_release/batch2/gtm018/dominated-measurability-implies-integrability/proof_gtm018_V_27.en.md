---
role: proof
locale: en
of_concept: dominated-measurability-implies-integrability
source_book: gtm018
source_chapter: "V"
source_section: "27"
---
**Proof.** Consider non negative $f$. Take an increasing sequence $\{f_n\}$ of non negative simple functions converging to $f$. Since $0 \leq f_n \leq |g|$, each $f_n$ is integrable and $\int f_n d\mu \leq \int |g| d\mu$. Thus $\{\int f_n\}$ is bounded and increasing, so $\lim_n \int f_n d\mu$ is finite. Moreover,
$$\lim_{m,n} \left| \int f_m d\mu - \int f_n d\mu \right| = 0,$$
and since $f_m - f_n$ has constant sign for fixed $m,n$,
$$\left| \int f_m d\mu - \int f_n d\mu \right| = \int \left| f_m - f_n \right| d\mu,$$
so $\{f_n\}$ is mean fundamental, hence $f$ is integrable. The general case follows by considering $f^+$ and $f^-$.
