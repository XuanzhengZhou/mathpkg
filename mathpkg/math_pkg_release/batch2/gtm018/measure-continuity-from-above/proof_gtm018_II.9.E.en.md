---
role: proof
locale: en
of_concept: measure-continuity-from-above
source_book: gtm018
source_chapter: "II"
source_section: "9"
---

If $\mu(E_m) < \infty$, then $\mu(E_n) \leq \mu(E_m) < \infty$ for $n \geq m$, and therefore $\mu(\lim_n E_n) < \infty$. It follows from Theorems A and D that

$$\mu(E_m) - \mu(\lim_n E_n) = \mu(E_m - \lim_n E_n) = \mu(\lim_n (E_m - E_n)) =$$

$$= \lim_n \mu(E_m - E_n) = \lim_n (\mu(E_m) - \mu(E_n)) = \mu(E_m) - \lim_n \mu(E_n).$$

Since $\mu(E_m) < \infty$, the desired result follows by subtraction.
