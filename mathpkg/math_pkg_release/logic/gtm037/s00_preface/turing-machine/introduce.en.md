---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A Turing machine is a formal mathematical model of computation, introduced to give a rigorous definition of effective procedure. It consists of finitely many internal states, a reading head, and a two-way infinite tape divided into squares each containing either $0$ or $1$. The machine's behavior is completely specified by a finite matrix of state-symbol-action-next-state quadruples. At each step, the machine reads the symbol on the scanned square, consults the matrix row matching its current state and the read symbol, performs the indicated action (write 0, write 1, move left, move right, or stop), and transitions to the next state. This definition forms the foundation for the theory of Turing computability developed in subsequent chapters.
