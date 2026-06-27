---
role: proof
locale: en
of_concept: extension-of-set-map-to-homomorphism
source_book: gtm023
source_chapter: "5"
source_section: "§1. Basic properties"
---

It is clear that the condition is necessary. Conversely, assume that the condition is satisfied. Then define a mapping $\varphi: A \to B$ by

$$
\varphi \sum_{(v)} \xi^{v_1 \dots v_p} x_{v_1} \dots x_{v_p} = \sum_{(v)} \xi^{v_1 \dots v_p} \varphi_0 x_{v_1} \dots \varphi_0 x_{v_p}, \quad x_{v_i} \in S.
$$

To show that $\varphi$ is well defined, notice that if

$$
\sum_{(v)} \xi^{v_1 \dots v_p} x_{v_1} \dots x_{v_p} = \sum_{(u)} \eta^{\mu_1 \dots \mu_q} y_{\mu_1} \dots y_{\mu_q}
$$

then

$$
\sum_{(v)} \xi^{v_1 \dots v_p} x_{v_1} \dots x_{v_p} - \sum_{(u)} \eta^{\mu_1 \dots \mu_q} y_{\mu_1} \dots y_{\mu_q} = 0.
$$

In view of the assumed condition,

$$
\sum_{(v)} \xi^{v_1 \dots v_p} \varphi_0 x_{v_1} \dots \varphi_0 x_{v_p} - \sum_{(u)} \eta^{\mu_1 \dots \mu_q} \varphi_0 y_{\mu_1} \dots \varphi_0 y_{\mu_q} = 0,
$$

which shows that $\varphi$ is well defined. It follows directly from the definition that $\varphi$ is a homomorphism extending $\varphi_0$.
