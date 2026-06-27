```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.5"
proof_technique: set-theoretic-bijection
locale: en
content_hash: ""
written_against: ""
---
Define $\varphi \colon S_f(G) \to S(H)$ by $\varphi(K) = f(K)$. By Exercise 2.9, $f(K)$ is a subgroup of $H$ for every $K \in S_f(G)$, so $\varphi$ is well-defined. For any subgroup $J \leq H$, $f^{-1}(J)$ is a subgroup of $G$ and $\operatorname{Ker} f \leq f^{-1}(J)$, so $f^{-1}(J) \in S_f(G)$. Since $f$ is surjective, $f(f^{-1}(J)) = J$, proving $\varphi$ is surjective. Exercise 18 shows $f^{-1}(f(K)) = K$ if and only if $\operatorname{Ker} f \leq K$, which holds for all $K \in S_f(G)$. Hence $\varphi$ is injective. For normality: if $K \trianglelefteq G$, then $f(K) \trianglelefteq H$; conversely, if $J \trianglelefteq H$, then $f^{-1}(J) \trianglelefteq G$.
