---
role: proof
locale: en
of_concept: proposition-3-2-
source_book: gtm001
source_chapter: "3"
source_section: ""
---

(1) $(\forall x)[x \in a \leftrightarrow x \in a]$.
(2) $(\forall x)[x \in a \leftrightarrow x \in b] \rightarrow (\forall x)[x \in b \leftrightarrow x \in a]$.
(3) $(\forall x)[x \in a \leftrightarrow x \in b] \wedge (\forall x)[x \in b \leftrightarrow x \in c] \rightarrow (\forall x)[x \in a \leftrightarrow x \in c]$.

Remark. Our intuitive idea of equality is of course identity. A basic property that we expect of equality is that paraphrased as “equals may be substituted for equals,” that is, if $a = b$ then anything that can be asserted of $a$ can also be asserted of $b$. In particular if a certain wff holds for $a$ it must also hold for $b$ and vice versa:

$$a = b \rightarrow [\varphi(a) \leftrightarrow \varphi(b)]$$

Here $\varphi(b)$ is the formula obtained from $\varphi$ by replacing each occurrence of some free variable by $b$, and $\varphi(a)$ is the formula obtained from $\varphi$ by replacing each occurrence of the same free variable by $a$.

We need not postulate such a substitution principle for, as we will now show, it can be deduced from Definition 3.1 and the following weaker principle.
