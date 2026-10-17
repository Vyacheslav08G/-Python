def check_winners(scores,s_score):
    s_scores = sorted(scores,reverse=True)
    top1 = s_scores[0]
    top2 = s_scores[1]
    top3 = s_scores[2]
    winners = [top1,top2,top3]
    if s_score in winners:
        print("Вы в тройке победителей")
    else:
        print("Вы не попали в тройку победителей")
