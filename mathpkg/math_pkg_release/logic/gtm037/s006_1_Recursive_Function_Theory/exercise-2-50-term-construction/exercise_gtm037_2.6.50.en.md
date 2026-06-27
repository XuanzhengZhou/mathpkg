---
role: exercise
locale: en
chapter: "2"
section: "2.6"
exercise_number: 50
---

For the set $A$ of Lemma 2.44, for each $f \in A$ introduce a symbol $R_f$. Allow, in addition, variables $v_0, v_1, v_2, \ldots$. We define term: any variable standing alone is a term. If $f \in A$, $f$ is $m$-ary ($m > 0$), and $\sigma_0, \ldots, \sigma_{m-1}$ are terms, then so is $R_f \sigma_0, \ldots, \sigma_{m-1}$. These are all the terms.

Let $i$ be such that all the variables appearing in a certain term $\tau$ are in the list $v_0, \ldots, v_i$. Define $g_{\tau}^i$:

$$g_{\tau}^i(v_0, \ldots, v_i) = \tau$$

for all $v_0, \ldots, v_i \in \omega$, where each $R_f$ occurring in $\tau$ is interpreted as $f$. Show that $g_{\tau} \in A$. [Try induction on how $\tau$ is built up.]
