---
role: proof
locale: en
of_concept: theorem-7-27
source_book: gtm008
source_chapter: "2"
source_section: "2 There is a class"
---
We prove by induction that $A_\alpha \in M$. Clearly $A_0 = 0 \in M$. If $A_\alpha \in M$ then $\bar{K}_\alpha = A_\alpha \cap K \in M$, hence $A_\alpha = \langle A_\alpha, \bar{K}_\alpha \rangle \in M$. By Theorem 7.10, $Df(A_\alpha)$ is absolute with respect to $M$. Therefore $A_{\alpha+1} \subseteq M$. But $A$ a set implies that $Df(A)$ is a set. Therefore $Df(A_\alpha) \in M$, i.e.,

$$A_{\alpha

If $b \in a'$ then there is a formula $\varphi$ of $\mathcal{L}(\{K(\cdot)\})$ and a finite set of constants $\{c_1, \ldots, c_n\} \subseteq a$ for which

$$b = \{x \in a \mid \langle a, k \rangle \models \varphi(x, c_1, \ldots, c_n)\}$$

Thus $b$ is determined by $\langle \lceil \varphi \rceil^*, \{c_1, \ldots, c_n\} \rceil$. The set of formulas of $\mathcal{L}(\{K(\cdot)\})$ is countable and the finite subsets of constants from $a$ can be well ordered since $a$ is well ordered. This gives a well ordering of $a'$.

Since $L_{K_0}$ is a model of $ZF$ it then follows from the foregoing argument that $A_{\alpha+1}$ is well ordered in $L_{K_0}$ if $A_{\alpha}$ is well ordered in $L_{K_0}$. Thus by induction on $\alpha$ there are relations $<_{\alpha}$ in $L_{K_0}$ such that $<_{\alpha}$ well orders $A_{\alpha}(<_{\alpha}$ is definable uniformly for all $\alpha$ in $L_{K_0})$.

If $Od(a) \triangleq \mu_{\alpha}(a \in A_{\alpha})$, $a \in L_K$ and if

$$a < b \leftrightarrow a \in L_{K_0} \land b \in L_{K_0} \land [Od(a) < Od(b) \lor [Od(a) = Od(b) \land a <_{Od(a)} b]]$$

then $<$ is a well ordering of $L_{K_0}$ that is definable in $L_{K_0}$. In particular each $a \in L_{K_0}$ is well ordered by $\{\langle x, y \rangle \mid x < y \land x, y \in a\} \in L_{K_0}$.
