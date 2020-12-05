scores =[60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48,
         69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55,
         52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55,
         61, 51, 44]
costs = [.25, .27, .25, .25, .25, .25,.33, .31, .25,
         .29, .27, .25,.31, .25, .25, .33, .21, .25,
         .22, .25, .28, .25, .24, .22,.20, .25, .30,
         .25, .24, .25,.25, .25, .27, .25,.26, .29]
 

highest_bubble = 0
for i in range(len(scores)):
    print(f"bubble solution #{i} score:{scores[i]}")
    if scores[i]> highest_bubble:
        highest_bubble = scores[i]
        
solutions = []
for i in range(len(scores)):
    if highest_bubble == scores[i]:
        solutions.append(i)

cost_effective = 0
highest_cost =[]


for x in range(len(costs)):
    if x == solutions[0] or x == solutions[1] :
       highest_cost.append(costs[x])
    

for x in range(len(costs)):
    if highest_cost[0]>highest_cost[1]:
        cost_effective = solutions[1]
    else:
        cost_effective = solutions[0]
#this is the books 1st solution
cost = 100.0
most_effective = 0
for i in range(len(scores)):
    if scores[i] == highest_bubble and costs[i] < cost:
        most_effective = i
        cost = costs[i]
print('Solution', most_effective,
    'is the most effective with a cost of',
    costs[most_effective])

#this is the books 2st solution
cost = 100.0
most_effective = 0
for i in range(len(solutions)):
    index = solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]
print('Solution', most_effective,
      'is the most effective with a cost of',
      costs[most_effective]) 


print(f"\nbubbles tests: {len(scores)}")
print(f"highest_bubble: {highest_bubble}")
#print(f"highest_bubble: {max(scores)}")
print(f"solutions with highest score: {solutions}")
print(f"cost_effective: {cost_effective}")



''''
i=0
while i < len(scores):
    print(f"bubble solution #{i} score:{scores[i]}")
    i += 1
'''
