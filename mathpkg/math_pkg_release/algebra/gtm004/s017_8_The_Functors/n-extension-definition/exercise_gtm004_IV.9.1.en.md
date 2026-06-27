---
role: exercise
locale: en
chapter: "IV"
section: "9. Ext^n and n-Extensions"
exercise_number: 1
---

# Exercise 9.1

Give the detailed proof that $\operatorname{Yext}_A^n(-, -)$ is a bifunctor for $n \geq 2$.

That is, given an $n$-extension

$$E : 0 \longrightarrow B \longrightarrow E_n \longrightarrow \cdots \longrightarrow E_1 \longrightarrow A \longrightarrow 0$$

and a homomorphism $\alpha : A' \rightarrow A$, construct the pull-back $n$-extension $E^\alpha$ ending in $A'$; and given a homomorphism $\beta : B \rightarrow B'$, construct the push-out $n$-extension $E_\beta$ starting from $B'$. Then show that these constructions induce well-defined maps on equivalence classes and satisfy the bifunctor axioms:

$$\alpha^*[E] = [E^\alpha], \qquad \beta_*[E] = [E_\beta].$$

Prove that $(\alpha_1 \alpha_2)^* = \alpha_2^* \alpha_1^*$ and $(\beta_1 \beta_2)_* = \beta_{1*} \beta_{2*}$.
