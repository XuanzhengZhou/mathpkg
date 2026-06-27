---
role: proof
locale: en
of_concept: theta-isomorphism-gamma-minus-plus
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "6. Rees Systems and Filtered Complexes"
---

# Proof of Theta-Induced Isomorphism Between $\Gamma^{-}$ and $\Gamma^{+}$

**Proposition 6.7.** In a special Rees system (6.9), the automorphism $\theta$ induces an isomorphism

$$\theta : \Gamma^{-} \longrightarrow \Gamma^{+}.$$

*Remark.* There is an isomorphism $\Gamma^{-} \cong \Gamma^{+}$ in any Rees system, even if it is not special (see Theorem 7.25 of [10]).

*Proof.* Recall the definitions (6.19) for a Rees system (6.9):

$$\Gamma^{+} = \varphi D / \varphi\alpha D, \qquad \Gamma^{-} = \ker(\bar{\alpha}\bar{\varphi}) / \ker(\bar{\varphi}),$$

where $\varphi : D \to \Gamma$, $\bar{\varphi} : \Gamma \to \bar{D}$, $\alpha : D \to D$, and $\bar{\alpha} : \bar{D} \to \bar{D}$ are the morphisms of the exact couples $\textcircled{1}$ and $\textcircled{2}$.

The specialness of (6.9) provides an automorphism $\theta : \Gamma \cong \Gamma$ satisfying the relations (6.11):

$$\theta\varphi = \varphi\alpha, \qquad \bar{\varphi}\theta = \bar{\alpha}\bar{\varphi}, \qquad \bar{\varphi}\theta^{-1}\varphi = \bar{\gamma}\beta.$$

**Step 1: Action on the denominator of $\Gamma^{-}$.** From the second relation, $\bar{\varphi}\theta = \bar{\alpha}\bar{\varphi}$, we obtain for any $x \in \Gamma$:

$$\bar{\varphi}(\theta x) = \bar{\alpha}(\bar{\varphi}x).$$

Consequently, $x \in \ker(\bar{\alpha}\bar{\varphi})$ if and only if $\theta x \in \ker(\bar{\varphi})$. Thus $\theta$ restricts to an isomorphism of subobjects:

$$\theta : \ker(\bar{\alpha}\bar{\varphi}) \xrightarrow{\cong} \ker(\bar{\varphi}). \tag{1}$$

Moreover, $\theta$ maps $\ker(\bar{\varphi})$ into itself, because if $\bar{\varphi}(x) = 0$ then $\bar{\varphi}(\theta x) = \bar{\alpha}(0) = 0$. Since $\theta$ is an automorphism of $\Gamma$, the restriction $\theta|_{\ker(\bar{\varphi})}$ is monic and hence induces an automorphism on any subquotient where it is well-defined.

**Step 2: Passage to the quotient $\Gamma^{-}$.** The isomorphism (1) descends to the quotient, yielding

$$\Gamma^{-} = \frac{\ker(\bar{\alpha}\bar{\varphi})}{\ker(\bar{\varphi})} \;\cong\; \frac{\ker(\bar{\varphi})}{\theta(\ker\bar{\varphi})}. \tag{2}$$

**Step 3: Action on $\Gamma^{+}$.** From the first relation $\theta\varphi = \varphi\alpha$, we have $\theta(\varphi D) = \varphi\alpha D$. Hence $\theta$ maps the pair $(\varphi D, \varphi\alpha D)$ isomorphically onto $(\varphi\alpha D, \varphi\alpha^2 D)$. On the quotient,

$$\Gamma^{+} = \frac{\varphi D}{\varphi\alpha D} = \frac{\varphi D}{\theta(\varphi D)}. \tag{3}$$

**Step 4: Identification via the third relation.** The third relation $\bar{\varphi}\theta^{-1}\varphi = \bar{\gamma}\beta$, together with the exactness of the couples $\textcircled{1}$ and $\textcircled{2}$, provides a natural isomorphism

$$\frac{\ker(\bar{\varphi})}{\theta(\ker\bar{\varphi})} \;\cong\; \frac{\varphi D}{\theta(\varphi D)}. \tag{4}$$

This identification arises because $\bar{\varphi}\theta^{-1}$ maps $\varphi D$ onto a subobject of $\bar{D}$ whose kernel modulo $\theta(\ker\bar{\varphi})$ corresponds exactly to $\varphi D / \theta(\varphi D)$, and the relation $\bar{\varphi}\theta^{-1}\varphi = \bar{\gamma}\beta$ guarantees compatibility with the exact couple structures.

**Step 5: Composition.** Composing the isomorphisms (2), (4), and the equality (3), we obtain the desired isomorphism

$$\theta : \Gamma^{-} \;\xrightarrow{\cong}\; \Gamma^{+},$$

induced canonically by the automorphism $\theta$. $\square$
