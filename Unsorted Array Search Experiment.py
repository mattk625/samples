import random
import time
from statistics import mean

wait = input("PRESS ENTER TO BUILD ARRAYS FOR EXPERIMENT.")
print("\nBUILDING ARRAYS FOR EXPERIMENT...")

loopArrays = []
runtimeArray = []
avgRuntimesAll = []

#Build some (5 in this case) arrays which increase in size linearly
for i in range(1, 6):
	loopArrays.append(random.sample(range(1, 1000000), 100000*i))

wait = input("\nARRAYS ARE BUILT, PRESS ENTER TO START THE EXPERIMENT.")
print("\nRUNNING EXPERIMENT, PLEASE WAIT A FEW MOMENTS...")

#Generic Array Search Algorithm (Find largest number in the array for this case)
def findMax(myArray):
    myMax = myArray[0]
    for num in myArray:
        if myMax < num:
            myMax = num
    return myMax

for array in loopArrays:
	for i in range(0, 10):
			#---
			start_time = time.clock()
			findMax(array) 
			runtime = (time.clock() - start_time)*1000
			#---
			runtimeArray.append(runtime)
			random.shuffle(array)
	avgRuntimesAll.append(mean(runtimeArray))
	runtimeArray = []
	
#Decided to use JSCanvas in HTML5 for ease of viewing 

chartTitle = 'Average Runtime(ms) of Search on Unsorted Array VS Number(in 100k) of Elements in Array'
xValue = 'Number of Elements'
yValue = 'Average Runtime (in ms)'

Experiment_Results = open('Experiment_Results.html', 'w')
Experiment_Results.write('<!DOCTYPE HTML>\n\
<html>\n\
<head>\n\
	<script type="text/javascript">\n\
	window.onload = function () {\n\
		var chart = new CanvasJS.Chart("chartContainer",\n\
		{\n\
\n\
			title:{\n\
				text: "')
Experiment_Results.write(chartTitle)
Experiment_Results.write('",\n\
				fontSize: 30\n\
			},\n\
                        animationEnabled: true,\n\
			axisX:{\n\
\n\
				gridColor: "Silver",\n\
				tickColor: "silver",\n\
\n\
			},\n\
                        toolTip:{\n\
                          shared:true\n\
                        },\n\
			theme: "theme2",\n\
			axisY: {\n\
				gridColor: "Silver",\n\
				tickColor: "silver"\n\
			},\n\
			legend:{\n\
				verticalAlign: "center",\n\
				horizontalAlign: "right"\n\
			},\n\
			data: [\n\
			{\n\
				type: "line",\n\
				showInLegend: true,\n\
				lineThickness: 2,\n\
				name: "')
Experiment_Results.write(yValue)
Experiment_Results.write('",\n\
				markerType: "square",\n\
				color: "#F08080",\n\
				dataPoints: [\n')
xValues = range(1,6)
yValues = avgRuntimesAll
j = 0
for i in xValues:
    Experiment_Results.write('				{ label: "%(xValue)s", y: %(yValue)s },\n' % {'xValue': i, 'yValue': yValues[j]})
    j += 1
Experiment_Results.write('				]\n\
			},\n\
\n\
			\n\
			],\n\
          legend:{\n\
            cursor:"pointer",\n\
            itemclick:function(e){\n\
              if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {\n\
              	e.dataSeries.visible = false;\n\
              }\n\
              else{\n\
                e.dataSeries.visible = true;\n\
              }\n\
              chart.render();\n\
            }\n\
          }\n\
		});\n\
\n\
chart.render();\n\
}\n\
</script>\n\
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/canvasjs/1.7.0/canvasjs.min.js"></script>\n\
</head>\n\
<body>\n\
	<div id="chartContainer" style="height: 300px; width: 100%;">\n\
	</div>\n\
</body>')
Experiment_Results.write('</html>')
Experiment_Results.close()	
	
wait = input("\nEXPERIMENT COMPLETED. \nHTML FILE (Experiment_Results.html) WITH RESULTS HAS BEEN GENERATED.\nPRESS ENTER TO EXIT.")	
