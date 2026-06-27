---
role: exercise
locale: en
chapter: "VIII"
section: "9"
exercise_number: 4
---

# Exercise 4

Carry out the program outlined in Remark (ii) at the end of the section. That is, given the short exact sequence of groups $N \hookrightarrow K \twoheadrightarrow Q$, construct the homology Lyndon--Hochschild--Serre spectral sequence by applying the left derived functor version of the Grothendieck spectral sequence. Define the functors

$$F(A) = \mathbb{Z} \otimes_N A, \quad G(B) = \mathbb{Z} \otimes_Q B,$$

so that $GF(A) = \mathbb{Z} \otimes_K A$. Prove that $F$ preserves projectives (since $F$ is left adjoint to $\bar{F}$, which preserves epimorphisms), and deduce a spectral sequence

$$E^1_{p,q} = H_p(Q, H_{q-p}(N, A)) \Rightarrow H_q(K, A),$$

which converges finitely to the graded object associated with $\{H_q(K, A)\}$, suitably filtered.
