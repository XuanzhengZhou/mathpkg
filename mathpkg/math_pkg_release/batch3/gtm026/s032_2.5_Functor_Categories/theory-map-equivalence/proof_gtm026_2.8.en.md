---
role: proof
locale: en
of_concept: theory-map-equivalence
source_book: gtm026
source_chapter: "2"
source_section: "2.8"
---

**1 implies 2.** Recall that in the clone form (1.3.14), the Kleisli composition $\alpha \circ \beta$ for $\alpha: A \to BT$ and $\beta: B \to CT$ is defined by $\alpha \circ \beta = A\eta \cdot \alpha T \cdot \mu_C$. Using the naturality of $\lambda$ and the commutativity of the theory map diagrams, one verifies:
$$
K\eta \cdot K\lambda = K\eta',
$$
and the preservation of Kleisli composition:
$$
(\alpha \circ \beta) \cdot C\lambda = (\alpha \cdot B\lambda) \circ' (\beta \cdot C\lambda).
$$

**2 implies 1.** To prove that $\lambda: T \to T'$ is natural, let $f: A \to B$ in $\mathcal{K}$ and recall the definition of $fT: AT \to BT$ from 1.3.10. We have:
$$
fT \cdot B\lambda = (\mathrm{id}_{AT} \circ f^A) \cdot B\lambda = A\lambda \circ' (f^A \cdot B\lambda) = A\lambda \circ' (f \cdot B\eta') = A\lambda \cdot fT',
$$
where the last step uses 1.3.12 (the unit law for Kleisli composition). This establishes naturality.

For the unit condition ($\eta \cdot \lambda = \eta'$), condition (2) with $\alpha = \mathrm{id}_A$ and $\beta = \mathrm{id}_B$ yields the result. For the multiplication condition ($\mu \cdot \lambda = \lambda\lambda \cdot \mu'$):
$$
A\mu \cdot A\lambda = (\mathrm{id}_{ATT} \circ \mathrm{id}_{AT}) \cdot A\lambda = (\mathrm{id}_{ATT} \cdot AT\lambda) \circ' (\mathrm{id}_{AT} \cdot A\lambda) = AT\lambda \circ' A\lambda = AT\lambda \cdot A\lambda T' \cdot A\mu' = A\lambda\lambda \cdot A\mu'.
$$
