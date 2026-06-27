---
role: proof
locale: en
of_concept: recursive-enumerability-of-descriptive-validity
source_book: gtm037
source_chapter: "29"
source_section: "5. Unusual Logics"
---

The proof follows from Theorem 29.20, which establishes that every descriptive formula $\varphi$ is equivalent (relative to $\Gamma$) to a $\tau$-free formula $\varphi^*$. Since the set of valid $\tau$-free sentences is recursively enumerable (by the completeness theorem for ordinary first-order logic), the set

$$\{ \varphi : \varphi \text{ is a sentence of } (\mathcal{L}, \tau, \mathbf{O}) \text{ and } \models \varphi \}$$

is also recursively enumerable. Specifically, one can enumerate all $\tau$-free formulas $\varphi^*$ that are valid in ordinary first-order logic, and for each such $\varphi^*$, the corresponding $\varphi$ (obtained by reversing the eliminability translation) is valid in the descriptive logic.

This result also gives rise to the possibility of developing a proof theory based on the $\tau$-operator, with logical axioms for $\tau$, leading to a notion $\Gamma \vdash_{\mathbf{D}} \varphi$ for which the completeness theorem can be proved.
