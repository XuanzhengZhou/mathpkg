---
role: proof
locale: en
of_concept: hanf-number-existence-theorem
source_book: gtm037
source_chapter: "4"
source_section: "Model Theory"
---

For each $\Gamma \in \mathrm{pr}_0^* R$, let

$$f_\Gamma = 0 \quad \text{if } \forall p \,\exists \mathfrak{A} \,\exists n \; [(\Gamma, \mathfrak{A}, n) \in R \text{ and } n \geq p],$$

$$f_\Gamma = \text{least } p \text{ such that } \forall \mathfrak{A} \,\forall n \; [(\Gamma, \mathfrak{A}, n) \in R \Rightarrow n < p] \quad \text{otherwise}.$$

Let

$$m = \left(\bigcup \{f_\Gamma : \Gamma \in \mathrm{pr}_0^* R\}\right)^+.$$

Then $m$ satisfies the condition of the theorem. In fact, suppose $\Gamma \in \mathrm{pr}_0^* R$ and (i) holds, say $(\Gamma, \mathfrak{A}, n) \in R$ with $n \geq m$. If the second condition in the definition of $f_\Gamma$ holds, we would have $n < f_\Gamma < m \leq n$, contradiction. Thus the first condition holds, which is precisely condition (ii) in the statement of the theorem.

The proof uses the replacement axiom of set theory to ensure that $\{f_\Gamma : \Gamma \in \mathrm{pr}_0^* R\}$ is a set, since $\mathrm{pr}_0^* R$ is a set by definition of a Hanf system. The successor cardinal of its union therefore exists and serves as the desired $m$.
