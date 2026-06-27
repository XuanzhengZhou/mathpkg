---
role: exercise
locale: en
chapter: "8"
section: "2"
exercise_number: "8.54"
---

We work with a sentential logic in which negation and disjunction are taken as primitive. We describe a definition of "$\vdash \varphi$" in which rules of inference rather than axioms take precedence. We define four rules of inference.

(1) **Association.** This rule is a relation $R_0 \subseteq \text{Sent} \times \text{Sent}$. If $\varphi$ is a sentence, $(\psi \vee \chi) \vee \theta$ is a consecutive part of $\varphi$, with $\psi, \chi, \theta \in \text{Sent}$ (i.e., $\varphi = \theta'((\psi \vee \chi) \vee \theta)\theta''$ for some expressions $\theta', \theta''$), and if $\sigma$ is obtained from $\varphi$ by replacing a consecutive part of $\varphi$ of this sort by $\psi \vee (\chi \vee \theta)$ (i.e., if $\sigma = \theta'(\psi \vee (\chi \vee \theta))\theta''$ with notation as before), then $(\varphi, \sigma) \in R_0$.

(2) **Commutation.** We define $R_1 \subseteq \text{Sent} \times \text{Sent}$. If $\varphi$ is a sentence, $\psi \vee \chi$ is a consecutive part of $\varphi$, with $\psi, \chi \in \text{Sent}$, and $\sigma$ is obtained from $\varphi$ by replacing a consecutive part of $\varphi$ of this sort by $\chi \vee \psi$, then $(\varphi, \sigma) \in R_1$.

(3) **Double negation.** $R_2$ consists of all pairs of the following sort, where $\psi, \chi, \theta \in \text{Sent}$: $((\psi \vee \chi) \vee \theta, (\psi \vee \neg\neg\chi) \vee \theta)$; $(\chi \vee \theta, \neg\neg\chi \vee \theta)$; $(\psi \vee \chi, \psi \vee \neg\neg\chi)$; $(\chi, \neg\neg\chi)$.

(4) **Conjunction.** $R_3$ consists of all triples of [appropriate form for conjunction introduction/elimination].
