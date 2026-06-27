---
role: proof
locale: en
of_concept: convolution-distribution-convergence
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Continuity of Convolution under Distribution Convergence

**Corollary 7.6.** Suppose $(f_n)_{1}^{\infty} \subset \mathcal{P}$, $(g_n)_{1}^{\infty} \subset \mathcal{P}$, and set

$$F_n = F_{f_n}, \quad G_n = F_{g_n}.$$

Suppose

$$F_n \to F \quad (\mathcal{P}') \quad \text{and} \quad G_n \to G \quad (\mathcal{P}').$$

Then

$$F_n * G \to F * G \quad (\mathcal{P}')$$

and

$$F * G_n \to F * G \quad (\mathcal{P}').$$

*Proof.* Suppose $u \in \mathcal{P}$. Then, using the definition of convolution of distributions,

$$(F_n * G)(u) = F_n(G^\sim * u) \to F(G^\sim * u) = (F * G)(u),$$

since $F_n \to F$ in $\mathcal{P}'$ and $G^\sim * u \in \mathcal{P}$ is a fixed test function.

For the second assertion, note that by Lemma 7.5, $G_n^\sim * u \to G^\sim * u$ in the sense of $\mathcal{P}$. Therefore

$$(F * G_n)(u) = F(G_n^\sim * u) \to F(G^\sim * u) = (F * G)(u),$$

using the continuity of $F$ as a linear functional on $\mathcal{P}$. $\square$

This corollary establishes that convolution of distributions is jointly sequentially continuous in each argument (when the other is fixed), a crucial property for approximation arguments.
