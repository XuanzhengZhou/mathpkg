---
role: proof
locale: en
of_concept: upward-lowenheim-skolem-without-equality
source_book: gtm037
source_chapter: "Part 5"
source_section: "Unusual Logics"
---

**Proof.** Fix $a \in A$ and define $f: B \to A$ by setting $f x = x$ for $x \in A$ and $f x = a$ for $x \in B \setminus A$. For each $m$-ary relational symbol $R$, let
$$R^{\mathfrak{B}} = \{ x \in {}^{m}B : f \circ x \in R^{\mathfrak{A}} \}.$$
This defines our $\mathcal{L}$-structure $\mathfrak{B}$. One easily checks the following key property:

(1) For any $x \in {}^{\omega}B$ and any formula $\varphi$ of $\mathcal{L}$ we have
$$\mathfrak{B} \models \varphi[x] \quad \text{iff} \quad \mathfrak{A} \models \varphi[f \circ x].$$

This is proved by induction on the complexity of $\varphi$. For atomic formulas $R v_{i_0} \cdots v_{i_{m-1}}$, it follows directly from the definition of $R^{\mathfrak{B}}$. The induction steps for $\neg$, $\lor$, $\land$ are straightforward. For the quantifier step, suppose $\varphi$ is $\exists v_k \psi$. If $\mathfrak{B} \models \exists v_k \psi[x]$, then there exists $b \in B$ such that $\mathfrak{B} \models \psi[x(b/k)]$, where $x(b/k)$ is the assignment that agrees with $x$ except at $k$ where it takes value $b$. By induction hypothesis, $\mathfrak{A} \models \psi[(f \circ x)(f b/k)]$, so $\mathfrak{A} \models \exists v_k \psi[f \circ x]$. Conversely, if $\mathfrak{A} \models \exists v_k \psi[f \circ x]$, there exists $c \in A$ with $\mathfrak{A} \models \psi[(f \circ x)(c/k)]$. Taking $b = c$ (which lies in $A \subseteq B$), we have $f b = c$, and by induction hypothesis $\mathfrak{B} \models \psi[x(b/k)]$, so $\mathfrak{B} \models \exists v_k \psi[x]$.

Now if $x \in {}^{\omega}A$, then $f \circ x = x$, so (1) gives $\mathfrak{B} \models \varphi[x]$ iff $\mathfrak{A} \models \varphi[x]$, which means exactly that $\mathfrak{A} \preceq \mathfrak{B}$.
