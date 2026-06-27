---
role: proof
locale: en
of_concept: theorem-4-13-perspectivity-subgroups
source_book: gtm006
source_chapter: IV
source_section: '5'
content_hash: bfdb354de875
written_against: efb5c684a67d
---

Clearly $\Gamma_{(k,\ell)} \leq \Gamma_\ell$ in both cases.

\textbf{Case (a).} $k \neq \ell$. Let $\alpha, \beta$ be any two elements of $\Gamma_{(k,\ell)}$. Clearly $k^\alpha = k^\beta = k$, so $k^{\alpha\beta^{-1}} = k$. Thus $\alpha\beta^{-1}$ is an element of $\Gamma_\ell$ whose centre, by Lemma 4.12, lies on $k$. Hence $\alpha\beta^{-1} \in \Gamma_{(k,\ell)}$.

\textbf{Case (b).} $k = \ell$. We know $\Gamma_{(P,\ell)}$ is a group for any $P$ and $\ell$. For $\alpha \in \Gamma_{(A,\ell)}$ and $\beta \in \Gamma_{(B,\ell)}$ with $A \neq B$, we show $\alpha\beta^{-1} \in \Gamma_{(\ell,\ell)}$. Since $\alpha\beta^{-1}$ fixes $\ell$ pointwise, it must have a centre. To show this centre is on $\ell$, it suffices to show $X^{\alpha\beta^{-1}} \neq X$ for any $X \notin \ell$. If $X^{\alpha\beta^{-1}} = X$, then $X^\alpha = X^\beta$. Since $A$ is the centre of $\alpha$, $A, X, X^\alpha$ are collinear. Similarly $B, X, X^\beta$ are collinear. But $X^\alpha = X^\beta$ implies $A, B$ are both on $XX^\alpha$, which is impossible since $\ell = AB$ and $X \notin \ell$. Thus $\alpha\beta^{-1} \in \Gamma_{(\ell,\ell)}$.