---
role: exercise
locale: en
chapter: "VIII"
section: "5"
exercise_number: 2
---

# Exercise 5.2

Show that Theorem 5.2 and its dual yield all the information about limits and colimits used in the proof of Theorem 5.3.

In particular:

1. Formulate and prove the dual of Theorem 5.2: given a co-tower of pushout squares

   $$
   \begin{CD}
   C_{i-1} @>>> D_{i-1} \\
   @VVV @VVV \\
   C_i @>>> D_i
   \end{CD}
   $$

   for $i \geq 1$, the induced square between the colimits $C_\infty = \operatorname{colim}_i C_i$ and $D_\infty = \operatorname{colim}_i D_i$, together with the colimit structure maps to $C_0$ and $D_0$, is a pushout.

2. Explain how Theorem 5.2 is applied in Step 2 of the proof of Theorem 5.3 to obtain $E_{0,\infty} = \lim_n E_{0,n}$, and how its dual is applied in Step 1 to obtain $E_{m,\infty} = \lim_n E_{m,n}$ (interpreted as a colimit in the appropriate direction of the spectral sequence).

3. Show that the compatibility condition (5.15) needed for the application of Theorem 5.2 follows from the naturality of the $Q^\nu$-construction with respect to the maps $\varrho_n: D_{n+1} \to D_n$.

4. Verify that the limit and colimit processes commute in this special case by applying Theorem 5.1 (interchange of limits) to the bigraded object $\{E_{m,n}\}$.
