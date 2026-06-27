---
role: proof
locale: en
of_concept: if-there-exists-a-set-that-is-a-standard-model-of-zf-then-there-exists-one-and-o
source_book: gtm001
source_chapter: "17"
source_section: ""
---

From Mostowski’s theorem (Theorem 12.8) every standard model is $\in$-isomorphic to a standard transitive model. Therefore the existence of a set that is a standard model of ZF implies the existence of a set that is a standard transitive model. For transitive models the property of being an ordinal is absolute. That is, those sets in a transitive model that play the role of ordinals are ordinals. Furthermore, from transitivity, if $\alpha$ is in the model, then all smaller ordinals are in the model. But a standard transitive model that is a set cannot contain all ordinals.

If $\alpha$ is the smallest ordinal not contained in such a model then $\alpha$ is the class of ordinals for that model. But the existence of such an ordinal implies the existence of a smallest such ordinal, $\alpha_0$, that is the set of all ordinals in some standard transitive model $N_0$.

Since $N_0$ is a model of ZF it follows that if

$$M_0 \triangleq L^{N_0} = \{x | (\exists \alpha \in N_0) [x = F' \alpha]\} = \{F' \alpha | \alpha < \alpha_0\}$$

then $M_0$ is a model of ZF + V = L.

If $N$ is any standard transitive model of ZF then $N$ is closed w.r.t. the fundamental operations. Therefore since $\alpha_0 \subseteq N$ it follows that $M_0 \subseteq N$. From this we see that $M_0$ is unique, for if $M_0$ and $M'$ are each standard transitive models with the prescribed properties then

$$M_0 \subseteq M' \quad \text{and} \quad M' \subseteq M_0.$$

Finally, from the Lowenheim–Skolem theorem, $M_0$ contains a countable standard submodel. But this submodel must be $\in$-isomorphic to a countable standard transitive model that must contain $M_0$ as a submodel. Hence $M_0$ is countable.

Remark. The unique model $M_0$ described in Theorem 1

is a model of $ZF + V \neq L$. It then follows that this theorem relativized to $M_0$ is also a theorem. That is

$$\{x \in M_0 | \varphi^{M_0}(x)\}$$

is a submodel of $M_0$ that is also a model of $ZF + V \neq L$. Since $M_0$ is a model of $V = L$ this submodel is a proper submodel of $M_0$. But such a submodel of $M_0$ must be isomorphic to a standard transitive proper submodel of $M_0$ that must in turn contain $M_0$ as a submodel. This is impossible.

The independence of $V = L$ must then be established by some method other than that of internal models. Cohen’s approach is to extend the minimal model $M_0$ in the following way. Since $M_0$ is countable and $\mathcal{P}(\omega)$ is not countable, there exists a set $a$ such that $a \subseteq \omega$ and $a \notin M_0$. We adjoin such a set $a$ to $M_0$ to obtain $M_0 \cup \{a\}$ and we define $M_0[a]$ to be the result of closing $M_0 \cup \{a\}$ under the eight fundamental operations. Can we select a set $a$ so that $M_0[a]$ is a model of $ZF$? We will show that we can. Moreover we will show that $a$ can be selected so that the ordinals in $M_0[a]$ are precisely the ordinals in $M_0$. It then follows that

$$L^{M_0[a]} = \{x | (\exists \alpha \in M_0)[x = F' \alpha]\} = M_0.$$

This tells us that in the universe $M_0[a]$ the class of constructible sets is $M_0$. Since $a \in M_0[a]$ but $a \notin M_0$ it follows that $a$ is not constructible relative to the universe $M_0[a]$. That is, $M_0[a]$ is a model of $
