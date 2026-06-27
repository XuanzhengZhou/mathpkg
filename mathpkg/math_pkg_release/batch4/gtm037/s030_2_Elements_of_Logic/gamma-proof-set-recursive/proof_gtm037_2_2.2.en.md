---
role: proof
locale: en
of_concept: gamma-proof-set-recursive
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

For any $x \in \omega$, we have $x \in g^{+*}(\Gamma\text{-Prf})$ iff $x > 1$ and for every $i \leq \ln(x)$ one of the following conditions holds:

\begin{enumerate}
\item[(1)] $(x)_i \in g^{+*} \operatorname{Axm}$,
\item[(2)] $(x)_i \in g^{+*} \Gamma$,
\item[(3)] $\exists j, k < i \; (x)_k = (x)_j \to' (x)_i$,
\item[(4)] $\exists j < i \; \exists k \leq x \; [k \in \operatorname{Rng} (g \circ v) \text{ and } (x)_i = \forall' 2^{k+1} (x)_j]$.
\end{enumerate}

Here $(x)_i$ denotes the $i$-th component of the sequence coded by $x$ (i.e., the exponent of the $i$-th prime in the prime factorization of $x$), $\ln(x)$ is the length of the sequence, $\to'$ is the Godel number function for the implication connective, and $\forall'$ codes the universal quantifier.

Since $g^{+*} \operatorname{Axm}$ is recursive (Proposition 10.25), $g^{+*} \Gamma$ is recursive by hypothesis, and conditions (3) and (4) involve only bounded quantifiers and recursive operations, the entire disjunction is a recursive predicate. Therefore $g^{+*}(\Gamma\text{-Prf})$ is recursive.
