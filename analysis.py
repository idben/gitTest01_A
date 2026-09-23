scores = [72, 85, None, 90, 68, None, 95]
clean_scores = [score for score in scores if score is not None]

print("資料筆數：", len(scores))
print("原始資料：", scores)
print("有效資料筆數：", len(clean_scores))
print("清理後資料：", clean_scores)
if clean_scores:
    print("平均分數：", sum(clean_scores) / len(clean_scores))
    print("最高分數：", max(clean_scores))
    print("最低分數：", min(clean_scores))
else:
    print("沒有可分析的有效資料")