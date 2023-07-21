def dense_ranking(scores, gits_scores):
    unique_scores = sorted(set(scores), reverse=True)
    rank_dict = {score: rank + 1 for rank, score in enumerate(unique_scores)}
    result = [rank_dict[score] for score in gits_scores]
    return result

def main():
    n = int(input())
    scores = list(map(int, input().split()))
    m = int(input())
    gits_scores = list(map(int, input().split()))

    result = dense_ranking(scores, gits_scores)
    print(*result)

if __name__ == "__main__":
    main()
