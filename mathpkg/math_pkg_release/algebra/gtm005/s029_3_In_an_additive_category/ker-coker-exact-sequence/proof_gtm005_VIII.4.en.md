---
role: proof
locale: en
of_concept: ker-coker-exact-sequence
source_book: gtm005
source_chapter: "VIII"
source_section: "4"
---

From the morphism of short exact sequences, construct two auxiliary objects: let $d$ be the pullback of $e$ and $k = \ker h$, giving an epi $u : d \twoheadrightarrow \operatorname{Ker} h$ with kernel $s$ (by Proposition 2). Dually, let $d'$ be the pushout of $p = \operatorname{coker} f$ and $m'$, with cokernel $s'$.

Define $\delta_0 = p' g k' : d \rightarrow d'$, where $k'$ is the pullback projection and $p'$ the pushout injection. Observe that $s' \delta_0 = h k u = 0$ and $\delta_0 s = u' p f = 0$. Since $u' = \ker s'$ and $u = \operatorname{coker} s$, the morphism $\delta_0$ factors uniquely as

\[
\delta_0 = u' \delta u : d \xrightarrow{u} \operatorname{Ker} h \xrightarrow{\delta} \operatorname{Coker} f \xrightarrow{u'} d'.
\]

The middle factor is the required connecting morphism $\delta : \operatorname{Ker} h \rightarrow \operatorname{Coker} f$.

To verify exactness at $\operatorname{Ker} h$, use the calculus of members. For $x \in_m \operatorname{Ker} h$ with $\delta x \equiv 0$, since $e$ is epi there exists $y \in_m b$ with $e y \equiv k x$. Then $e' g y \equiv h e y \equiv h k x \equiv 0$, so by exactness of the lower row there exists $z \in_m a'$ with $m' z \equiv g y$. The member $p z \in_m \operatorname{Coker} f$ corresponds to $\delta x$.

If $\delta x \equiv 0$, then $p z \equiv 0$, so $z \equiv f z_2$ for some $z_2 \in_m a$. Then $g m z_2 \equiv g y$. Form the difference member $y_0 = y - m z_2 \in_m b$. By rule (vi), $e y_0 \equiv e y = k x$ and $g y_0 \equiv 0$. Since $j : b_0 \rightarrow b$ is $\ker g$, there exists $x_0 \in_m \operatorname{Ker} g$ with $j x_0 \equiv y_0$. Then $k e_0 x_0 = e j x_0 \equiv e y_0 \equiv k x$, and since $k$ is monic, $e_0 x_0 \equiv x$. This proves that every $x$ with $\delta x \equiv 0$ lies in the image of $e_0$, establishing exactness at $\operatorname{Ker} h$.

The exactness at the other positions is verified similarly using the member calculus. This proof is exactly analogous to the classical element-based proof in $\mathbf{Ab}$, but uses members instead of elements throughout.
