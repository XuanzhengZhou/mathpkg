---
role: proof
locale: en
of_concept: every-recursive-function-syntactically-definable-in-r
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

Let $A = \{f : f \text{ is syntactically definable in } R\}$. We use Julia Robinson's theorem (3.48) to show that every recursive function is in $A$.

**I. $+$ is in $A$.** Let $\varphi$ be the formula $v_0 + v_1 = v_2$; obviously the desired conditions of 14.1 hold.

**II. $\cdot$ is in $A$.** Let $\varphi$ be $v_0 \cdot v_1 = v_2$.

**III. $U_i^n \in A$ for $0 \leq i < n$.** Let $\varphi$ be $v_i = v_n$.

**IV. The excess function $\operatorname{Exc} \in A$.** Let $\varphi$ be the formula:
$$\exists v_2 [v_2 \cdot v_2 \leq v_0 \land v_0 < (v_2 + \mathbf{1}) \cdot (v_2 + \mathbf{1}) \land v_1 + v_2 \cdot v_2 = v_0].$$
Then $R \models \varphi(\mathbf{x}, v_1) \rightarrow v_1 = \operatorname{Exc}(x)$. Using 14.9(iv) we have $R \models v_0 \leq \mathbf{x} \rightarrow v_0 = \mathbf{0} \lor \cdots \lor v_0 = \mathbf{x}$. Let $y$ be the integer part of $\sqrt{x}$, so $y^2 \leq x < (y+1)^2$ and $\operatorname{Exc}(x) = x - y^2$. Then for the formula $\psi$ expressing the condition, one checks using the key number-theoretic fact that if $i \neq y$ or $j \neq \operatorname{Exc}(x)$, then $x \neq i^2 + j$, that the defining conditions hold.

**V. $A$ is closed under composition.** Let $f \in A$ be $m$-ary, syntactically defined by $\varphi$, and for each $i < m$, let $g_i \in A$ be $n$-ary, syntactically defined by $\psi_i$. Let $h(x_0, \ldots, x_{n-1}) = f(g_0(x_0, \ldots, x_{n-1}), \ldots, g_{m-1}(x_0, \ldots, x_{n-1}))$. Define $\chi$ as:
$$\exists v_{n+1} \cdots \exists v_{n+m} \left[ \bigwedge_{i < m} \psi_i(x_0, \ldots, x_{n-1}, v_{n+i+1}) \land \varphi(v_{n+1}, \ldots, v_{n+m}, v_n) \right].$$
For any $i < m$, since $\psi_i$ syntactically defines $g_i$ in $R$, we have $R \models \psi_i(\mathbf{x}_0, \ldots, \mathbf{x}_{n-1}, v_{n+i+1}) \rightarrow v_{n+i+1} = \mathbf{y}_i$ where $y_i = g_i(x_0, \ldots, x_{n-1})$. It follows that $R \models \chi \rightarrow \varphi(\mathbf{y}_0, \ldots, \mathbf{y}_{m-1}, v_n)$ and hence $R \models \chi \rightarrow v_n = \mathbf{z}$ where $z = h(x_0, \ldots, x_{n-1})$.

**VI. $A$ is closed under inversion (applied to functions with range $\omega$).** Let $f \in A$ with range $\omega$, syntactically defined by $\varphi$. Let $\psi$ be:
$$\varphi(v_1, v_0) \land \forall v_2[\varphi(v_2, v_0) \rightarrow v_1 \leq v_2].$$
We show $\psi$ syntactically defines $f^{(-1)}$ in $R$. Let $x \in \omega$ and $f^{(-1)}(x) = y$, so $f(y) = x$. Then $R \models \varphi(\mathbf{y}, \mathbf{x})$. Using the lemma that $R \models \varphi(v_2, \mathbf{x}) \rightarrow \mathbf{y} \leq v_2$ (which follows from 14.9(iv) and the properties of $f^{(-1)}$), we verify the two conditions of 14.1.

By Julia Robinson's theorem (3.48), every recursive function belongs to $A$, completing the proof.
