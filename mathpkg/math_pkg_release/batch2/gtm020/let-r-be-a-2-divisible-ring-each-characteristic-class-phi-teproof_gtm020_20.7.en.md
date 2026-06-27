---
role: proof
locale: en
of_concept: let-r-be-a-2-divisible-ring-each-characteristic-class-phi-te
source_book: gtm020
source_chapter: "20. General Theory of Characteristic Classes"
source_section: "7"
---

Proof. The construction of $a$ and $m$ proceeds as in paragraph 1 of the proof of (4.3) and the monomorphic character of $a$ and $m$ as semigroup morphisms as in paragraphs 2 and 3.

Let $\eta$ be the oriented 4-plane bundle over $CP^n \times CP^n$ which is the Whitney sum $\eta_1 \oplus \eta_2$, where $\eta_i = pr_i^*(\varepsilon_0(\gamma))$ for $i = 1, 2$. Observe that $\varepsilon_0(\gamma) = \gamma_2^+$ over $CP^n = G_2^+(R^{2n+2})$. Then $H^*(CP^n \times CP^n, R)$ is the polynomial ring $R[x, y]$ modulo the relations $x^{n+1} = 0$ and $y^{n+1} = 0$. Then we have $a(\phi)(x) + a(\phi)(y) = \phi(\eta_1 \oplus \eta_2) = \phi(\eta_1^* \oplus \eta_2^*) = a(\phi)(-x) + a(\phi)(-y)$ and $m(\phi)(x)m(\phi)(y) = \phi(\eta_1 \oplus \eta_2) = \phi(\eta_1^* \oplus \eta_2^*) = m(\phi)(-x)m(\phi)(-y)$ since reversing the orientation of both $\eta_1$ and $\eta_2$ leaves the orientation of $\eta_1 \oplus \eta_2$ unchanged. By writing a power series $f(t) = g_1(t^2) + tg_2(t^2)$, we see that $a(\phi)(t) \in R^+[[t]]$ and $m(\phi)(t) \in R

8. Examples and Applications

8.1 Example. Under the bijection $m: [\text{Vect}(-), H^{\text{ev}}(-, \mathbf{Z})]_{+, \times} \rightarrow \mathbf{Z}[[t]]$, the total Chern class corresponds to $1 + t$, and under bijection $m: [\text{Vect}_R(-), H^*(-, Z_2)]_{+, \times} \rightarrow Z_2[[t]]$, the total Stietel-Whitney class corresponds to $1 + t$. The top Chern class and top Stiefel-Whitney class correspond to $t$ in each of the respective cases. The above statements are clearly true for line bundles, and therefore they are true in general.
