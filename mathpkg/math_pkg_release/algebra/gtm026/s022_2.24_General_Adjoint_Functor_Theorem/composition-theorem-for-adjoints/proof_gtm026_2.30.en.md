---
role: proof
locale: en
of_concept: composition-theorem-for-adjoints
source_book: gtm026
source_chapter: "2"
source_section: "2.30"
---

Fix $C$ in $\mathcal{C}$. We check the universal property for the advertised unit $C\eta = C\eta_2 \cdot CF_2\eta_1U_2$. Let $f: C \rightarrow AU_1U_2$ be given. Since $(F_2, U_2, \eta_2, \varepsilon_2)$ is an adjointness, there exists unique $\psi: CF_2 \rightarrow AU_1$ in $\mathcal{B}$ such that $C\eta_2 \cdot \psi U_2 = f$.

Now, since $(F_1, U_1, \eta_1, \varepsilon_1)$ is an adjointness, there exists unique $f^\#: CF_2F_1 \rightarrow A$ in $\mathcal{A}$ such that $CF_2\eta_1 \cdot f^\# U_1 = \psi$.

It is now straightforward to verify that $f^\#$ is unique with respect to the property that $C\eta_2 \cdot CF_2\eta_1U_2 \cdot f^\# U_1U_2 = f$. Indeed,
$$C\eta_2 \cdot CF_2\eta_1U_2 \cdot f^\# U_1U_2 = C\eta_2 \cdot (CF_2\eta_1 \cdot f^\# U_1)U_2 = C\eta_2 \cdot \psi U_2 = f.$$

Uniqueness follows from the uniqueness at each step. The formula for the counit follows by duality from the formula for the unit via 2.17.
