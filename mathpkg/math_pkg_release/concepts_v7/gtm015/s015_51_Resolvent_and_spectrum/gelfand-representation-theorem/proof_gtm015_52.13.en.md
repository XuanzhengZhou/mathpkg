---
role: proof
locale: en
of_concept: gelfand-representation-theorem
source_book: gtm015
source_chapter: "52"
source_section: "52.13"
---

# Proof of Gelfand Representation Theorem

(52.13) Theorem. (Gel'fand representation theorem) Let $A$ be a Gel'fand algebra and let $\mathcal{M}$ be the maximal ideal space of $A$ (52.10).

(i) The mapping $x \mapsto \hat{x}$ ($x \in A$) described in (52.11) is an algebra homomorphism $A \rightarrow \mathbb{C}(\mathcal{M})$ such that $\hat{1}$ is the constant function 1;

(ii) for each $x \in A$, the range of the function $\hat{x}$ is $\sigma(x)$;

(iii) $\|\hat{x}\|_\infty = r(x) \leq \|x\|$ for all $x \in A$, thus the mapping $x \mapsto \hat{x}$ is continuous (with norm 1);

(iv) the kernel of the homomorphism $x \mapsto \hat{x}$ is the intersection of all the maximal ideas of $A$; it is also the set of all $x \in A$ such that $\sigma(x) = \{0\}$.

The mapping $

therefore $x$ is invertible in $A$. Then $1 = (xx^{-1})^2 = \hat{x}(x^{-1})^2$, thus $(\hat{x})^{-1} = (x^{-1})^2 \in \hat{A}$.

(vi) This is immediate from (52.12) and the fact that the Gel'fand topology is separated, but it is instructive to prove a little more: $A$ is a 2-fold transitive algebra of functions, in the sense that if $M_1 \neq M_2$ and if $\lambda_1, \lambda_2$ is any specified pair of complex numbers, then there exists $x \in A$ such that $\hat{x}(M_1) = \lambda_1$ and $\hat{x}(M_2) = \lambda_2$. Note that $M_2 \notin M_1$. $\{M_2 \subset M_1$ would imply $M_2 = M_1$ by the maximality of $M_2\}$. Choose $x_1 \in M_2$ with $x_1 \notin M_1$; then $f_{M_2}(x_1) = 0$ and $f_{M_1}(x_1) \neq 0$, thus $\hat{x}_1(M_2) = 0$ and $\hat{x}_1(M_1) \neq 0$. {This, too, settles (vi).} Multiplying $x_1$ by a scalar, we can suppose $\hat{x}_1(M_1) = 1$. Similarly, choose $x_2$ so that $\hat{x}_2(M_1) = 0$ and $\hat{x}_2(M_2) = 1$. The element $x = \lambda_1 x_1 + \lambda_2 x_2$ meets the requirements. {Better yet, see (52.15).}
