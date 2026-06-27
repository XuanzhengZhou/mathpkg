---
role: proof
locale: en
of_concept: birkhoff-subcategory-induces-theory-map
source_book: gtm026
source_chapter: "3"
source_section: "3.2"
---

For $\gamma: C \longrightarrow DT'$ we have $\beta^{\#\#} \cdot \gamma^{\#\#} = (\beta \cdot \gamma^{\#\#})^{\#\#}$. For $\alpha: A \longrightarrow BT'$, define $\alpha \circ \beta = \alpha \cdot \beta^{\#\#}$. Then

$$(\alpha \circ \beta) \circ \gamma = (\alpha \cdot \beta^{\#\#}) \cdot \gamma^{\#\#} = \alpha \cdot (\beta \cdot \gamma^{\#\#})^{\#\#} = \alpha \circ (\beta \circ \gamma).$$

Define $X\eta': X \longrightarrow XT'$ by $X\eta' = X\eta \cdot X\lambda$. Then for $f: A \longrightarrow B$,

$$(f \cdot B\eta') \circ \gamma = f \cdot B\eta \cdot B\lambda \cdot \beta^{\#\#} = f \cdot \beta.$$

Also, $(B\eta \cdot B\lambda)^{\#\#} = \text{id}_{BT'}$, so

$$\alpha \circ B\eta' = \alpha \cdot (B\eta \cdot B\lambda)^{\#\#} = \alpha.$$

Given $a: A \longrightarrow BT$ and $b: B \longrightarrow CT$, we have the associativity condition

$$B\lambda \cdot (b \cdot C\lambda)^{\#\#} = (b \cdot C\lambda)^{\#\#} = b^{\#} \cdot C\lambda,$$

since $C\lambda$ is a $\mathbf{T}$-homomorphism. This shows that $\mathbf{T}' = (T', \eta', \mu')$ is an algebraic theory and that $\lambda: \mathbf{T} \longrightarrow \mathbf{T}'$ is a theory map.

To see that $(XT', X\mu')V = (XT', \xi_X)$, that is, $\xi_X = XT' \cdot \lambda \cdot X\mu'$, observe that

$$\xi_X: (XT'T, XT'\mu) \longrightarrow (XT', \xi_X)$$

and

$$XT'\lambda: (XT'T, XT'\mu) \longrightarrow (XT'T', \xi_{XT'})$$

are $\mathbf{T}$-homomorphisms by definition, and

$$X\mu': (XT'T', \xi_{XT'}) \longrightarrow (XT', \xi_X)$$

is a $\mathbf{T}'$-homomorphism such that $B\eta' \cdot \beta^{\#\#\#} = \beta$. Applying $V$, $\beta^{\#\#\#}: (BT', \xi_B) \longrightarrow (CT', \xi_C)$ is a $\mathbf{T}$-homomorphism such that $B\eta \cdot B\lambda \cdot \beta^{\#\#\#} = \beta$. Therefore, $\beta^{\#\#\#} = \beta^{\#\#}$.
