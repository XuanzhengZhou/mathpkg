---
role: proof
locale: en
of_concept: unit-group-idele-lemma
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

Let $U_p$ be the group of unit ideles (components at primes not dividing $p$ are units). Let $U^{(n)}$ be the subgroup of ideles whose $p$-adic components are $\equiv 1 \bmod \mathfrak{p}^n$ for each prime $\mathfrak{p} \mid p$. The collection $\{U^{(n)}\}_{n \geq 1}$ forms a fundamental system of neighborhoods of $1$ in the idele group.

Consider the closure $\overline{K^\times}$ of the diagonal embedding of $K^\times$ in the idele group $\mathbf{J}_K$. An idele $\alpha \in \mathbf{J}_K$ lies in $\overline{K^\times}$ if and only if for every $n \geq 1$, there exists $x \in K^\times$ such that $\alpha x^{-1} \in U^{(n)}$.

Now $\alpha \in U_p \cap \overline{K^\times}$ means that $\alpha$ has unit components at all $\mathfrak{p} \nmid p$ and $\alpha \in \overline{K^\times}$. Taking the approximation $x \in K^\times$ as above, the condition $\alpha x^{-1} \in U^{(n)}$ together with $\alpha \in U_p$ implies that $x$ is a unit at all $\mathfrak{p} \nmid p$, and $x \equiv 1 \bmod \mathfrak{p}^n$ for all $\mathfrak{p} \mid p$ (after adjusting by a $p$-unit).

Thus $U_p \cap U^{(n)} K^\times = U^{(n)} E$, where $E = \mathcal{O}_K^\times$ is the group of global units. Intersecting over all $n$ and using that $\bigcap_n U^{(n)} = \{1\}$, we obtain

$$
U_p \cap \overline{K^\times} = \bigcap_n (U_p \cap U^{(n)} K^\times) = \bigcap_n U^{(n)} E = \overline{E}
$$

where the last closure is taken in the idele topology. This completes the proof.
