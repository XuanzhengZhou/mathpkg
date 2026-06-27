---
role: proof
locale: en
of_concept: mostowski-collapse
source_book: gtm053
source_chapter: "I"
source_section: "7"
---

The proof constructs $M$ and $f$ by transfinite induction on the ordinals.

**(a) Base case.** Set $N_0 = \{X \in N \mid [X] = \varnothing\}$, i.e., those $X$ for which there is no $Y$ with $Y \varepsilon X$. By the axiom of the empty set being $\phi$-true, $N_0$ contains the empty set interpretation. Define $M_0 = \{\varnothing\}$ and $f_0: N_0 \to M_0$ by $f_0(X) = \varnothing$. This is well-defined since all elements of $N_0$ have empty $[X]$.

**(b) Successor step.** Suppose $N_\alpha$, $M_\alpha$, and $f_\alpha: N_\alpha \to M_\alpha$ have been defined such that $f_\alpha$ is an isomorphism of $(N_\alpha, \varepsilon)$ with $(M_\alpha, \in)$. Define

$$N_{\alpha+1} = \{X \in N \mid [X] \subset N_\alpha\},$$

i.e., those $X$ whose $\varepsilon$-elements all lie in $N_\alpha$. For $X \in N_{\alpha+1} \setminus N_\alpha$, define

$$f_{\alpha+1}(X) = \{f_\alpha(Y) \mid Y \in [X]\}.$$

For $X \in N_\alpha$, set $f_{\alpha+1}(X) = f_\alpha(X)$. Set $M_{\alpha+1} = f_{\alpha+1}(N_{\alpha+1})$.

**(c) Limit step.** If $\beta$ is a limiting ordinal, set $N_\beta = \bigcup_{\alpha < \beta} N_\alpha$, $M_\beta = \bigcup_{\alpha < \beta} M_\alpha$, and $f_\beta = \bigcup_{\alpha < \beta} f_\alpha$.

**(d) Conclusion.** Set $M = \bigcup_\alpha M_\alpha$ and $f = \bigcup_\alpha f_\alpha$, where the union is taken over all ordinals.

**Verification.** By induction on $\alpha$:

(c1) $N_\alpha$ is a set, i.e., $N_\alpha \in V$. This holds since $[ \cdot ]$ is a function from $N_{\alpha+1} \setminus N_\alpha$ to $\mathcal{P}(N_\alpha)$, and since the axiom of extensionality is $\phi$-true, this function has an inverse, so $N_{\alpha+1} \setminus N_\alpha$ is a set.

(c2) $M_\alpha$ is a transitive subset of $V$. Elements of $M_{\alpha+1} \setminus M_\alpha$ have the form $\{f_\alpha(Y) \mid Y \in [X]\}$ where $X \in N_{\alpha+1} \setminus N_\alpha$, and since $[X] \subset N_\alpha$, any element of such a set belongs to $f_\alpha(N_\alpha) = M_\alpha$, establishing transitivity.

(c3) $f_\alpha$ is an isomorphism of $(N_\alpha, \varepsilon)$ with $(M_\alpha, \in)$. This follows from the construction and the fact that the axiom of extensionality guarantees $f_{\alpha+1}$ is injective on the new elements.

(c4) $N = \bigcup_\alpha N_\alpha$, which follows from the well-foundedness of the relation (implicitly assumed for the construction to exhaust $N$).

Thus $f: N \to M$ is the required isomorphism onto a transitive class.
