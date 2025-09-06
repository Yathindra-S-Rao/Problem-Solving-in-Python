text = "Python Code Pad"

words = text.split()
processed = [i[1:-1] for i in words]
print(" ".join(processed))