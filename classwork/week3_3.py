def test():
    print("hi")
    return "hello"
getx = test()
print(getx)
def greet():
    print("Record check starting")

greet()
greet()
def greet_record(record_id):
    print(f"Checking {record_id}")

greet_record("srv-01")
greet_record("srv-02")
