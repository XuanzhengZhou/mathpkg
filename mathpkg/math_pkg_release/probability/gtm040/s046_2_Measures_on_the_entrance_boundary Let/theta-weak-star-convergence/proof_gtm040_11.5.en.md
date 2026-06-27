---
role: proof
locale: en
of_concept: theta-weak-star-convergence
source_book: gtm040
source_chapter: "11"
source_section: "2"
---

**Proof of Proposition 11-5.** The proof proceeds by considering the continuous functions on ${}^*S$ whose restrictions to $S$ have limits at infinity (i.e., along the entrance boundary $B^e$). For any such function $f$, the recurrence formula of Proposition 11-3 yields

$$\sum_{j \in E_k} \theta^{E_k}_j f(j) = \sum_{j \in E_k} \nu_j (I - P^{E_k})_{jj} f(j) + f(0).$$

As $k \to \infty$, the right-hand side converges to $\int_{S \cup B^e} f(x) \, d\beta^\nu(x)$ by the integral representation of Proposition 11-2 and the definition of the Martin kernel. Since the continuous functions with limits at infinity are dense in $C({}^*S)$, the weak-star convergence follows. The finiteness of each $E_k$ guarantees that $\theta^{E_k}$ is a probability measure, and the increasing union $\bigcup E_k = S$ ensures that the limit captures the full entrance boundary.
