---
role: exercise
locale: en
chapter: "IX"
section: "§26. Sequences of Integrable Functions"
exercise_number: 7
---

If $\{f_n\}$ is a sequence of non-negative integrable functions which converges a.e. to an integrable function $f$, and if $\int f_n \, d\mu = \int f \, d\mu$, $n = 1, 2, \dots$, then $\{f_n\}$ converges to $f$ in the mean.

(Hint: write $g_n = f_n - f$ and observe that the trivial inequality $|f_n - f| \leq f_n + f$ implies that $0 \leq g_n^- \leq f$. The bounded convergence theorem may therefore be applied to the sequence $\{g_n^-\}$; the desired result follows from the fact that $\int g_n^+ \, d\mu - \int g_n^- \, d\mu = 0$, $n = 1, 2, \dots$)
