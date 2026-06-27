---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

In a hidden Markov model, an underlying Markov chain $P$ on a state space $S$ evolves unseen, and at each step an observable outcome in $Y$ is produced according to a probability matrix $F$. The formula gives the joint probability of a finite sequence of observed outcomes, summing over all possible hidden state trajectories. When each row $F_i$ concentrates its mass on a single entry, this reduces to the lumping of Markov chains; when all entries are strictly positive, the model admits parameter estimation via the Baum-Welch iterative procedure.
