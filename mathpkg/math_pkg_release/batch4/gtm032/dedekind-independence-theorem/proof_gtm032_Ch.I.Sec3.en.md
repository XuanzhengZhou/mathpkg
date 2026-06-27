---
role: proof
locale: en
of_concept: dedekind-independence-theorem
source_book: gtm032
source_chapter: "I"
source_section: "3"
---

Suppose $\sum_{i=1}^{n} s_i \rho_i = 0$ with not all $\rho_i = 0$. Choose a relation with the minimal number $m$ of non-zero $\rho_i$. By reindexing, we may assume $\rho_1, \dots, \rho_m \neq 0$ and $\sum_{i=1}^{m} s_i \rho_i = 0$. Note that $m > 1$ since $s_1 \rho_1 = 0$ would imply $\rho_1 = 0$ (as $s_1$ is injective). Since $s_1 \neq s_2$, there exists $\eta \in E$ such that $\eta^{s_1} \neq \eta^{s_2}$. Multiply the relation on the left by $\eta_R$:

$$0 = \eta_R\left(\sum_{i=1}^{m} s_i \rho_i\right) = \sum_{i=1}^{m} \eta_R s_i \rho_i = \sum_{i=1}^{m} s_i (\eta^{s_i})_R \rho_i = \sum_{i=1}^{m} s_i (\eta^{s_i} \rho_i).$$

Also multiply the original relation by $\eta^{s_1}$ on the right:

$$0 = \left(\sum_{i=1}^{m} s_i \rho_i\right) (\eta^{s_1})_R = \sum_{i=1}^{m} s_i (\rho_i \eta^{s_1}).$$

Subtracting the two expressions gives:

$$0 = \sum_{i=1}^{m} s_i (\eta^{s_i} \rho_i - \rho_i \eta^{s_1}) = \sum_{i=2}^{m} s_i (\eta^{s_i} - \eta^{s_1}) \rho_i.$$

Since $\eta^{s_2} \neq \eta^{s_1}$, the coefficient of $s_2$ is non-zero. This gives a relation with fewer non-zero terms, contradicting the minimality of $m$. Hence all $\rho_i = 0$.
