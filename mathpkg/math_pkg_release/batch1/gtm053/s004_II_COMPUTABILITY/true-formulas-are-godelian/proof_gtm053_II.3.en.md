---
role: proof
locale: en
of_concept: true-formulas-are-godelian
source_book: gtm053
source_chapter: "II"
source_section: "3"
---

We must verify the four defining properties of a Gödelian set:

1. **Completeness:** For any closed formula $P$, either $P \in T_\phi L$ or $\neg P \in T_\phi L$. This follows from the definition of truth: $|P|_\phi$ is either $1$ or $0$, and $|\neg P| = 1 - |P|$.

2. **No contradiction:** There is no formula $P$ such that both $P \in T_\phi L$ and $\neg P \in T_\phi L$. This is because $|P|_\phi = 1$ implies $|\neg P|_\phi = 0$.

3. **Closure under MP:** If $P \in T_\phi L$ and $P \Rightarrow Q \in T_\phi L$, then $Q \in T_\phi L$. Since $|P|_\phi = 1$ and $|P \Rightarrow Q|_\phi = 1 - |P| + |P||Q| = |Q| = 1$, we have $|Q|_\phi = 1$.

4. **Closure under Gen:** If $P \in T_\phi L$, then $\forall x P \in T_\phi L$. If $|P|_\phi(\xi) = 1$ for all $\xi \in \overline{M}$, then for any $\xi$, $|\forall x P|_\phi(\xi) = \min_{\xi'} |P|_\phi(\xi') = 1$, where $\xi'$ runs over variations of $\xi$ along $x$.

5. **Contains all logical axioms:** The tautologies are true regardless of the truth values of components, and the quantifier axioms are verified to be $\phi$-true in section 3.7.
