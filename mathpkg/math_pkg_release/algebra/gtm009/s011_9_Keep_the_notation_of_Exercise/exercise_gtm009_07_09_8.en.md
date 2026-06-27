---
role: exercise
locale: en
chapter: "7"
section: "9"
exercise_number: 8
---
Fix $\lambda \in \Lambda^+$. Then a minimal admissible lattice $M_{\min}$ in $V(\lambda)$ has a $Z$-basis $(v_0, \ldots, v_\lambda)$ for which the formulas in Lemma 7.2 are valid:

$$h.v_i = (\lambda - 2i)v_i,$$
$$y.v_i = (i + 1)v_{i+1} \quad (v_{\lambda+1} = 0),$$
$$x.v_i = (\lambda - i + 1)v_{i-1} \quad (v_{-1} = 0).$$

Show that the corresponding maximal admissible lattice $M_{\max}$ has a $Z$-basis $(w_0, \ldots, w_\lambda)$ with $w_0 = v_0$ and action given by:

$$h.w_i = (\lambda - 2i)w_i,$$
$$y.w_i = (\lambda - i)w_{i+1},$$
$$x.w_i = iw_{i-1}.$$

Deduce that $v_i = \binom{\lambda}{i}w_i$. Therefore, $[M_{\max} : M_{\min}] = \prod_{i=0}^{\lambda} \binom{\lambda}{i}$.
