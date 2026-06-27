---
role: proof
locale: en
of_concept: singer-group-difference-set-uniqueness
source_book: gtm006
source_chapter: "XIII"
source_section: "5"
---

*Proof.* Since $\Pi$ is regular on the points of $\mathcal{P}$, the points $X$ and $X^\beta$ are distinct; thus there is a unique line joining them. By the transitivity of $\Pi$ on lines, this line is $m^\alpha$ for some $\alpha \in \Pi$.

Now the points $X^{\alpha^{-1}}$ and $X^{\beta\alpha^{-1}}$ lie on $m = (m^\alpha)^{\alpha^{-1}}$. Therefore $\alpha^{-1} = \delta_2$ and $\beta\alpha^{-1} = \delta_1$ both belong to $\mathcal{D}$, and we have
$$\beta = (\beta\alpha^{-1})(\alpha^{-1})^{-1} = \delta_1 \delta_2^{-1}.$$

To prove uniqueness, suppose $\beta = \delta_1 \delta_2^{-1} = \delta_1' (\delta_2')^{-1}$ with $\delta_1,\delta_2,\delta_1',\delta_2' \in \mathcal{D}$. Then the two lines $m^{\delta_2}$ and $m^{\delta_2'}$ both join the distinct points $X^{\delta_1}$ and $X^{\delta_1'}$, which forces $\delta_2 = \delta_2'$ and $\delta_1 = \delta_1'$ by the uniqueness of the line joining two distinct points in a projective plane.

For the second representation, apply the same argument with the roles of points and lines interchanged (or consider the dual plane), yielding unique $\delta_3, \delta_4 \in \mathcal{D}$ such that $\beta = \delta_3^{-1} \delta_4$. $\square$

A corollary of this representation is that every element of $\Pi$ can be written as $\delta_1 \delta_2^{-1}$, which implies $|\mathcal{D}| \geq 3$ (otherwise $|\Pi| < 3$). Moreover, the points and lines of $\mathcal{P}$ are in one-to-one correspondence with the elements of $\mathcal{D}$.
