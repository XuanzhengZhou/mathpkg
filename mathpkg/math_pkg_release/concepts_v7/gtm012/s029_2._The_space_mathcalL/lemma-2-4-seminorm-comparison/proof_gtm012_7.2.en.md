---
role: proof
locale: en
of_concept: lemma-2-4-seminorm-comparison
source_book: gtm012
source_chapter: "7"
source_section: "§2. The space $\mathcal{L}$"
---

# Proof of Seminorm Comparison Inequality

**Lemma 2.4.** Suppose $k, k'$ are integers, and

$$0 \leq k \leq k', \quad a \leq a', \quad M \geq M'.$$

Suppose also either that $k = k'$ or that $a' > 0$. Then there is a constant $c$ such that

$$|u|_{k,a,M} \leq c |u|_{k',a',M'}, \quad \text{all } u \in \mathcal{L}.$$

**Proof.** It is sufficient to prove the inequality in all cases when two of the three indices are the same, and then chain the comparisons.

**Case 1:** $k = k'$, $a = a'$. Then $M \geq M'$ implies $[M, \infty) \subseteq [M', \infty)$, so the supremum over the smaller set is smaller:

$$|u|_{k,a,M} = \sup_{t \geq M} e^{at}|D^k u(t)| \leq \sup_{t \geq M'} e^{at}|D^k u(t)| = |u|_{k,a,M'}.$$

Thus $c = 1$ works.

**Case 2:** $k = k'$, $M = M'$. Since $a \leq a'$ and $t \geq M$, we have $e^{at} \leq e^{a't}$ for all $t \geq \max(M, 0)$. The condition $k = k'$ or $a' > 0$ ensures that either we are comparing the same derivative order (so the seminorms are directly comparable via the exponential factor) or $a' > 0$ (which guarantees the exponential factor $e^{at} \leq e^{a't}$ for $t$ sufficiently large). In either case, there exists a constant $c$ such that

$$|u|_{k,a,M} \leq c |u|_{k,a',M}.$$

Specifically, if $a' > 0$ then for $t \geq M$, $e^{at} \leq e^{a't}$ when $t \geq 0$; for $t \in [M, 0]$ (if $M < 0$) a constant factor $e^{(a'-a)M}$ accounts for the difference. If $k = k'$ and $a = a'$ the inequality is trivial.

**Case 3:** $a = a' > 0$, $M = M'$. Let $k' = k + j$ with $j \geq 0$, and set $v = D^{k'}u$. We may obtain $D^k u$ from $v$ by repeated integration from the right:

$$D^k u = (S_+)^j v,$$

where $S_+ w(t) = -\int_t^\infty w(s)\,ds$. Using the estimate

$$|S_+ w|_{0,a,M} \leq a^{-1} |w|_{0,a,M}$$

(from the bound (7) in the text) repeatedly $j$ times, we obtain

$$|u|_{k,a,M} = |D^k u|_{0,a,M} \leq a^{-j} |v|_{0,a,M} = a^{-j} |D^{k'} u|_{0,a,M} = a^{-j} |u|_{k',a,M}.$$

**Chaining the comparisons.** Starting from $|u|_{k,a,M}$:

1. By Case 1 (in reverse), increase $M$ to $M'$ (since $M \geq M'$): $|u|_{k,a,M} \leq |u|_{k,a,M'}$.
2. If $k < k'$, then $a' > 0$ by hypothesis. We may replace $a$ by $a'$ using Case 2, then apply Case 3 with $a'$: $|u|_{k,a',M'} \leq (a')^{-j} |u|_{k',a',M'}$. The intermediate comparison $|u|_{k,a,M'} \leq |u|_{k,a',M'}$ uses $a \leq a'$.
3. If $k = k'$, then $j = 0$ and we only need Case 1 and Case 2.

In all cases, there exists a constant $c$ (e.g., $c = \max(1, (a')^{-(k'-k)}, e^{(a'-a)|M'|})$) such that

$$|u|_{k,a,M} \leq c |u|_{k',a',M'}$$

for all $u \in \mathcal{L}$. $\square$

**Remark.** The seminorm comparison lemma shows that the family of seminorms $\{|\cdot|_{k,a,M}\}$ is directed: increasing $k$, increasing $a$, or decreasing $M$ makes the seminorm larger (up to a constant factor). This property is essential for establishing that $\mathcal{L}$ is a countably normed space, where one can extract a countable cofinal family of seminorms.
