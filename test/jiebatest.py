#encoding=utf-8
import jieba

# 全模式
text = "2018年国家自然科学基金杰出青年基金2017年北京市科学技术奖一等奖（排名1）2016年微软亚洲研究院合作研究奖2015年牛顿高级学者基金2013年中国人工智能学会（CAAI）吴文俊人工智能科学技术（进步）一等奖（排名1）2012年CCF青年科学家奖2012年NSFC优秀青年学者2011年北京科技新星2011年清华大学优秀员工2010年清华学术新人奖2006年度清华大学优秀博士论文"

# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(" ".join(seg_list))
