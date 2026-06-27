---
role: proof
locale: en
of_concept: omega-zero-properties
source_book: gtm027
source_chapter: "Problems"
source_section: "E"
---

# Proof of Properties of the Space of Countable Ordinals

Let $\Omega$ be the first uncountable ordinal and let $\Omega_0 = \{\alpha : \alpha < \Omega\}$ be the set of all countable ordinals, endowed with the order topology.

**Statement.** The space $\Omega_0$ is locally compact, Hausdorff, satisfies the first axiom of countability, and is sequentially compact, but is not compact.

**Proof.**

1. *Hausdorff.* Every order topology is Hausdorff: given $\alpha < \beta$ in $\Omega_0$, there exists an ordinal $\gamma$ with $\alpha < \gamma < \beta$ (since $\Omega_0$ is dense in itself), and the open intervals $[0, \gamma)$ and $(\gamma, \Omega)$ separate $\alpha$ and $\beta$.

2. *Locally compact.* For any $\alpha \in \Omega_0$, the closed interval $[0, \alpha] = \{\beta : \beta \leq \alpha\}$ is a neighborhood of $\alpha$ (it contains the open interval $[0, \alpha+1)$). This interval is compact: any open cover of $[0, \alpha]$ has a finite subcover by transfinite induction on the countable ordinal $\alpha$.

3. *First axiom of countability.* For each $\alpha \in \Omega_0$, the countable collection $\{(\beta, \alpha] : \beta < \alpha\}$ forms a local basis at $\alpha$ (where $(\beta, \alpha] = \{\gamma : \beta < \gamma \leq \alpha\}$). Since $\alpha$ is countable, this collection is countable.

4. *Sequentially compact.* Let $(x_n)_{n \in \mathbb{N}}$ be a sequence in $\Omega_0$. Each $x_n$ is a countable ordinal. Let $\beta = \sup_n x_n$. Since the supremum of countably many countable ordinals is countable, $\beta < \Omega$. The interval $[0, \beta]$ is compact (as proved above), hence the sequence has a convergent subsequence in $[0, \beta]$, and therefore in $\Omega_0$.

5. *Not compact.* The open cover $\{[0, \alpha) : \alpha < \Omega\}$ of $\Omega_0$ has no finite subcover. If it did, there would be a finite set $\{\alpha_1, \ldots, \alpha_n\} \subset \Omega_0$ with $\Omega_0 = \bigcup_{i=1}^n [0, \alpha_i) = [0, \max_i \alpha_i)$, but $\max_i \alpha_i$ is a countable ordinal, so it does not cover the ordinal $\max_i \alpha_i + 1 \in \Omega_0$, contradiction.
