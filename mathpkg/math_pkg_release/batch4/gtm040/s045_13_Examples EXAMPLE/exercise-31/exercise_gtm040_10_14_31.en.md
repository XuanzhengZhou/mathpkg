---
role: exercise
locale: en
chapter: "10"
section: "14"
exercise_number: 31
---

Let

$${}_j P_{ik}^{(n)} = \Pr{}_i[x_n = k \land x_m \neq j \text{ if } 0 \leq m < n]$$

be the probability that the process goes from $i$ to $k$ in $n$ steps without visiting $j$ at any intermediate time. Show that

$${}_k L_{ij} = \sum_{r=k}^{\infty} \sum_{n=0}^{\infty} {}_j P_{ir}^{(n)} P_{rj},$$

and derive as a consequence that

$${}_k L_{ij} \leq N_{ij} - \sum_{r=0}^{k-1} N_{ir} P_{rj}.$$
