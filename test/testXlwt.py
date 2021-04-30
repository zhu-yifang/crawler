import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # create workbook
worksheet = workbook.add_sheet('sheet1')    # create worksheet
for i in range(0,9):
	for j in range(0,i+1):
		# formula = str(i+1) + '*' + str(j+1) + '=' + str((i+1)*(j+1))
		worksheet.write(i,j,'%d * %d = %d' % (i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')    # save