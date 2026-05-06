# ACC Non-Linear Properties

## Benchmark Motivation
The following benchmark was designed to verify the correct handling of non-linear properties as introduced in VNN-LIB 2.0. One way in which this new feature proves useful is when proving properties involving kinematic equations such as the common displacement equation.

$$d = v_i+\frac{1}{2}at^2$$

This benchmark, originally described by Prebet et al., seeks to verify the safety of a network used in adaptive cruise control by ensuring that the output always results in a state where the car has enough space in front of it to avoid a collision [1]. The specifications outlined by Prebet et al. were manually negated and translated to VNN-LIB 2.0 query language, allowing compatible solvers to search for unsafe counterexamples.

## Model Description
The network being verified receives an input tensor of shape $(1,2)$ describing the relative position $X_{rPos}$ and relative velocity $X_{rVel}$ of a car to the car in front of it. The output is a tensor of shape $(1,1)$ describing the level of relative acceleration $Y_{rAccpost}$ the car should apply given the input.

## Properties Description
The property of the network that we wish to verify is that if the vehicle is at a safe distance from the vehicle in front of it, then the action resulting from the network's output will not result in the vehicle creating an unsafe distance between the two of them.

$$
\begin{aligned}
\forall \mathit{rPos}, \mathit{rVel} .\; & \Bigg( \mathit{rPos} > 0 \wedge \mathit{min\_rPos} \le \mathit{rPos} \le \mathit{max\_rPos} \wedge \mathit{min\_rVel} \le \mathit{rVel} \le \mathit{max\_rVel} \wedge \mathit{rPos} \ge \frac{\mathit{rVel}^2}{200} \Bigg) \\
\Rightarrow \;& \Bigg( -100.001 \le \mathit{rAccpost} \le 100.001 \;\wedge \\
& \quad \bigg( (\mathit{rAccpost} \ge 100) \;\vee \\
& \quad\quad \Big( -100 \le \mathit{rAccpost} < 100 \wedge \mathit{rAccpost} \ne 0 \wedge \left( \mathit{rPos} + 0.1\mathit{rVel} + 0.005\mathit{rAccpost} > \frac{(\mathit{rVel} + 0.1\mathit{rAccpost})^2}{200} \right) \\
& \quad\quad\quad \wedge \left( \frac{-\mathit{rVel}}{\mathit{rAccpost}} \notin [0, 0.1] \vee \mathit{rPos} > \frac{\mathit{rVel}^2}{2\mathit{rAccpost}} \right) \Big) \;\vee \\
& \quad\quad \left( \mathit{rAccpost} = 0 \wedge \mathit{rPos} + 0.1\mathit{rVel} > \frac{\mathit{rVel}^2}{200} \right) \bigg) \Bigg)
\end{aligned}
$$

This property guarantees the safety of such neural networks given a control period of $0.1$ seconds, a maximum acceleration/deceleration of $100 m/s^2$, and that the car infront is travelling at a constant velocity. The two-dimensional inputs $(X_{rPos},X_{rVel})$ are partitioned into 50 distinct bounding boxes which are randomly selected to be verified by the solver, determined by the random seed provided by the single numeric argument.

The input constraints ensure that the vehicle is in an intial safe state, where the relative position is greater or equal to the minimum distance required to zero the relative velocity (aka. it is always physically possible to brake to avoid a collision). Inputs outside of this domain are not considered, since no output can guarantee safety from those states.

The output constraints describe the safety of the output of the network. The network is safe if one of the three following conditions are met for every possible input:

1. The network advises to apply maximum deceleration.
2. The network advises zero acceleration and the calculated post state after 0.1 seconds matches the same safety conditions as the initial state.
3. The network advises any other valid acceleration level and the calculated post state after 0.1 seconds matches the same safety conditions as the initial state.

The VNN-LIB 2.0 property encodes the negation of the above property; if any input results in an output where the output is outside the valid acceleration range or none of the previous conditions are met, the benchmark is satisfied and the verifier should output an example of such an input. If all inputs result in a safe output, the benchmark is not satisfied and the solver should output UNSAT.

The kinematic equations used to calculate the safety of the initial and post states use non-linear properties (quadratic equations), as such this benchmark should be useful for verifying the correct handling of non-linear properties.

## References

The specifications were translated into VNN-LIB 2.0 from the original specifications constructed by [Samuel Teuber](https://teuber.dev/) from the following sources:

Prebet, E., Teuber, S., & Platzer, A. (2026). Verification of Autonomous Neural Car Control with KeYmaera X. In F. Ishikawa & M. Leuschel (Eds.), Lecture notes in computer science (Vol. 15728, pp. 288–307). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-94533-5_17

Teuber, S., Mitsch, S., & Platzer, A. (2024). Provably Safe Neural Network Controllers via Differential Dynamic Logic. https://doi.org/10.48550/arxiv.2402.10998

