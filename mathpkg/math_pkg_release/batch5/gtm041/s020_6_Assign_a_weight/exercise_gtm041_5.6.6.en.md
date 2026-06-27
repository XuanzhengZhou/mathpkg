---
role: exercise
locale: en
chapter: "5"
section: "6"
exercise_number: 6
---

Assign a weight $f(x, y)$ to each lattice point $(x, y)$ and let $S_n$ be the sum of all the weights in $T_n$,

$$S_n = \sum_{(x, y) \in T_n} f(x, y).$$

(a) By comparing the regions $T_r$ and $T_{r-1}$ for $r \geq 2$ show that

$$S_r - S_{r-1} = f(r, r) + \sum_{k=1}^{r-1} \{f(k, r) + f(r, k)\} - \sum_{k=1}^{r-1} f(k, r-k),$$

and deduce that

$$S_n = \sum_{r=1}^{n} f(r, r) + \sum_{r=2}^{n} \sum_{k=1}^{r-1} \{f(k, r) + f(r, k)\} - \sum_{r=2}^{n} \sum_{k=1}^{r-1} f(k, r-k).$$

Note: If $f(x, y) = 0$ whenever $(x, y) > 1$ this reduces to a formula of J. Lehner and M. Newman [25],

$$\sum_{(x, y) \in T_n'} f(x, y) = f(1, 1) + \sum_{r=2}^{n} \sum_{k=1}^{r-1} \{f(k, r) + f(r, k) - f(k, r-k)\}.$$

This relates a sum involving Farey fractions to one which does not.
