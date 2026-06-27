---
role: proof
locale: en
of_concept: well-ordering-of-constructible-universe
source_book: gtm008
source_chapter: "7"
source_section: "Relative Constructibility"
---
If $b \in a'$ then there is a formula $\varphi$ of $\mathcal{L}(\{K(\cdot)\})$ and a finite set of constants $\{c_1, \ldots, c_n\} \subseteq a$ for which

$$b = \{x \in a \mid \langle a, k \rangle \models \varphi(x, c_1, \ldots, c_n)\}$$

Thus $b$ is determined by $\langle \lceil \varphi \rceil^*, \{c_1, \ldots, c_n\} \rceil$. The set of formulas of $\mathcal{L}(\{K(\cdot)\})$ is countable and the finite subsets of constants from $a$ can be well ordered since $a$ is well ordered. This gives a well ordering of $a'$.

Since $L_{K_0}$ is a model of $ZF$ it then follows from the foregoing argument that $A_{\alpha+1}$ is well ordered in $L_{K_0}$ if $A_{\alpha}$ is well ordered in $L_{K_0}$. Thus by induction on $\alpha$ there are relations $<_\alpha$ in $L_{K_0}$ such that $<_\alpha$ well orders $A_{\alpha}$ ($<_\alpha$ is definable uniformly for all $\alpha$ in $L_{K_0}$).
