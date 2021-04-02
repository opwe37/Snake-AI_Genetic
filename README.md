# Snake-AI_Genetic

![](https://github.com/opwe37/Snake-AI_Genetic/blob/main/image/snake%20game%20training.png)

## Run
```
python ga.py
```

## Approach

**신경망(Neural Network)** + **유전 알고리즘(Genetic Algorithm)**

- 신경망: 주어진 상황에서 뱀의 이동 방향을 결정하는 역할
- 유전 알고리즘: 신경망을 학습시키는 용도(최적화)

## Neural Network

뱀의 두뇌에 해당하는 역할을 수행. Input, Hidden, Output으로 구성

- Input: 9개의 뉴런으로 구성
- Hidden: 3개의 층으로 되어 있으며 각각 20, 20, 10개의 뉴런으로 구성
- Output: 3개의 뉴런으로 구성

### Input & Output

Input의 경우, 뱀의 머리를 기준으로 3방향(전방, 우측, 좌측)에 대한 다음의 정보를 수집하여 제공
- (거리 5이내에) 벽 또는 자신의 몸 유무
- (거리 5이내에) 먹이 유무
- 대략적인 먹이 방향

Output의 경우, 3개의 뉴런으로 각각이 현재 진행방향 고수, 우측 방향 전환, 좌측 방향 전환을 의미한다.

## Genetic Algorithm

생물의 진화 과정을 본뜬 최적화 알고리즘으로 Selection, Crossover, Mutation 과정을 반복하며 최적화를 수행한다.

- Population: 100
- Selection: 엘리트 보존 + 엘리트로 선정된 뱀을 동일한 확률로 랜덤한 선택
- Crossover: 신경망의 각 층별(input->hidden1, hidden1->hidden2, ...)로 싱글-포인트 교배를 실시
- Mutation: 모든 가중치값을 대상으로 0.05의 확률로 돌연변이 발생

Fitness의 경우, 대략적으로 다음과 같은 규칙을 통해 계산되어 진다.
- 뱀이 먹이를 먹는 경우
  - 기본 플러수 점수: 10
  - 추가 점수: 긍정적인 이동 횟수 / 총 이동 횟수 
- 뱀 머리와 먹이와의 거리가 관찰되었던 최소 거리보다 멀어질 때: -0.2

여기서 긍정적인 이동 횟수란, 현재까지 관찰된 먹이와 머리의 최소 거리보다 가까워지게 만드는 이동을 의미한다.

## Result
![](https://github.com/opwe37/Snake-AI_Genetic/blob/main/image/result.png)

위의 그래프는 유전 알고리즘을 통한 여러번의 트레이닝 중 마지막 시도에서 얻은 데이터로, 각 세대의 뱀이 최고 많이 먹은 먹이에 대한 그래프이다. 우상향을 그리고 있으며, 29세대에서 95개의 먹이를 먹은 것이 최고점이다.

## Reference
https://github.com/kairess/genetic_snake
