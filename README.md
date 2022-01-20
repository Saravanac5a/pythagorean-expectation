# pythagorean-expectation
Analyzing the correlation between win percentage and the pythagorean expectation on all the T20 World Cup matches played

One of the most famous theories in sports analysis is the pythagorean expectation. This was invented by Bill James, an American baseball writer, historian, and statistician (yes, the Moneyball guy). He says, the success of a team in a tournament is directly proportional to the square of the total runs scored by the team in the tournament divided by the sum of squares of the total runs scored by the team and its opposition.

On testing this in the case of cricket - in particular, all the T20 World Cup matches ever played, we find that this relation is indeed quite a strong one. In statistics, the p-value describes the correlation between two variables. The closer the p-value is to 0, the stronger the relationship between the variable: in this case, the win percentage and the pythagorean expectation. We get the p-value to be as low as 0.01




What does the graph tell us about outliers? If you consider Bangladesh, they have a relatively high Pythagorean expectation of 0.47 but have a win ratio of only 0.21 to show for it. So statistically speaking, Bangladesh should’ve won a lot more games than they managed to, which means they underperformed and lost quite a few crunch games.

The data for other sports such as baseball has a greater correlation. Why not in cricket? In cricket, the team batting second needs only score one more run than the opponent to win, and so the inning ends if it reaches this milestone. If the team batting second is the winning team, then the gap in the scores will be small. However, if the team batting first can get all ten wickets cheaply, then the gap in scores could be very large

In fact, if the win percentage and the pythagorean expectation upto the middle of a tournament is considered, the pythagorean expectation is a better predictor of the team's success than the win percentage

The beauty of this relationship is that it does not apply only to cricket. It applies to sports such as basketball, baseball, football, ice hockey etc., Tells you how the essence of any sport can be captured through data
