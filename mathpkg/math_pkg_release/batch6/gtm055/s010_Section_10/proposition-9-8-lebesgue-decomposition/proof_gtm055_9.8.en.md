---
role: proof
locale: en
of_concept: proposition-9-8-lebesgue-decomposition
source_book: gtm055
source_chapter: "9"
source_section: "2"
---

The proof constructs $
u_1$ as the supremum (in the sense of measures) of all measures of the form $
u_f$, where $f$ ranges over nonnegative measurable functions such that $
u_f \leq 
u$ and $
u_f \ll \mu$. One verifies that this supremum is attained by some $f_0$, and then $
u_1$ is defined as the indefinite integral of $f_0$ with respect to $\mu$. Defining $
u_2 = 
u - 
u_1$, the key step is showing that $
u_2 \perp \mu$. This is accomplished by considering the signed measures $rac{1}{n}\mu - 
u_2$ and applying the Hahn decomposition: one constructs a set $A$ on which $
u_2$ is concentrated and $\mu(A) = 0$. Uniqueness follows from the uniqueness of the Radon--Nikodym derivative and the fact that a measure cannot be simultaneously absolutely continuous and singular with respect to $\mu$ unless it is the zero measure. The $\sigma$-finiteness hypothesis ensures the construction can be carried out on exhausting sequences of finite-measure sets.
