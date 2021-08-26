# python3
# coding: utf-8

deductable = 1000 * 12  # 使用租房等最多可以每月扣减1000
yanglaobaoxian_max = 22941  # 广州2021 养老保险缴纳基数上限
yanglaobaoxian_ratio = 0.08
gongjijin_max = 33786  # 广州2021 公积金缴纳基数上限
yigongshegnshi_ratio = 0.022  # 其他四险的比例
gongjijin_ratio = 0.12  # 公积金的公司缴纳比例和个人缴纳比例(一般都是12%)

# 按照年计算
def cal(raw_yearly_income):
	taxable_amount = raw_yearly_income - deductable # 可以扣减的项目
	taxable_amount = taxable_amount - yanglaobaoxian_max * 0.08 * 12
	taxable_amount = taxable_amount - gongjijin_max * yigongshegnshi_ratio * 12
	taxable_amount = taxable_amount - gongjijin_max * gongjijin_ratio * 12
	tax = 0
	if taxable_amount > 36000:
		tax = taxable_amount * 0.10 - 2520
	if taxable_amount > 144000:
		tax = taxable_amount * 0.20 - 16920
	if taxable_amount > 300000:
		tax = taxable_amount * 0.25 - 31920
	if taxable_amount > 420000:
		tax = taxable_amount * 0.30 - 52920
	if taxable_amount > 660000:
		tax = taxable_amount * 0.35 - 85920
	if taxable_amount > 960000:
		tax = taxable_amount * 0.45 - 181920
	return taxable_amount - tax, taxable_amount - tax + gongjijin_max * gongjijin_ratio * 2 * 12

if __name__ == '__main__':
	mode = input('输入是否为高薪模式(年收入打满公积金, 且按照12%缴纳公积金):')
	if mode == 'n':
		gongjijin_max = int(input('输入公积金缴纳基数:'))
		gongjijin_ratio = float(input('输入公积金缴纳比例:'))
	
	raw_yearly_income = input('input yearly income:')
	raw_yearly_income = int(raw_yearly_income)
	year_net_income, year_home_income = cal(raw_yearly_income)
	print('raw_yearly_income', raw_yearly_income)
	print('year:', '不含公积金的纯税后(年)', round(year_net_income), '包含公积金的总收入(年)', round(year_home_income))
	print('month:', '不含公积金的纯税后(月均)', round(year_net_income / 12), '不含公积金的纯税后(月均)', round(year_home_income / 12))
	
