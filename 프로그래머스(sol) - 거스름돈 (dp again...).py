# 또 dp다... 이 문제는 해당 금액과, 동전의 종류가 주어질때, 해당 동전으로 금액을 결제할 수 있는 방법의 경우의 수를 구하는 문제였다.
# dp는 점화식 설계가 중요해, 점화식을 어떻게 설계할지 충분히 고민했지만... 아직도 많이 부족해서 잘 모르겠더라
# 결론은 현재 n원을 만드는것이니 우선 배열을 초기화해 n원까지의 경우의수를 0으로 초기화해놓는다
# 그 후 0원을 만드는 경우의 수는 1이니 1로 만들어준다.
# 그 후 money 배열을 통해 coin의 종류를 돌면서, 해당 coin으로 dp[amount]를 만들 수 있는 경우의 수를 구한다
# amount가 여기서 2라면 dp[amount] = dp[amount - coin] 인데 기존 dp[amount]의 경우의 수에서 dp[amount-coin]에서 coin원 만큼만 추가하면
# amount 값이 되기때문에, dp[amount]가 되니까 dp[amount] += dp[amount - coin]으로 업데이트 해나간다. 
# 솔직히 다시 풀어도 이렇게 발상이 한번에 나올지는 모르겠다.. 충분히 이 문제의 개념을 익혀서 적어도 이런문제가 나오면
# 다시는 틀리지 않도록 잘 해나가야겠다! 외우자! 모르면! 100번 안되면 200번 하면되니까~ 


def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1  

    for coin in money:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
            print(amount, dp)
            dp[amount] %= MOD  

    return dp[n]

solution(5, [1,2,5])