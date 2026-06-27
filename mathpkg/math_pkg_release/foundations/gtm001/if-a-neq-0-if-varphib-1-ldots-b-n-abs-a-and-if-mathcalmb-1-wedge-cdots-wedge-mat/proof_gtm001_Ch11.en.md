---
role: proof
locale: en
of_concept: if-a-neq-0-if-varphib-1-ldots-b-n-abs-a-and-if-mathcalmb-1-wedge-cdots-wedge-mat
source_book: gtm001
source_chapter: "11"
source_section: ""
---

(By induction on $n$). If $n = 1$ then

$$\varphi(B_1) \leftrightarrow (\forall x_1)[x_1 = B_1 \rightarrow \varphi(b_1)]$$

$$\leftrightarrow (\exists x_1)[x_1 = B_1 \wedge \varphi(b_1)].$$

If $\varphi(b_1)$ Abs $A$ and $b_1 = B_1$ Abs $A$ then $[b_1 = B_1 \rightarrow \varphi(b_1)]$ Abs $A$ and $[b_1 = B_1 \wedge \varphi(b_1)]$ Abs $A$. Then by Theorem 13.8, $\varphi(B_1)$ Abs $A$.

The induction step is obvious

Then $x \in A$ implies

$$[x \in \{y \mid \varphi(y)\}]^A \leftrightarrow x \in A \wedge \varphi^A(x)$$

$$\leftrightarrow x \in \{y \in A \mid \varphi^A(y)\}$$

$$\leftrightarrow x^A \in \{y \mid \varphi(y)\}^A.$$

(4) $[\{y \mid \varphi(y)\} \in x]^* \leftrightarrow (\exists z) [z \in x \wedge (\forall y) [y \in z \leftrightarrow \varphi(y)]]$.

Hence

$$[\{y \mid \varphi(y)\} \in x]^A \leftrightarrow (\exists z \in A) [z \in x \wedge (\forall y \in A) [y \in z \leftrightarrow \varphi^A(y)]]$$.

Then $A$ transitive and $x \in A$ implies

$$[\{y \mid \varphi(y)\} \in x]^A \leftrightarrow (\exists z \in A) [z \in x \wedge (\forall y \in A) [y \in z \leftrightarrow \varphi^A(y)]]$$

$$\leftrightarrow (\exists z \in A) [z \in x \wedge z = \{y \in A \mid \varphi^A(y)\}]$$

$$\leftrightarrow \{y \in A \mid \varphi^A(y)\} \in x$$

$$\leftrightarrow \{y \mid \varphi(y)\}^A \in x^A.$$

(5) $[\{x \mid \varphi(x)\} \in \{y \mid \psi(y)\}]^*$

$$\leftrightarrow (\exists z) [(\forall x) [x \in z \leftrightarrow \varphi(x)] \wedge z \in \{y \mid \psi(y)\}]$$.

Therefore from (1) and (3)

$$[\{x \mid \varphi(x)\} \in \{y \mid \

If $a_1, \ldots, a_n \in A$ then since $\varphi(x)$ is absolute with respect to $A$

$$x \in \{x \mid \varphi(x)\}^A \leftrightarrow x \in A \land \varphi^A(x)$$

$$\leftrightarrow x \in A \land \varphi(x)$$

$$\leftrightarrow x \in \{x \mid \varphi(x)\} \cap A.$$

Remark. The class $\{x \mid \varphi(x)\}^A$ is the class $\{x \mid \varphi(x)\}$ relativized to $A$. By definition $\{x \mid \varphi(x)\}^A$ is the class of individuals in $A$ for which $\varphi^A(x)$ holds. From Proposition 13.14 we see that if $\varphi(x)$ is absolute with respect to $A$ then $\{x \mid \varphi(x)\}^A$ is simply the class of individuals in $A$ for which $\varphi(x)$ holds.
