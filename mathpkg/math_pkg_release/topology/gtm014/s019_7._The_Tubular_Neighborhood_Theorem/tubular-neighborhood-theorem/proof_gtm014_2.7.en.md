---
role: proof
locale: en
of_concept: tubular-neighborhood-theorem
source_book: gtm014
source_chapter: "2"
source_section: "7"
---

*Proof.* Using the Whitney Embedding Theorem (Proposition 5.9), we may assume that $Y \subset \mathbf{R}^p$ for $p = 2 \dim Y + 1$. Thus $X$ is a submanifold of $\mathbf{R}^k$ and by Lemma 7.6 there is a tubular neighborhood of $X$ in $\mathbf{R}^p$ which we call $Z'$.

Let $E_x$ be the set of vectors normal to $X$ and tangent to $Y$ at $x$ for $x \in X$ and let $E = \bigcup_{x \in X} E_x$. Then $E$ is a vector bundle over $X$ since it is the complementary subbundle to $TX$ in $T_X Y$.

As in Lemma 7.6, this explicit construction of $E$ gives a smooth mapping $f: E \to \mathbf{R}^p$ such that $f|_{X_0} = f|_X = \mathrm{id}_X$.

Let $Z''$ be a tubular neighborhood of $Y$ in $\mathbf{R}^p$ with projection map $\pi''$. Then $U = f^{-1}(Z' \cap Z'')$ is an open neighborhood of $X_0$ in $E$.

Consider the smooth mapping $\pi'' \circ f: U \to Y$. Note that $\pi'' \circ f|_X = \mathrm{id}_X$ since $X \subset Y$ and $\pi''|_Y = \mathrm{id}_Y$.

We wish to apply Proposition 7.5 to obtain the desired result. In order to do so we need to know that $d(\pi'' \circ f)_x: T_x E \to T_{f(x)} Y$ is an isomorphism for all $x \in X$.

Since $\dim E = \dim Y$, we need only show that $\operatorname{Ker} d(\pi'' \circ f)_x = \{0\}$. Now $T_x E = T_x X \oplus T_x E_x$. Since $\pi'' \circ f|_X = \mathrm{id}_X$, it remains to prove that if $v \in T_x E_x$ and $d(\pi'' \circ f)_x(v) = 0$, then $v = 0$.

But $f$ maps $E_x$ diffeomorphically onto the normal space to $X$ at $x$ in $\mathbf{R}^p$, and $\pi''$ projects along the normal directions of $Y$. Since $E_x$ consists of vectors tangent to $Y$ but normal to $X$, the composition $\pi'' \circ f$ restricted to $E_x$ is an isomorphism onto the normal bundle of $X$ in $Y$. Therefore the kernel condition forces $v = 0$.

Hence $d(\pi'' \circ f)_x$ is an isomorphism for all $x \in X$. By Proposition 7.5, there exists an open neighborhood $V$ of $X$ in $U \subset E$ such that $\pi'' \circ f|_V$ is a diffeomorphism onto a tubular neighborhood of $X$ in $Y$. This completes the proof. ∎
