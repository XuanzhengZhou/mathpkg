---
role: proof
locale: en
of_concept: theorem-23-21
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
Suppose that there is a family of sequences $\langle b_{\alpha i} \mid \alpha \in On \rangle$ for each $i \in I$, where $I$ is a set, such that

$$\{b_{\alpha i} \mid \alpha \in On \land i \in I\} \subseteq B,$$
$$(\forall i \in I)(\forall \alpha)(\forall \beta)[\alpha < \beta \rightarrow b_{\alpha i} \geq b_{\beta i}],$$

and

$$(\forall i \in I)\left[\prod_{\alpha \in On} b_{\alpha i} = 0\right].$$

Then, for each $i \in I$, $\langle -b_{\alpha i} \mid \alpha \in On \rangle$ is nondecreasing and converges to 1. By the s.c.c., these sequences must eventually become constant, i.e.,

$$(\forall i \in I)(\exists \beta_i)[-b_{\beta_i} = 1],$$
$$(\forall i \in I)(\forall \alpha \geq \beta_i)[b_{\alpha i} = 0].$$

Let $\beta = \sup_{i \in I} \beta_i$ (note that $I$ is a set). Then

$$(\forall \alpha > \beta)\left[\sum_{i \in I}

Therefore assume (i) and let $a \in V^{(B)}$. Suppose that (ii) does not hold for $a$. Then for some $b \in B$,

$$0 < b \wedge b \cdot \llbracket (\exists v) (\forall x \in a) (\exists y \in v) \varphi'(x, y) \rrbracket = 0.$$

Then

$$(\forall x \in \mathcal{D}(a)) \left[ - \sum_{y \in V_{\alpha}^{(B)}} \llbracket \varphi'(x, y) \rrbracket = 0 \right]$$

by (i) and Theorem 23.15, hence

$$\sum_{x \in \mathcal{L}(a)} \left( - \sum_{y \in V_{\alpha}^{(B)}} \llbracket \varphi'(x, y) \rrbracket \right) = 0$$

by the UCL.

Therefore for some $\alpha \in On$,

$$\sum_{x \in \mathcal{D}(a)} \left( - \sum_{y \in V_{\alpha}^{(B)}} \llbracket \varphi'(x, y) \rrbracket \right) \neq b,$$

or by passing to complements,

(iii) $$\prod_{x \in \mathcal{D}(a)} \sum_{y \in V_{\alpha}^{(B)}} \llbracket \varphi'(x, y) \rrbracket \neq -b.$$

Let $v \in V^{(B)}$ be $v: V_{\alpha}^{(B)} \rightarrow \{1\}$, i.e., $v$ is the constant function $1$ on $V_{\alpha}^{(B)}$. Then by assumption

$$0 = b \cdot \llbracket (\forall x \in a) (\exists y \in v) \varphi'(x, y) \rrbracket$$

$$= b \cdot \prod_{x \in \mathcal{D}(a)} \left( a(x) \Rightarrow \sum_{y \in V_{\alpha}^{(B)}} \llbracket \varphi'
