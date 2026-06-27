---
role: proof
locale: en
of_concept: scc-implies-ucl
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

Suppose that there is a family of sequences $\langle b_{\alpha i} \mid \alpha \in On \rangle$ for each $i \in I$, where $I$ is a set, such that
$$\{b_{\alpha i} \mid \alpha \in On \land i \in I\} \subseteq B,$$
$$(\forall i \in I)(\forall \alpha)(\forall \beta)[\alpha < \beta \rightarrow b_{\alpha i} \geq b_{\beta i}],$$
and
$$(\forall i \in I)\left[\prod_{\alpha \in On} b_{\alpha i} = 0\right].$$

Then, for each $i \in I$, $\langle -b_{\alpha i} \mid \alpha \in On \rangle$ is nondecreasing and converges to $1$. By the s.c.c., these sequences must eventually become constant, i.e.,
$$(\forall i \in I)(\exists \beta_i)[-b_{\beta_i} = 1],$$
$$(\forall i \in I)(\forall \alpha \geq \beta_i)[b_{\alpha i} = 0].$$

Let $\beta = \sup_{i \in I} \beta_i$ (note that $I$ is a set). Then $(\forall \alpha > \beta)[\sum_{i \in I} b_{\alpha i} = 0]$, which verifies the UCL.
