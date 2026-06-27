---
role: proof
locale: en
of_concept: lemma-4-14-elation-commutation
source_book: gtm006
source_chapter: IV
source_section: '5'
content_hash: 2e9c7f052b8d
written_against: 64d7a66a2452
---

Let $\alpha \in \Gamma_{(A,\ell)}$, $\beta \in \Gamma_{(B,\ell)}$ with $A \neq B$, both non-identity. By Lemma 4.11, $\beta^{-1}\alpha\beta$ is an $(A^\beta, \ell^\beta)$-elation. Since $\beta$ has axis $\ell$, $\beta^{-1}\alpha\beta$ is an $(A,\ell)$-elation. Similarly $\alpha^{-1}\beta^{-1}\alpha\beta \in \Gamma_{(B,\ell)}$.

Now write $\alpha^{-1}\beta^{-1}\alpha\beta = \alpha^{-1}(\beta^{-1}\alpha\beta)$, which lies in $\Gamma_{(A,\ell)}$. But also $\alpha^{-1}\beta^{-1}\alpha\beta = (\alpha^{-1}\beta^{-1}\alpha)\beta$, which lies in $\Gamma_{(B,\ell)}$. Thus
$$\alpha^{-1}\beta^{-1}\alpha\beta \in \Gamma_{(A,\ell)} \cap \Gamma_{(B,\ell)}.$$
Since any non-identity elation has a unique centre, $\Gamma_{(A,\ell)} \cap \Gamma_{(B,\ell)} = \{1\}$. Therefore $\alpha\beta = \beta\alpha$.

To complete the proof that $\Gamma_{(\ell,\ell)}$ is abelian, one must also show that two elations with the same centre commute. Let $\alpha_1, \alpha_2$ be non-trivial $(A,\ell)$-elations and let $\beta \neq 1$ be a $(B,\ell)$-elation for $B \neq A$. By the above, $\alpha_1\beta = \beta\alpha_1$ and $\alpha_2\beta = \beta\alpha_2$. By Exercise 4.9, the centre of $\alpha_1\beta$ differs from $A$, so $\alpha_1\beta$ commutes with $\alpha_2$. This yields $\alpha_1\alpha_2 = \alpha_2\alpha_1$.