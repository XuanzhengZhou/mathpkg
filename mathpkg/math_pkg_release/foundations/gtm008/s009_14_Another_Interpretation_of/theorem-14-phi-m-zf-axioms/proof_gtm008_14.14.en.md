---
role: proof
locale: en
of_concept: theorem-14-phi-m-zf-axioms
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

Let $\phi$ be $(\forall x)\psi(x)$. Then

$$[\phi^M] = [[(\forall x)[M(x) \rightarrow \psi(x)]]] = \prod_{u \in V^{(B)}} ([M(u)] \Rightarrow [\psi(u)])$$
$$= \prod_{u \in V^{(B)}} \left( \sum_{k \in V} [u = \check{k}] \Rightarrow [\psi(u)] \right)$$
$$= \prod_{u \in V^{(B)}} \prod_{k \in V} ([u = \check{k}] \Rightarrow [\psi(\check{k})])$$
$$= \prod_{k \in V} [\psi(\check{k})].$$

Now if $\phi$ is an axiom of ZF, then since $V$ is a model of ZF, $\psi(k)$ is true for each $k \in V$. Hence $(\forall k \in V) [\psi(\check{k})] = 1$, because $V^{(B)} \models ZF$.

A similar argument shows that if $\phi$ is $(\exists x)\psi(x)$, then $[\phi^M] = \sum_{k \in V} [\psi(\check{k})]$. Since $V$ is a model of ZF, $(\exists k_0 \in V)[\psi(k_0)]$, hence $[\psi(\check{k_0})] = 1$, so the sum is 1.
