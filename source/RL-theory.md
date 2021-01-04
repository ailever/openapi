# Reinforcement Learning

***

## Markov Reward Process (MRP) 
$$<\mathcal{S}, \mathcal{P}, \mathcal{R}>$$
- $\mathcal{S}$ is a set of states.
- $\mathcal{P}$ is the probability that state $s$ at time $t$ will lead to state $s'$ at time $t+1$.
- $\mathcal{R}$ is expected immediate reward.


### Bellman Expectation Equation
$$
\begin{aligned}
   V(s)&=\mathbb{E}(G_{t}|S_{t}=s) \\
   &=\mathbb{E}(R_{t+1} + \gamma V(S_{t+1})|S_{t}=s) \\
   &=R(s) + \gamma \sum_{s'\in S_{t+1}} P_{SS'}V(s') \\
\end{aligned}
$$
$$ *\quad G_{t}=\sum_{\tau=t}^{\infin} \gamma^{\tau-t}R_{\tau+1} $$
$$ *\quad P_{SS'}=P[S_{t+1}=s'|S_{t}=s]$$

- Matrix Representaion

$$
\begin{aligned}
   V&=R + \gamma Pv  \\
   &=(I - \gamma P)^{-1}R 
\end{aligned}
$$

***

## Markov Decision Process (MRP)
$$<\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}>$$
- $\mathcal{S}$ is a set of states.
- $\mathcal{A}$ is a set of actions.
- $\mathcal{P}$ is the probability that action $a$ in state $s$ at time $t$ will lead to state $s'$ at time $t+1$.
- $\mathcal{R}$ is expected immediate reward.

### Bellman Expectation Equation (BEE)
$$
\begin{aligned}
   V_{\pi}(s)&=\mathbb{E}_{\pi}(G_{t}|S_{t}=s) \\
   &=\mathbb{E}_{\pi}(R_{t+1} + \gamma V_{\pi}(S_{t+1})|S_{t}=s) \\
   &=R(s) + \gamma \sum_{s'\in S_{t+1}} P_{SS'}V_{\pi}(s') \\
   Q_{\pi}(s,a)&=\mathbb{E}_{\pi}(G_{t}|S_{t}=s,A_{t}=a) \\
   &=\mathbb{E}_{\pi}(R_{t+1} + \gamma Q_{\pi}(S_{t+1},A_{t+1})|S_{t}=s,A_{t}=a) \\
   &=R(s,a) + \gamma \sum_{s'\in S_{t+1}} P_{SS'}^{A}V_{\pi}(s') \\
   V_{\pi}(s) &= \sum_{a\in \mathcal{A}}\pi (a|s) Q_{\pi}(s,a)\\
\end{aligned}
$$
$$ *\quad G_{t}=\sum_{\tau=t}^{\infin} \gamma^{\tau-t}R_{\tau+1} $$
$$*\quad P_{SS'}^{A}=P[S_{t+1}=s'|S_{t}=s,A_{t}=a]$$

- Bellman Expectation Backup Operator

$$
\begin{aligned}
   V&=R^{\pi} + \gamma P^{\pi}v = T^{\pi}(v) \\
   &=(I - \gamma P^{\pi})^{-1}R^{\pi}
\end{aligned}
$$

- $\gamma$ - Retraction Morphism(:left inverse morphism)

$$
\begin{aligned}
    \| T^{\pi}(u) - T^{\pi}(v) \|_{p} &\le \gamma \|u-v\|_{p} \\
\end{aligned}
$$

### Bellman Optimality Equation (BOE)
$$
\begin{aligned}
    V^{*}(s)&=\sum_{a\in \mathcal{A}}\pi^{*}(a|s)Q^{*}(s,a)\\
    Q^{*}(s,a)&=R(s,a)+ \gamma \sum_{s'\in \mathcal{A}}P^{A}_{SS'}V^{*}(s') \\

\end{aligned}
$$

- Optimal Policy Theorem

$$\forall \pi,\quad \pi^{*} >\pi \quad \leftrightarrow \quad V_{\pi^{*}}(s)>V_{\pi}(s)$$
$$
\begin{aligned}
    \therefore V^{*}(s)&= \max_{\pi}V_{\pi}(s)=V_{\pi^{*}}(s)\\
    \therefore Q^{*}(s,a)&= \max_{\pi}Q_{\pi}(s,a)=Q_{\pi^{*}}(s,a)\\
\end{aligned}
$$

- Policy Improvement Theorem

$$ \pi'(s) = \argmax_{a\in\mathcal{A}} Q(s,a) $$
$$ \therefore V^{\pi}(s) \le V^{\pi^{*}}(s) $$

- Bellman Optimality Backup Operator

$$T^{*}(V)=\max_{a\in \mathcal{A}}(R^{a}+\gamma P^{a}V)$$

***

## Synchronous Dynamic Programming (Synchronous DP)
### Policy Iteration : Policy Evaluation (PE)
$$ V^{\pi}_{t+1}(s) \leftarrow \sum_{a\in \mathcal{A}}\pi(a|s)(R(s,a) + \gamma \sum_{s'\in S_{t+1}} P_{SS'}^{A}V^{\pi}_{t}(s')) $$
$$until,\quad \max_{s\in \mathcal{S}}|V^{\pi}_{t+1}(s)-V^{\pi}_{t}(s)|\le\epsilon$$
### Policy Iteration : Policy Improvement (PI)
$$ Q^{\pi}_{t+1}(s,a) \leftarrow R(s,a) + \gamma \sum_{s'\in S_{t+1}} P_{SS'}^{A}V^{\pi}_{t}(s') $$
$$
\pi'(a|s) = \begin{cases}
   1 &\text{if } a= \argmax_{a\in \mathcal{A}}Q^{\pi}(s,a) \\
   0 &\text{otherwise} 
\end{cases}
$$

## Asynchronous Dynamic Programming (Asynchronous DP)
### In-place DP (full sweeping)
$$ V(s) = \max_{a\in \mathcal{A}}\{R(s,a)+\gamma \sum_{s'\in\mathcal{S}}P^{A}_{SS'}V(S')\}$$

### Prioritized sweeping
- Bellman Error

$$ Error(s) = |\max_{a\in \mathcal{A}}\{(R(s,a)+\gamma \sum_{s'\in\mathcal{S}}P^{A}_{SS'}V(S'))-V(s)\}| $$

### Real-time DP
$$ V(S_{t}) = \max_{a\in \mathcal{A}}\{R(S_{t},a)+\gamma \sum_{s'\in\mathcal{S}}P^{A}_{S_{t}S'}V(S')\}$$
