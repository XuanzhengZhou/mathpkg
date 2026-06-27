---
role: proof
locale: en
of_concept: epsilon-invariant-theorem
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.1"
---

Let $e = (e_1,\ldots,e_n)$ and $e' = (e_1',\ldots,e_n')$ be two orthogonal bases of $V$, with $a_i = e_i \cdot e_i$ and $a_i' = e_i' \cdot e_i'$.

We prove the independence by induction on $n$. The case $n=1$ is trivial. For $n \geq 2$, it suffices to show that $\varepsilon(e)$ is unchanged when we replace $e$ by a basis $e'$ that differs from $e$ in at most one vector. Without loss of generality, suppose $e_1' \neq e_1$ and $e_i' = e_i$ for $i \geq 2$.

Since $\langle e_2,\ldots,e_n \rangle$ and its orthogonal complement both contain $e_1$, there exist scalars $\lambda_2,\ldots,\lambda_n$ such that $e_1' = e_1 + \sum_{i=2}^n \lambda_i e_i$ (after scaling). By orthogonality, $e_1' \cdot e_1' = e_1 \cdot e_1$, so $a_1' = a_1$ in $k^*/k^{*2}$.

Now compute:

$$\varepsilon(e') = (a_1, d(Q)a_1) \prod_{2 \leq i < j} (a_i', a_j').$$

But the inductive hypothesis applied to the orthogonal complement of $e_1$ shows that

$$\prod_{2 \leq i < j} (a_i, a_j) = \prod_{2 \leq i < j} (a_i', a_j').$$

Thus $\varepsilon(e') = \varepsilon(e)$, and the result follows by induction.
