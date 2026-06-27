---
role: exercise
locale: en
chapter: "2"
section: "Exercises"
exercise_number: 12
---

([Lawvere '63, Chapter III, Theorem 2], [Linton '66, section 2]). Let $U: \mathcal{A} \longrightarrow \mathbf{Set}$ be a tractable functor (1.5.44). For each set $n$, let $nT$ be the set of natural transformations from $U^n$ to $U$. Define $n\eta: n \longrightarrow nT$, $i \longmapsto \mathrm{pr}_i: U^n \longrightarrow U$. Given $\alpha: n_1 \longrightarrow n_2 T$, $\beta: n_2 \longrightarrow n_3 T$, define

$$\langle i, \alpha \circ \beta \rangle = (\beta_j : j \in n_2) \cdot \alpha_i : U^{n_3} \longrightarrow U \quad (i \in n_1).$$

(a) Prove that $\mathbf{T} = (T, \eta, \circ)$ is an algebraic theory in $\mathbf{Set}$.

(b) Define $\Phi: \mathcal{A} \longrightarrow \mathbf{Set}^T$ by $A\Phi = (AU, \xi_A)$ where, for $\omega \in AUT$, $\omega \xi_A = \langle \mathrm{id}_{AU}, A\omega \rangle$. Show that $\Phi$ is a well-defined functor over $\mathbf{Set}$ and that $\Phi$ is an algebraic reflection.
