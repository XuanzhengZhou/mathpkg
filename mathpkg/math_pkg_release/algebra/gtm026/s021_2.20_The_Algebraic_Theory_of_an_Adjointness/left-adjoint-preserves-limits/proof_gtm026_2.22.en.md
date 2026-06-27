---
role: proof
locale: en
of_concept: left-adjoint-preserves-limits
source_book: gtm026
source_chapter: "2"
source_section: "2.22"
---

Let $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$ be an adjointness. Let $(K, \Gamma)$ be a lower bound of $(\Delta, DU)$. For each $\alpha \in \Delta(i, j)$ we have

$$\Gamma_i \cdot \alpha(DU) = \Gamma_j$$

since $(K, \Gamma)$ is a lower bound. Applying the adjunction isomorphism $(-)^\sharp$, we obtain morphisms $\Gamma_i^\sharp\colon KF \longrightarrow D(i)$ in $\mathcal{A}$ such that

$$\Gamma_i^\sharp \cdot \alpha D = \Gamma_j^\sharp$$

for all $\alpha \in \Delta(i, j)$. Thus $(KF, \Gamma^\sharp)$ constitutes a lower bound of the original diagram $(\Delta, D)$ in $\mathcal{A}$.

Since $(L, \psi)$ is a limit of $(\Delta, D)$, there exists a unique map $f\colon KF \longrightarrow L$ with $f \cdot \psi_i = \Gamma_i^\sharp$ for all $i$.

Now define $f_\# = K\eta \cdot fU\colon K \longrightarrow LU$. We verify that $f_\#$ satisfies the required commutativity. For each $i$,

$$f_\# \cdot \psi_i U = K\eta \cdot fU \cdot \psi_i U = K\eta \cdot (f \cdot \psi_i)U = K\eta \cdot (\Gamma_i^\sharp)U.$$

By the adjunction identities, $(\Gamma_i^\sharp)U = \Gamma_i \cdot \eta U$ (up to composition order), and using the unit-counit triangle identities we obtain

$$f_\# \cdot \psi_i U = \Gamma_i$$

for all $i$.

For uniqueness, suppose $g\colon K \longrightarrow LU$ also satisfies $g \cdot \psi_i U = \Gamma_i$ for all $i$. Applying the adjunction isomorphism $(-)^\sharp$, we obtain $g^\sharp\colon KF \longrightarrow L$ with $g^\sharp \cdot \psi_i = \Gamma_i^\sharp$ for all $i$. By the uniqueness of the mediating morphism $f$ from the limit $(L, \psi)$, we have $g^\sharp = f$. Then

$$g = g^{\sharp\#} = f_\#$$

as desired. Thus $(LU, \psi U)$ is a limit of the diagram $(\Delta, DU)$.
