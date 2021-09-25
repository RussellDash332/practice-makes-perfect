def debug(s):
    try:
        return s + 123
    except ValueError:
        return str(s) + "123"
    except Exception:
        return "F"
    except:
        return "FF"
for q in ["Gday", 42, [0]]:
    print(debug(q))