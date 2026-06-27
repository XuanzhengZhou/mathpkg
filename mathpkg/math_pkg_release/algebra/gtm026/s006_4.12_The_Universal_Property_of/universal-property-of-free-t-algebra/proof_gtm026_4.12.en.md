---
role: proof
locale: en
of_concept: universal-property-of-free-t-algebra
source_book: gtm026
source_chapter: "4"
source_section: "4.12"
---

We have already remarked that $(AT, A\mu)$ is a $T$-algebra. The morphism $fT: (AT, A\mu) \longrightarrow (XT, X\mu)$ is a $T$-homomorphism precisely because $\mu$ is natural (3.15). The structure map $\xi: (XT, X\mu) \longrightarrow (X, \xi)$ is a $T$-homomorphism by (4.10). Therefore, $f^{\#}$ as defined by the composite

$$
AT \xrightarrow{fT} XT \xrightarrow{\xi} X
$$

is a $T$-homomorphism.

Because $\eta$ is natural (3.11), we have

$$
A\eta \cdot f^{\#} = A\eta \cdot fT \cdot \xi = f \cdot X\eta \cdot \xi = f
$$

using (4.9), which states that $X\eta \cdot \xi = \mathrm{id}_X$. This verifies that $f^{\#}$ satisfies the required commutativity condition $A\eta \cdot f^{\#} = f$.

It remains to show uniqueness, and this is where (for the first time) the law

$$
A\eta T \cdot A\mu = \mathrm{id}_{AT}
$$

of 3.16 gets used. Suppose $g: AT \longrightarrow X$ is any $\mathcal{K}$-morphism satisfying

$$
A\eta \cdot g = f \quad \text{and} \quad A\mu \cdot g = gT \cdot \xi.
$$

The second equation states precisely that $g$ is a $T$-homomorphism. Since $T$ is a functor, applying $T$ to the first equation yields $A\eta T \cdot gT = fT$. Now compute:

$$
g = \mathrm{id}_{AT} \cdot g = A\eta T \cdot A\mu \cdot g = A\eta T \cdot gT \cdot \xi = fT \cdot \xi = f^{\#}.
$$

The first equality uses the law of 3.16, the second uses the $T$-homomorphism condition on $g$, and the third uses $A\eta T \cdot gT = fT$. Thus $g = f^{\#}$, establishing uniqueness.

The proof is complete. $\square$
