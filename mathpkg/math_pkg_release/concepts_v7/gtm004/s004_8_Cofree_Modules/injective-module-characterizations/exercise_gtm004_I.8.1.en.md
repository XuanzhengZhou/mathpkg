---
role: exercise
locale: en
chapter: "I. Modules"
section: "8. Cofree Modules"
exercise_number: 1
---

# Exercise 8.1

Complete the proof of Theorem 8.4.

Theorem 8.4 states that for a $\Lambda$-module $I$ the following are equivalent:

1. $I$ is injective;
2. For every exact sequence $A \xrightarrow{\mu} B \xrightarrow{\varepsilon} C$ of $\Lambda$-modules the induced sequence
   $$0 \rightarrow \operatorname{Hom}_{\Lambda}(C, I) \xrightarrow{\varepsilon^*} \operatorname{Hom}_{\Lambda}(B, I) \xrightarrow{\mu^*} \operatorname{Hom}_{\Lambda}(A, I) \rightarrow 0$$
   is exact;
3. If $\mu : I \rightarrow B$ is a monomorphism, then there exists $\beta : B \rightarrow I$ such that $\beta \mu = 1_I$;
4. $I$ is a direct summand in every module which contains $I$ as a submodule;
5. $I$ is a direct summand in a cofree module.

Fill in the details of the dualization of Theorem 4.7. In particular, provide the proof of the implication (3) $\Rightarrow$ (4) by establishing the dual of Lemma 4.6.
