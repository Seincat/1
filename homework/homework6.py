result = []

def divider(a, b):
    if a < b:
        raise ValueError("a must be greater than or equal to b")
    if b > 100:
        raise IndexError("b must be less than or equal to 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")
print(result)

