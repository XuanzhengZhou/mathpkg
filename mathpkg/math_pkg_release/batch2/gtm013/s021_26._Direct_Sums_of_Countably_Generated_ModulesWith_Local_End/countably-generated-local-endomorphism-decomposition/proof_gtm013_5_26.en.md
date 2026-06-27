---
role: proof
locale: en
of_concept: countably-generated-local-endomorphism-decomposition
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

Let $M = \bigoplus_A M_\alpha$ where each $M_\alpha$ is countably generated and has a local endomorphism ring. By Corollary (26.2), every direct summand of $M$ is a direct sum of countably generated submodules (necessarily direct summands) of $M$. So it suffices to prove the result for a countably generated direct summand of $M$.

Thus, let $M = K \oplus L$ with $K$ countably generated. Let $x \in K$. Then there is a finite set $G \subseteq A$ with $x \in \bigoplus_G M_\alpha$. Set $N = \bigoplus_G M_\alpha$. By Lemma (26.4) there are direct summands $K' \leq K$ and $L' \leq L$ such that

$$M = N \oplus K' \oplus L'.$$

Let $H = K \cap (N \oplus L')$. Then $x \in K \cap N \subseteq H$, and by modularity

$$K = K \cap M = K \cap ((N \oplus L') \oplus K') = H \oplus K'.$$

Since $L'$ is a direct summand of $L$, there is a submodule $I \leq L$ with $L = I \oplus L'$. Thus

$$N \cong M / (K' \oplus L') \cong H \oplus I.$$

But by (12.7) the decomposition $N = \bigoplus_G M_\alpha$ complements direct summands. Hence $H$ is isomorphic to $\bigoplus_F M_\alpha$ for some finite subset $F \subseteq A$.

Now let $x_1, x_2, \ldots$ be a spanning set for $K$. Assume that there exists a direct decomposition

$$K = H_1 \oplus \cdots \oplus H_n \oplus K_n$$

of $K$ and finite subsets $F_1, \ldots, F_n$ of $A$ such that $x_1, \ldots, x_n \in H_1 \oplus \cdots \oplus H_n$ and $H_i \cong \bigoplus_{F_i} M_\alpha$ for $i = 1, \ldots, n$. Then using the same technique as above for $K_n$ and $x_{n+1}$, we can refine the decomposition to include $x_{n+1}$ in an additional summand $H_{n+1} \cong \bigoplus_{F_{n+1}} M_\alpha$. By induction, we obtain that $K$ is isomorphic to a direct sum of countably many submodules, each isomorphic to a finite direct sum of the $M_\alpha$. By regrouping, $K$ is a direct sum of countably generated modules, each isomorphic to a direct summand of some $M_\alpha$. By (12.7) each such summand has a local endomorphism ring.
