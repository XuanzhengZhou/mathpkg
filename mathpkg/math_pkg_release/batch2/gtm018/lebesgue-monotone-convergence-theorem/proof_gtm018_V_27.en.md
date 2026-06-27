---
role: proof
locale: en
of_concept: lebesgue-monotone-convergence-theorem
source_book: gtm018
source_chapter: "V"
source_section: "27"
---
**Proof.** Since $\{f_n\}$ is increasing and the sequence of integrals is bounded, $\lim_n \int f_n d\mu$ exists and is finite. Hence $\{f_n\}$ is mean fundamental. By Theorem 26.B, $\{f_n\}$ mean converges to some integrable function $g$, and since mean convergence implies convergence in measure, a subsequence converges a.e. to $g$. But $f_n \uparrow f$ everywhere, so $f = g$ a.e., and $\int f d\mu = \lim_n \int f_n d\mu$.
