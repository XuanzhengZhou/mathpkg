---
role: proof
locale: en
of_concept: tvs-compatibility-conditions
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "11. Real and complex topological vector spaces"
---

# Proof of TVS Compatibility Conditions

**Theorem (11.3).** Let $E$ be a vector space over $\mathbb{K}$ and let $\tau$ be a topology on $E$. Then $\tau$ is compatible with the vector space structure of $E$ if and only if (i) $\tau$ is compatible with the additive group structure of $E$, (ii) for each $x \in E$, the mapping $\lambda \mapsto \lambda x$ ($\lambda \in \mathbb{K}$) is continuous at $\lambda = 0$, (iii) for each $\lambda \in \mathbb{K}$, the mapping $x \mapsto \lambda x$ ($x \in E$) is continuous at $x = \theta$, and (iv) the mapping $(\lambda, x) \mapsto \lambda x$ ($\lambda \in \mathbb{K}, x \in E$) is continuous at $(0, \theta)$.

*Proof.* **Only if:** Conditions (ii)–(iv) follow trivially from the definition of a TVS (11.1). Condition (i) results from the continuity of $(x, y) \mapsto x + y$ and $x \mapsto (-1)x = -x$ (1.2).

**If:** Let $\lambda_0 \in \mathbb{K}$, $x_0 \in E$; the problem is to show that $(\lambda, x) \mapsto \lambda x$ is continuous at $(\lambda_0, x_0)$. Let $U$ be a neighborhood of $\lambda_0 x_0$. We seek neighborhoods $A$ of $\lambda_0$ in $\mathbb{K}$ and $V$ of $x_0$ in $E$ such that $A V \subset U$. Write

$$(\lambda_0 + \alpha)(x_0 + y) = \lambda_0 x_0 + \lambda_0 y + \alpha x_0 + \alpha y.$$

By (i), addition is continuous at $(\lambda_0 x_0, \theta)$, so there exist neighborhoods $W_1, W_2$ of $\theta$ such that $\lambda_0 x_0 + W_1 + W_2 \subset U$. Specifically, choose a neighborhood $W$ of $\theta$ with $W + W \subset U - \lambda_0 x_0$.

By (ii), there exists $\delta_1 > 0$ such that $|\alpha| < \delta_1$ implies $\alpha x_0 \in W$. By (iii), there exists a neighborhood $V$ of $\theta$ such that $\lambda_0 y \in W$ for all $y \in V$. By (iv), there exist $\delta_2 > 0$ and a neighborhood $V'$ of $\theta$ such that $|\alpha| < \delta_2$ and $y \in V'$ imply $\alpha y \in W$.

Taking $\delta = \min(\delta_1, \delta_2)$ and setting $A = \{\alpha \in \mathbb{K} : |\alpha| < \delta\}$, and taking a neighborhood $V_0$ of $\theta$ with $V_0 \subset V \cap V'$, we obtain $(\lambda_0 + A)(x_0 + V_0) \subset U$. Translating to $x_0$ via the additive continuity, the result follows. $\square$
