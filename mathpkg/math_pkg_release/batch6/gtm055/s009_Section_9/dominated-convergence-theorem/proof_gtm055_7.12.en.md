---
role: proof
locale: en
of_concept: dominated-convergence-theorem
source_book: gtm055
source_chapter: "7"
source_section: "9"
---

Since $|f_n| \leq g$ a.e. and $g$ is integrable, each $f_n$ is integrable. Moreover, $|f| \leq g$ a.e., so $f$ is also integrable. Consider the sequence $\{2g - |f_n - f|\}$, which is nonnegative a.e. Applying Fatou's Lemma:
$$\int_X \liminf_n (2g - |f_n - f|) d\mu \leq \liminf_n \int_X (2g - |f_n - f|) d\mu.$$
Since $|f_n - f| \to 0$ a.e., the left side equals $\int_X 2g d\mu$. The right side equals $2\int_X g d\mu - \limsup_n \int_X |f_n - f| d\mu$. Hence $\limsup_n \int_X |f_n - f| d\mu \leq 0$, which forces $\lim_n \int_X |f_n - f| d\mu = 0$. The convergence of integrals follows from $|\int f_n - \int f| \leq \int |f_n - f| \to 0$.
