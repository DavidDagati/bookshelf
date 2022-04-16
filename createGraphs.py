import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('bookDATA.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[2])
		y.append(int(float(row[4])))

plt.bar(x, y, color = 'g', width = 0.72, label = "Pages")
plt.xlabel('Book')
plt.ylabel('Page Count')
plt.title('Page Count of Books')
plt.legend()
plt.show()
