---
role: proof
locale: en
of_concept: harmonic-measure-convergence-theorem
source_book: gtm040
source_chapter: "11"
source_section: "3"
---

**Proof of Theorem 11-7.** By Lemma 11-6, the row vector $\nu = G_{0\cdot}$ satisfies the admissibility conditions. Proposition 11-2 then guarantees the existence of a unique probability measure $\beta = \beta^\nu$ on $S \cup B^e$ such that
$$G_{0j} = \int_{S \cup B^e} {}_0N(x, j) \, d\beta(x).$$

The first assertion, that $\lambda^{E_k} \to \beta$ weak-star, follows from Proposition 11-5 and Lemma 11-6: by Lemma 11-6, $\nu_E(I - P^E) = \lambda^E_E - \delta_0$, which identifies the measures $\lambda^{E_k}$ with the escape measures $\theta^{E_k}$ constructed from $\nu = G_{0\cdot}$. Proposition 11-5 then yields the weak-star convergence.

For the independence of $0$, one uses the fact that for any two states $i$ and $j$, the Martin kernels are related by a Radon-Nikodym derivative that is a boundary limit of ratios of potential matrix entries. This ratio is a harmonic function on $S$, and the representing measure $\beta$ is characterized as the unique probability measure satisfying the integral representation for any choice of reference state. Since the weak-star limit of $\lambda^{E_k}$ does not reference a particular state, $\beta$ is independent of the distinguished state.

Finally, the integral representation for arbitrary $G_{ij}$ follows from the duality between the entrance and exit boundaries and the fact that the same harmonic measure $\beta$ serves as the representing measure for the entire potential kernel.
