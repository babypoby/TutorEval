
tp = 0
tn = 64
fp = 0
fn = 34


precision = 0
recall =0

precision_0class = tn / (tn + fn)
recall_0class = tn / (tn + fp)

f1 = 0
f1_0class = 2 * (precision_0class * recall_0class) / (precision_0class + recall_0class)
accuracy = (tp + tn) / (tp + tn + fp + fn)

print(precision)
print(recall)
print (accuracy)
print(f1)

print(precision_0class)
print(recall_0class)
print(f1_0class)