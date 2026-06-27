---
role: proof
locale: en
of_concept: left-regular-representation-faithful
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of Left regular representation of L^1(G) is a faithful star-representation

Proof. In view of the lemma, the only point remaining to be settled is that $T_{\tilde{u}} = (T_u)^*$.

Let $u \in L^1(G)$ and $v_1, v_2 \in L^2(G)$. Say $u = [f]$, $v_1 = [g_1]$, $v_2 = [g_2]$. From the properties of the modular function $\Delta$, we have

$$\left(T_{\tilde{u}} v_1 | v_2\right) = \left(\tilde{u} v_1 | v_2\right)$$

$$= \int \left(\int \tilde{f}(st) g_1(t^{-1}) dt\right) g_2(s)^* ds$$

$$= \iint \Delta(st) f(t^{-1} s^{-1})^* g_1(t^{-1}) g_2(s)^* dt ds$$

$$= \int \Delta(s) \left(\int \Delta(t) f(t^{-1} s^{-1})^* g_1(t^{-1}) dt\right) g_2(s)^* ds$$

$$= \int \Delta(s) \left(\int f(ts^{-1})^* g_1(t) dt\right) g_2(s^{-1})^* ds$$

$$= \iint f(ts)^* g_1(t) g_2(s^{-1})^* dt ds,$$

whereas

$$\left(T_u^* v_1 | v_2\right) = \left(v_1 | T_u v_2\right) = \left(v_1 | u v_2\right)$$

$$= \int g_1(t) \left(\int f(ts) g_2(s^{-1}) ds\right)^* dt$$

$$= \iint g_1(t) f(ts)^* g_2(s^{-1})^* ds dt,$$

thus $(T_{\tilde{u}} v_1 | v_2) = (T_u^* v_1 | v_2)$ by Fubini's theorem, establishing $T_{\tilde{u}} = (T_u)^*$.

The faithfulness follows from the fact that if $T_u = 0$, then $u * g = 0$ for all $g \in L^2(G)$ with compact support; by the approximate identity argument (69.13)-(69.14), this forces $u = 0$.
