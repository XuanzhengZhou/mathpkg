---
role: exercise
locale: en
chapter: "1"
section: "6"
exercise_number: "5"
---

# Exercise 5 — Inclusion-Exclusion Principle, Bonferroni, Gumbel, and Frechet Inequalities

Let $A_1, \ldots, A_n$ be events and let

$$S_r = \sum_{1 \leq i_1 < \cdots < i_r \leq n} \mathrm{P}(A_{i_1} \cap \cdots \cap A_{i_r}), \quad r = 1, \ldots, n.$$

Also let

$$B_m = \{\omega : \omega \text{ belongs to exactly } m \text{ of the events } A_1, \ldots, A_n\}.$$

Show that

$$\mathrm{P}(B_m) = \sum_{r=m}^{n} (-1)^{r-m} \binom{r}{m} S_r, \quad m = 1, \ldots, n.$$

In particular, the probability that at least one of the events $A_1, \ldots, A_n$ occurs is

$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) = \mathrm{P}(B_1) + \cdots + \mathrm{P}(B_n) = S_1 - S_2 + \cdots + (-1)^{n-1} S_n.$$

Show also that the probability that at least $m$ of the events $A_1, \ldots, A_n$ occur simultaneously is

$$\mathrm{P}(B_m) + \cdots + \mathrm{P}(B_n) = \sum_{r=m}^{n} (-1)^{r-m} \binom{r-1}{m-1} S_r.$$

Prove the following properties:

**(a) Bonferroni's inequalities:** for any $k = 1, 2, \ldots$ such that $2k \leq n$,

$$S_1 - S_2 + \cdots - S_{2k} \leq \mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq S_1 - S_2 + \cdots + S_{2k-1}.$$

**(b) Gumbel's inequalities:** for $m = 1, \ldots, n$,

$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}},$$

where $\tilde{S}_m = \sum_{1 \leq i_1 < \cdots < i_m \leq n} \mathrm{P}(A_{i_1} \cup \cdots \cup A_{i_m}).$

**(c) Frechet's inequalities:** for $m = 1, \ldots, n-1$,

$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_{m+1}}{\binom{n-1}{m}} \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}}.$$
