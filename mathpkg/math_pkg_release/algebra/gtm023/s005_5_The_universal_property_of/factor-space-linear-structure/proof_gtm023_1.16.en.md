---
role: proof
locale: en
of_concept: factor-space-linear-structure
source_book: gtm023
source_chapter: "1"
source_section: "1.16"
---

**Uniqueness:** Assume that $E/E_1$ is made into a vector space such that $\pi$ is a linear mapping. Then the equations

$$\pi(x + y) = \pi x + \pi y \quad \text{and} \quad \pi(\lambda x) = \lambda \pi x$$

show that the linear operations in $E/E_1$ are uniquely determined by those in $E$.

**Existence:** Let $\bar{x}$ and $\bar{y}$ be two arbitrary elements of $E/E_1$ and choose $x, y \in E$ such that $\pi x = \bar{x}$, $\pi y = \bar{y}$. The class $\pi(x + y)$ depends only on $\bar{x}$ and $\bar{y}$; indeed, if $x' \in E$ also satisfies $\pi x' = \bar{x}$, then $x' - x \in E_1$, so $(x' + y) - (x + y) \in E_1$, hence $\pi(x' + y) = \pi(x + y)$. Define addition by $\bar{x} + \bar{y} = \pi(x + y)$. This makes $E/E_1$ an abelian group with $\bar{0} = E_1$ as zero.

Similarly, for scalar multiplication, the class $\pi(\lambda x)$ depends only on $\bar{x}$. Define $\lambda \cdot \bar{x} = \pi(\lambda x)$. This satisfies axioms II.1--II.3, making $E/E_1$ into a vector space. By construction, $\pi(x + y) = \pi x + \pi y$ and $\pi(\lambda x) = \lambda \pi x$, so $\pi$ is linear.
