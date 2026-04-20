# acc-non-linear-properties-benchmark

This benchmark was designed to test queries with non-linear properties. The network being verified is a Adaptive Cruise Control (ACC) network, which receives an input tensor of shape (1,2) describing the relative position and relative velocity of a car to the car in front of it. The output is a tensor of shape (1,1) describing the level of acceleration the car should apply given the input.

These specifications guarantee the safety of such neural networks given a control period of 0.1 seconds and a maximum acceleration/deceleration of 100 m/s^2. The input constraints set the variable bounds to ensure that the vehicle is in an intial safe state, where the relative position is greater or equal to the minimum distance required to zero the relative velocity (aka. it is always physically possible to avoid a collision). Inputs outside of this domain are not considered, since no output can guarantee safety from those states.

The output constraints describe the safety of the output of the network. The network is safe if the one of the three following conditions are met for every possible input.

1. The network advises to apply maximum deceleration.
2. The network advises zero acceleration and the calculated post state after 0.1 seconds matches the same safety conditions as the initial state.
3. The network advises any other valid acceleration level and the calculated post state after 0.1 seconds matches the same safety conditions as the initial state.

If any input results in an output where the output is outside the valid acceleration range or none of the previous conditions are met, the benchmark is satisfied and the verifier should output an example of such an input. If all inputs result in a safe output, the benchmark is not satisfied and the verifier should output UNSAT.

The kinematic equations used to calculate the safety of the initial and post states use non-linear properties (quadratic equations), as such this benchmark should be useful for verifying the correct handling of non-linear properties.

## References

The specifications were translated into VNN-LIB 2.0 from the original specifications constructed by [Samuel Teuber](https://teuber.dev/) from the following sources:

Prebet, E., Teuber, S., & Platzer, A. (2026). Verification of Autonomous Neural Car Control with KeYmaera X. In F. Ishikawa & M. Leuschel (Eds.), Lecture notes in computer science (Vol. 15728, pp. 288–307). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-94533-5_17
