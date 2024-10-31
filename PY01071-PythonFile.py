s = input().lower()

print("yes" if len(s) >= 3 and s.find(".py") == len(s)-3 else "no")