---
role: proof
locale: en
of_concept: cor-3
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Corollary 3: Existence of a Discrete-Time Markov Process

**Corollary 3.** Let $T = \{0, 1, 2, \ldots\}$ and let $\{P_k(x; B)\}$ be a family of transition probabilities (one-step transition kernels) on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$, where for each $k$ and $x$, $P_k(x; \cdot)$ is a probability measure, and for each $B$, $P_k(\cdot; B)$ is Borel measurable. Let $\pi$ be a probability measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

Then there exist a probability space $(\Omega, \mathcal{F}, \mathsf{P})$ and a random sequence $X = (X_n)_{n \geq 0}$ with the finite-dimensional distributions

$$\mathsf{P}\{X_0 \in B_0, X_1 \in B_1, \ldots, X_n \in B_n\} = \int_{B_0} \pi(dx_0) \int_{B_1} P_0(x_0; dx_1) \cdots \int_{B_n} P_{n-1}(x_{n-1}; dx_n).$$

*Proof.* This is the discrete-time analogue of Corollary 2. The finite-dimensional distributions are defined by iterated integration and are consistent by construction (no additional Chapman--Kolmogorov condition is needed for one-step transitions, as the consistency follows from the fact that each $P_k(x; \cdot)$ is a probability measure). The existence follows from the Ionescu Tulcea theorem (Theorem 2), which applies to arbitrary measurable spaces and does not require any topological assumptions.

Specifically, we set $\Omega_k = \mathbb{R}$, $\mathcal{F}_k = \mathcal{B}(\mathbb{R})$, $P_1 = \pi$, and $P(x_0, \ldots, x_{k-1}; B) = P_{k-1}(x_{k-1}; B)$ (the transition depends only on the last state). The measurability condition is satisfied since transition probabilities are Borel measurable by hypothesis. The Ionescu Tulcea theorem then guarantees the existence of the unique probability measure $P$ on the product space with the specified finite-dimensional distributions. The coordinate process $X_n(\omega) = \omega_n$ is the desired Markov chain. $\square$
