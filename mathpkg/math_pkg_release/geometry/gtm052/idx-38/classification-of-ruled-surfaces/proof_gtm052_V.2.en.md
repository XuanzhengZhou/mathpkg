---
role: proof
locale: en
of_concept: classification-of-ruled-surfaces
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

(a) If $\mathcal{E}$ is decomposable, then $\mathcal{E} \cong \mathcal{L}_1 \oplus \mathcal{L}_2$ for two invertible sheaves $\mathcal{L}_1$ and $\mathcal{L}_2$ on $C$. We must have $\deg \mathcal{L}_i \leq 0$ because of the normalization (2.8) and furthermore $H^0(\mathcal{L}_i) \neq 0$ for at least one of them. Thus one of them is $\mathcal{O}_C$, so we have $\mathcal{E} \cong \mathcal{O}_C \oplus \mathcal{L}$ with $\deg \mathcal{L} \leq 0$. From (2.11.1), (2.11.2), and (2.11.3), we see that all values of $e \geq 0$ are possible.

(b) Now suppose $\mathcal{E}$ is indecomposable. Then, corresponding to the section $C_0$, we have an exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{L} \rightarrow 0$$

for some invertible sheaf $\mathcal{L}$ (2.8). This must be a nontrivial extension, so it corresponds to a nonzero element $\xi \in \operatorname{Ext}^1(\mathcal{L}, \mathcal{O}_C) \cong H^1(C, \mathcal{L}^{-1})$. In particular, $H^1(C, \mathcal{L}^{-1}) \neq 0$.

By Serre duality, $H^1(C, \mathcal{L}^{-1}) \cong H^0(C, \mathcal{L} \otimes \omega_C)^\vee$. For this to be nonzero, we need $\deg(\mathcal{L} \otimes \omega_C) \geq 0$, i.e., $\deg \mathcal{L} + (2g - 2) \geq 0$. Since $e = -\deg \mathcal{E} = -\deg \mathcal{L}$ (as $\det \mathcal{E} \cong \mathcal{L}$), we get $e \leq 2g - 2$.

On the other hand, since $\mathcal{E}$ is normalized, we have $H^0(\mathcal{E}) \neq 0$, which gives the inclusion $\mathcal{O}_C \hookrightarrow \mathcal{E}$ in the exact sequence above. The normalization also requires that for any invertible sheaf $\mathcal{M}$ with $\deg \mathcal{M} < 0$, $H^0(\mathcal{E} \otimes \mathcal{M}) = 0$. From the exact sequence

$$0 \rightarrow \mathcal{M} \rightarrow \mathcal{E} \otimes \mathcal{M} \rightarrow \mathcal{L} \otimes \mathcal{M} \rightarrow 0,$$

if $\deg \mathcal{M}$ were very negative such that $H^0(\mathcal{M}) = 0$ but $H^0(\mathcal{L} \otimes \mathcal{M}) \neq 0$, then $H^0(\mathcal{E} \otimes \mathcal{M})$ could be nonzero. Applying this reasoning with $\mathcal{M} = \omega_C^{-1}$ and using Clifford's theorem or the Riemann-Roch theorem gives the lower bound $-2g \leq e$.
