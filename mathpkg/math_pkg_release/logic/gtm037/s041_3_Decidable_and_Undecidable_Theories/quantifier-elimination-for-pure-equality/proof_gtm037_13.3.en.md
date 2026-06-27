role: proof
locale: en
of_concept: quantifier-elimination-for-pure-equality
source_book: gtm037
source_chapter: "13"
source_section: "3"
---

The atomic case is trivial, and the induction steps using $\neg$, $\lor$, $\land$ are trivial. As in previous proofs it now suffices to assume that $\varphi$ has the form $\exists\alpha\psi$, with $\psi$ a quantifier-free combination of basic formulas. Since the formulas $\varepsilon_m$ are sentences, and since $\alpha = \alpha$ is equivalent to $\varepsilon_1$, we may assume that $\varphi$ has the form

$$\exists\alpha\,[\alpha = \beta_0 \land \cdots \land \alpha = \beta_{m-1} \land \neg(\alpha = \beta_m) \land \cdots \land \neg(\alpha = \beta_{n-1})]$$

where $\beta_0, \ldots, \beta_{n-1}$ are distinct variables different from $\alpha$.

If $m > 0$, then $\varphi$ is clearly equivalent to

$$\bigwedge_{i < j < m} \beta_i = \beta_j \land \neg(\beta_0 = \beta_m) \land \cdots \land \neg(\beta_0 = \beta_{n-1})$$

(or to $\varepsilon_1$ if $m = 1$ and $n = m$). Hence we may assume that $m = 0$.

Let $I = \{i : m \leq i < n\} = \{0, \ldots, n-1\}$. We claim

$$\models \varphi \leftrightarrow \bigwedge_{J \subseteq I} \left(\bigwedge_{i, j \in J, i \neq j} \neg(\beta_i = \beta_j) \rightarrow \varepsilon_{|J|+1}\right). \tag{1}$$

To prove (1), first let $A$ be any set and let $x \in {}^\omega A$. Suppose $x$ satisfies $\varphi$ in $\mathfrak{A}$, let $J \subseteq I$, and suppose $x$ satisfies $\bigwedge_{i, j \in J, i \neq j} \neg(\beta_i = \beta_j)$ in $A$. Write $\beta_i = v_{k_i}$ for all $i \in I$, and $\alpha = v_t$. Thus $x_{k_i} \neq x_{k_j}$ for distinct $i, j \in J$, and $x_t \neq x_{k_i}$ for all $i \in I$. Consequently $|\{x_t\} \cup \{x_{k_i} : i \in J\}| = |J| + 1$, so $A$ has at least $|J| + 1$ elements, i.e., $x$ satisfies $\varepsilon_{|J|+1}$. This shows the forward direction of (1).

Conversely, suppose the right-hand side of (1) holds in $A$ under the assignment $x$. We need to find an element $a \in A$ such that $a \neq x_{k_i}$ for all $i \in I$. Let $J$ be a maximal subset of $I$ such that the values $\{x_{k_i} : i \in J\}$ are pairwise distinct. Then the right-hand side implies that $A$ satisfies $\varepsilon_{|J|+1}$, so $|A| \geq |J| + 1$. Since $\{x_{k_i} : i \in J\}$ has exactly $|J|$ elements, there exists $a \in A$ not in this set. By maximality of $J$, this $a$ is also distinct from $x_{k_i}$ for all $i \in I \setminus J$. Thus $a$ witnesses the existential quantifier in $\varphi$, completing the proof of (1).

The right-hand side of (1) is a quantifier-free Boolean combination of the sentences $\varepsilon_k$, establishing the quantifier elimination result for $\Gamma_3$.
