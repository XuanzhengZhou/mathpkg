---
role: proof
locale: en
of_concept: gumbel-inequalities
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of Gumbel's Inequalities

**Problem 5(b) (Section 6).** Prove **Gumbel's inequalities**: for $m = 1, 2, \ldots, n$,
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}},$$
where
$$\tilde{S}_m = \sum_{1 \leq i_1 < \cdots < i_m \leq n} \mathrm{P}(A_{i_1} \cup \cdots \cup A_{i_m}).$$

**Proof.** The proof uses a counting argument. For any outcome $\omega \in \Omega$, let
$$\nu(\omega) = \sum_{i=1}^{n} \mathbf{1}_{A_i}(\omega)$$
be the number of events among $A_1, \ldots, A_n$ that contain $\omega$.

**Step 1: Relating the two sums.** For a fixed $\omega$, consider how many $m$-tuples $(i_1, \ldots, i_m)$ satisfy $\omega \in A_{i_1} \cup \cdots \cup A_{i_m}$. The condition $\omega \in A_{i_1} \cup \cdots \cup A_{i_m}$ means that at least one of the $m$ chosen events contains $\omega$, i.e., $\nu(\omega) > 0$ among the chosen $m$ events. The number of $m$-tuples that FAIL this condition (i.e., none of the $m$ chosen events contains $\omega$) is
$$\begin{cases}
\binom{n - \nu(\omega)}{m}, & \text{if } m \leq n - \nu(\omega), \\
0, & \text{otherwise}.
\end{cases}$$

Therefore, the number of $m$-tuples with $\omega$ belonging to the union is
$$\binom{n}{m} - \binom{n - \nu(\omega)}{m} \quad \text{(with the convention } \binom{a}{b} = 0 \text{ for } b > a\text{).}$$

**Step 2: Sum over all outcomes.** Summing over $\omega$ with weight $\mathrm{P}(\{\omega\})$:
$$\tilde{S}_m = \sum_{\omega \in \Omega} \left[\binom{n}{m} - \binom{n - \nu(\omega)}{m}\right] \mathrm{P}(\{\omega\}).$$

For $\omega \in \bigcup_{i=1}^{n} A_i$, we have $\nu(\omega) \geq 1$. For such $\omega$, a combinatorial identity gives
$$\binom{n}{m} - \binom{n - \nu(\omega)}{m} \geq \binom{n-1}{m-1} \quad \text{for all } \nu(\omega) \geq 1.$$

(This is because the expression on the left is minimized when $\nu(\omega) = 1$, giving exactly $\binom{n}{m} - \binom{n-1}{m} = \binom{n-1}{m-1}$.)

**Step 3: The inequality.** Hence
$$\tilde{S}_m \geq \sum_{\omega \in \bigcup A_i} \binom{n-1}{m-1} \mathrm{P}(\{\omega\}) = \binom{n-1}{m-1} \cdot \mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right).$$

Dividing both sides by $\binom{n-1}{m-1}$ yields Gumbel's inequality:
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \frac{\tilde{S}_m}{\binom{n-1}{m-1}}.$$

**Remark.** For $m = 1$, $\tilde{S}_1 = \sum_{i=1}^{n} \mathrm{P}(A_i)$ and $\binom{n-1}{0} = 1$, so we recover the union bound:
$$\mathrm{P}\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} \mathrm{P}(A_i).$$

For larger $m$, the denominator $\binom{n-1}{m-1}$ grows, generally giving sharper bounds as more information about joint probabilities is incorporated.
