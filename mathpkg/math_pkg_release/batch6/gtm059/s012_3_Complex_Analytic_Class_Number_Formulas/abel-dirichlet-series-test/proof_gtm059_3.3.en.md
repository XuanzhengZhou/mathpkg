---
role: proof
locale: en
of_concept: abel-dirichlet-series-test
source_book: gtm059
source_chapter: "3"
source_section: "3. Complex Analytic Class Number Formulas"
---

Let $B_n = \sum_{k=1}^{n} b_k$. By hypothesis, $|B_n| \leq C$ for some constant $C > 0$ and all $n$. Using summation by parts (Abel summation):

$$\sum_{k=m+1}^{n} a_k b_k = \sum_{k=m+1}^{n} a_k (B_k - B_{k-1}) = a_n B_n - a_{m+1} B_m - \sum_{k=m+1}^{n-1} (a_{k+1} - a_k) B_k.$$

Since $a_n$ decreases to $0$ and $|B_k| \leq C$, we have

$$\left|\sum_{k=m+1}^{n} a_k b_k\right| \leq C a_n + C a_{m+1} + C \sum_{k=m+1}^{n-1} |a_{k+1} - a_k|.$$

Because $a_k$ is decreasing, $a_{k+1} - a_k \leq 0$, so $|a_{k+1} - a_k| = a_k - a_{k+1}$. The sum telescopes:

$$\sum_{k=m+1}^{n-1} |a_{k+1} - a_k| = a_{m+1} - a_n.$$

Therefore

$$\left|\sum_{k=m+1}^{n} a_k b_k\right| \leq C a_n + C a_{m+1} + C (a_{m+1} - a_n) = 2C a_{m+1}.$$

Since $a_{m+1} \to 0$ as $m \to \infty$, the partial sums form a Cauchy sequence, and the series $\sum a_n b_n$ converges.
