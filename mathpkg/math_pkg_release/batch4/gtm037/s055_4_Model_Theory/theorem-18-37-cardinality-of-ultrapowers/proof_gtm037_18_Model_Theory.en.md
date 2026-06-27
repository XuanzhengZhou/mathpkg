---
role: proof
locale: en
of_concept: theorem-18-37-cardinality-of-ultrapowers
source_book: gtm037
source_chapter: "18"
source_section: "Model Theory"
---

By Definition 18.34 choose $E \subseteq F$ so that $|E| = |I|$ and $\bigcap G = \varnothing$ whenever $G \subseteq E$ and $G$ is infinite.

For each $i \in I$ let $H_i = \{a \in E : i \in a\}$. Thus by our choice of $E$, $H_i$ cannot be infinite; hence we can choose a one-one function $f_i$ mapping $\mathcal{P}(H_i) = \{z : z \subseteq H_i\}$ into $A$.

Now for each $X \subseteq E$ we define a function $g_X : I \to A$ by setting $g_X(i) = f_i(X \cap H_i)$. We claim that if $X \neq Y$, then $[g_X] \neq [g_Y]$ in the ultrapower.

Indeed, if $X \neq Y$, then there exists some $a \in E$ such that $a \in X \triangle Y$ (symmetric difference). Without loss of generality, assume $a \in X \setminus Y$. Then for every $i \in a$, we have $a \in H_i$ (since $i \in a$ and $a \in E$), so $a \in X \cap H_i$ but $a \notin Y \cap H_i$. Hence $X \cap H_i \neq Y \cap H_i$, and since $f_i$ is one-one, $g_X(i) \neq g_Y(i)$ for all $i \in a$. Since $a \in E \subseteq F$, the set $\{i \in I : g_X(i) \neq g_Y(i)\}$ contains $a$ and thus belongs to $F$. Therefore $[g_X] \neq [g_Y]$.

Since there are $2^{|E|} = 2^{|I|}$ distinct subsets $X \subseteq E$, we obtain $2^{|I|}$ distinct elements in $^I A / F$, proving the result.
